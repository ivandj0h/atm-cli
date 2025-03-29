import json
import os
from tabulate import tabulate
from colorama import init, Fore, Style

init(autoreset=True)

DATA_FILE = "data.json"
NOTIF_KEY = "notifications"


class ATM:
    def __init__(self):
        self.data = self.load_data()
        self.current_user = None

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        return {}

    def save_data(self):
        with open(DATA_FILE, "w") as f:
            json.dump(self.data, f, indent=4)

    def login(self, name):
        if name not in self.data:
            pin = input("Buat PIN baru untuk akun ini: ")
            self.data[name] = {
                "pin": pin,
                "balance": 0,
                "owed_to": {},
                "owed_from": {},
                NOTIF_KEY: [],
                "history": []
            }
            print(Fore.GREEN + "Akun baru berhasil dibuat!")
        else:
            for _ in range(3):
                pin = input("Masukkan PIN: ")
                if pin == self.data[name]["pin"]:
                    break
                else:
                    print(Fore.RED + "PIN salah!")
            else:
                print(Fore.RED + "Terlalu banyak percobaan. Login gagal.")
                return

        self.current_user = name
        print(Fore.CYAN + f"\nHalo, {name}!")
        self.show_notifications()
        self.print_balance()

    def logout(self):
        if self.current_user:
            print(Fore.CYAN + f"Sampai jumpa, {self.current_user}!")
            self.current_user = None
        self.save_data()

    def deposit(self, amount):
        amount = self._validate_amount(amount)
        if amount is None:
            return

        user = self.data[self.current_user]
        user["balance"] += amount
        user["history"].append(f"Deposit Rp{amount:,}")
        print(Fore.GREEN + f"Top up berhasil: Rp{amount:,}")
        self.print_balance()
        self.save_data()

    def withdraw(self, amount):
        amount = self._validate_amount(amount)
        if amount is None:
            return

        user = self.data[self.current_user]
        if user["balance"] >= amount:
            user["balance"] -= amount
            user["history"].append(f"Tarik tunai Rp{amount:,}")
            print(Fore.GREEN + f"Penarikan berhasil: Rp{amount:,}")
        else:
            print(Fore.RED + "Saldo tidak cukup untuk penarikan.")
        self.print_balance()
        self.save_data()

    def transfer(self, target, amount):
        amount = self._validate_amount(amount)
        if amount is None or target == self.current_user:
            print(Fore.RED + "Transfer gagal.")
            return

        sender = self.data[self.current_user]

        if sender["balance"] < amount:
            print(Fore.RED + "Saldo tidak mencukupi. Silakan topup terlebih dahulu.")
            return

        if target not in self.data:
            pin = input(f"Buat PIN baru untuk akun {target}: ")
            self.data[target] = {
                "pin": pin,
                "balance": 0,
                "owed_to": {},
                "owed_from": {},
                NOTIF_KEY: [],
                "history": []
            }
            print(Fore.GREEN + f"Akun {target} berhasil dibuat!")

        sender["balance"] -= amount
        self.data[target]["balance"] += amount
        sender["history"].append(f"Transfer ke {target} Rp{amount:,}")
        self.data[target]["history"].append(f"Menerima dari {self.current_user} Rp{amount:,}")

        # Notifikasi untuk penerima
        self.data[target][NOTIF_KEY].append({
            "from": self.current_user,
            "amount": amount
        })

        print(Fore.GREEN + f"Berhasil transfer Rp{amount:,} ke {target}")
        self.print_balance()
        self.save_data()

    def print_balance(self):
        user = self.data[self.current_user]
        rows = [["Saldo", f"Rp{user['balance']:,}"]]

        for t, v in user["owed_to"].items():
            rows.append([f"Utang ke {t}", f"Rp{v:,}"])

        for f, v in user["owed_from"].items():
            rows.append([f"Piutang dari {f}", f"Rp{v:,}"])

        print(Fore.BLUE + "\nInformasi Akun:")
        print(Fore.BLUE + tabulate(rows, headers=["Tipe", "Jumlah (Rp)"], tablefmt="grid"))

    def show_notifications(self):
        notifs = self.data[self.current_user].get(NOTIF_KEY, [])
        for notif in notifs:
            print(Fore.YELLOW + f"\n[INFO] Kamu menerima Rp{notif['amount']:,} dari {notif['from']}")
        self.data[self.current_user][NOTIF_KEY] = []

    def show_history(self):
        history = self.data[self.current_user].get("history", [])
        if not history:
            print(Fore.YELLOW + "Belum ada riwayat transaksi.")
            return

        print(Fore.MAGENTA + "\nRiwayat Transaksi:")
        for h in history:
            print("-", h)

    def _validate_amount(self, amount):
        try:
            amount = int(amount)
            if amount <= 0:
                raise ValueError
            return amount
        except:
            print(Fore.RED + "Jumlah tidak valid. Gunakan angka bulat positif.")
            return None


def main():
    atm = ATM()
    print(Fore.CYAN + "=== ATM CLI Enterprise Edition ===")
    print("Perintah: login [nama], deposit [jumlah], withdraw [jumlah], transfer [tujuan] [jumlah], history, logout")

    while True:
        try:
            command = input(Fore.WHITE + ">>> ").strip().split()
            if not command:
                continue
            cmd = command[0]

            if cmd == "login" and len(command) == 2:
                atm.login(command[1])
            elif cmd == "logout":
                atm.logout()
            elif cmd == "deposit" and len(command) == 2:
                atm.deposit(command[1])
            elif cmd == "withdraw" and len(command) == 2:
                atm.withdraw(command[1])
            elif cmd == "transfer" and len(command) == 3:
                atm.transfer(command[1], command[2])
            elif cmd == "history":
                atm.show_history()
            else:
                print(Fore.RED + "Perintah tidak dikenal atau salah format.")
        except KeyboardInterrupt:
            print(Fore.CYAN + "\nKeluar dari ATM. Sampai jumpa!")
            break


if __name__ == "__main__":
    main()
