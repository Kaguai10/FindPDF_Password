# 📄 PDF Bruteforce Tool

Alat sederhana berbasis Python untuk melakukan brute force pada file PDF terenkripsi menggunakan wordlist.

---

## 🚀 Fitur

* Input via argumen command line (bukan hardcoded atau interaktif)
* Validasi keberadaan file PDF dan wordlist
* Menampilkan status percobaan setiap password
* Menampilkan password jika berhasil ditemukan

---

## 🛠️ Instalasi

1. **Klon repositori ini** (jika kamu mengunggahnya ke GitHub):

   ```bash
   git clone https://github.com/kamu/pdf-bruteforce-tool.git
   cd pdf-bruteforce-tool
   ```

2. **Install dependency**:

   ```bash
   pip install -r requirements.txt
   ```

---

## 📦 Penggunaan

```bash
python bruteforce_pdf.py -f path_ke_file_pdf -w path_ke_wordlist
```

Contoh:

```bash
python bruteforce_pdf.py -f file_terkunci.pdf -w wordlist.txt
```

---

## 📂 Struktur Proyek

```
📁 pdf-bruteforce-tool/
├── bruteforce_pdf.py        # Skrip utama
├── wordlist.txt             # Contoh wordlist
├── file_terkunci.pdf        # (Opsional) contoh file PDF terenkripsi
├── requirements.txt         # Dependency Python
└── README.md                # Dokumentasi
```

---

## ⚠️ Disclaimer

Alat ini dibuat untuk tujuan edukasi dan pengujian keamanan. **Jangan digunakan untuk aktivitas ilegal atau tanpa izin.**

---

## 📬 Kontribusi

Pull request dan saran sangat diterima! Jangan ragu untuk fork dan mengembangkan lebih lanjut 🚀

