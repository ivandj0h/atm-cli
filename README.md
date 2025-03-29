# 💳 ATM Enterprise Edition - CLI Version

ATM Command Line Interface (CLI) ini adalah simulasi sistem ATM berbasis Python dengan fitur lengkap ala enterprise, cocok untuk demo, pembelajaran, atau proyek pribadi.  😎

---

## 🚀 Fitur Utama

- 🔐 **Login dengan PIN**
- 💸 **Deposit, Withdraw, Transfer**
- 📢 **Notifikasi penerimaan transfer** (hanya tampil sekali saat login)
- 📊 **Tampilan saldo & utang/ piutang dalam bentuk tabel (tabulate)**
- 📜 **Riwayat transaksi per user**
- 🎨 **Tampilan CLI berwarna (colorama)**
- 💾 **Data persistent (tersimpan di `data.json`)**

---

## 🛠️ Cara Setup

### 1. Clone / salin project ini

```bash
mkdir atm-enterprise
cd atm-enterprise
# Simpan file Python dan README ini di dalam folder
```

### 2. Buat Virtual Environment (venv)

```bash
python -m venv venv
source venv/bin/activate        # (Linux/macOS)
venv\Scripts\activate           # (Windows)
```

### 3. Install Dependensi

```bash
pip install tabulate colorama
```

### 4. Jalankan Aplikasinya

```bash
python atm_json_enterprise.py
```

---

## 🧾 Perintah CLI

| Perintah                        | Fungsi                                      |
|--------------------------------|---------------------------------------------|
| `login [nama]`                 | Login (atau buat akun baru + PIN)           |
| `deposit [jumlah]`            | Menambahkan saldo                           |
| `withdraw [jumlah]`           | Menarik uang dari saldo                     |
| `transfer [target] [jumlah]`  | Kirim uang ke pengguna lain                 |
| `history`                      | Lihat semua transaksi sebelumnya            |
| `logout`                       | Keluar dari akun                            |

---

## 📁 Tentang `data.json`

- File ini dibuat otomatis saat pertama kali aplikasi menyimpan data
- Jangan edit manual jika tidak paham format JSON
- Isinya menyimpan semua data user: saldo, utang, PIN, riwayat, dll

---

## 💡 Tips Demo

- Jalankan dari **2 terminal berbeda** untuk simulasi multi-user
- Login sebagai user berbeda dan saling transfer untuk lihat notifikasi real-time
- Tekankan fitur warna-warni & notifikasi saat presentasi 😎

---

## 🧱 Tech Stack (CLI)

- Python 3.x
- tabulate (untuk tampilan tabel)
- colorama (untuk warna terminal)
- JSON file-based storage (data.json)

---

## 🌐 Rencana Ekspansi Web (Next Project)

Aplikasi ini dirancang agar bisa diakses tidak hanya melalui CLI, tetapi juga versi **web-based** yang akan:

- Berbagi data yang sama (mengakses `data.json` yang sama atau via API abstraction)
- Mendukung UI modern dan interaktif
- Cocok untuk kebutuhan enterprise & demo profesional

### 🧱 Tech Stack (Web Frontend - Plan)

- **Next.js 15 (App Router)**
- **Tailwind CSS** (sudah include ketika setup ShadcnUI)
- **shadcn/ui**

> Project Web akan dipisah agar struktur tetap modular dan scalable 🚀

---

## 📌 License

MIT License — Silakan pakai, ubah, fork, tapi jangan lupa traktir kopi kalau suka ☕

---

## 🙌 Credit

Dibuat dengan penuh semangat oleh [ivandjoh @2025](https://github.com/ivanj0h) 💻✨