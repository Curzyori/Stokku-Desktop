# Stokku Desktop 📦

> **Aplikasi Manajemen Persediaan & Mutasi Stok Gudang UMKM Berbasis Python (Offline-First)**

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Database](https://img.shields.io/badge/Database-SQLite3-green.svg)](https://www.sqlite.org/)
[![GUI](https://img.shields.io/badge/GUI-Tkinter%2Fttk-orange.svg)](https://docs.python.org/3/library/tkinter.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📌 Informasi Akademik

Proyek ini dikembangkan untuk memenuhi penilaian **Ujian Tengah Semester (UTS - P08)** dan **Final Project Ujian Akhir Semester (UAS - P11–P16)** pada mata kuliah **Dasar Pemrograman (Python - 894)**:

- **Perguruan Tinggi:** Universitas Bina Sarana Informatika (UBSI)
- **Program Studi / Kelas:** Teknik Informatika / 15.1C.30
- **Dosen Pengampu:** Ali Mustopa, M.Kom (Kode Dosen: AOP)
- **Kelompok:** 4 (Empat)

### 👥 Anggota Tim Pengembang
| No | NIM | Nama Lengkap | Peran Utama |
| :---: | :---: | :--- | :--- |
| 1 | **15260767** | **YUKEN VELINO** | Project Lead, Backend Logic & Data Validation |
| 2 | **15260673** | **MAHARDIKA ATHAILLAH** | Frontend UI & Presentation Designer |
| 3 | **15260847** | **RENKYNA AFTANIA NASUTION** | Reporting Module (Pandas P7) & Academic Documentation |
| 4 | **15260722** | **PRISILA HUTAJULU** | *Status: Sementara / Tentatif — Test Runner & Notulen* |

---

## 🎯 Latar Belakang & Masalah

Sebagian besar pelaku Usaha Mikro, Kecil, dan Menengah (UMKM) masih mengandalkan pencatatan buku fisik untuk mengelola persediaan barang. Masalah yang sering dihadapi meliputi:
- Ketidaktahuan jumlah sisa stok fisik secara riil tanpa menghitung ulang (*stock opname*).
- Keterlambatan pengadaan ulang (*restock*) ketika barang habis di etalase.
- Terjadinya selisih stok akibat barang rusak, kedaluwarsa, atau pemakaian internal yang tidak tercatat.
- Kesulitan menghitung total estimasi modal aset yang tertanam di gudang.

**Stokku Desktop** hadir sebagai aplikasi desktop lokal mandiri (*zero external dependency*) yang ringan, cepat, dan mudah dioperasikan tanpa membutuhkan koneksi internet maupun biaya server.

---

## ✨ Fitur Utama

1. **Dashboard & Ringkasan Eksekutif:**
   - 4 Kartu Metrik: Total Jenis Produk (SKU), Total Kuantitas Fisik, Estimasi Nilai Modal Aset Gudang (Rupiah), dan Jumlah Barang Kritis.
   - Peringatan dini otomatis visual (`[KRITIS / RESTOCK]`) jika stok $\le$ batas minimum aman.
2. **Master Data Barang (Inventory Management):**
   - Tambah barang baru dengan validasi kode alfanumerik unik (*case-insensitive*).
   - Edit informasi produk (nama, kategori, satuan, harga beli, harga jual, minimum stok).
   - Hapus data barang dengan dialog konfirmasi aman.
   - Live Search pencarian instan berdasarkan nama produk atau kode barang.
3. **Transaksi Barang Masuk (Restock):**
   - Penambahan stok fisik dari pemasok/supplier lengkap dengan pencatatan keterangan sumber.
4. **Transaksi Barang Keluar (Anti-Stok Minus):**
   - Pengurangan stok untuk penjualan toko, barang rusak, atau kedaluwarsa.
   - **Validasi Mutlak:** Transaksi otomatis dibatalkan jika jumlah keluar melebihi stok yang tersedia.
5. **Log Riwayat Transaksi Mutasi:**
   - Catatan kronologis seluruh arus keluar-masuk barang lengkap dengan waktu kejadian, stok sebelum, stok sesudah, dan alasan transaksi.
6. **Analisis Data Tabular (Integrasi Pandas):**
   - Konversi data inventaris ke objek `pandas.DataFrame` untuk laporan analisis persediaan (materi Pertemuan 7).

---

## 🛠️ Tech Stack & Dependensi

- **Bahasa Pemrograman:** Python 3 (Python 3.8 s.d. 3.14)
- **Antarmuka Grafis (GUI):** Tkinter & `tkinter.ttk` (Pustaka Standar Python)
- **Basis Data:** SQLite3 (`sqlite3` bawaan Python — berkas lokal `stok_gudang.db`)
- **Analisis Tabular:** Pandas (`pandas.DataFrame`)
- **Dependensi Eksternal:** **0** (*Zero pip install*, kecuali Pandas untuk P07)

---

## 🚀 Roadmap Rilis Versi

### 1. Versi 1.0 (v1.0 — Target Evaluasi UTS Pertemuan 8 | Silabus P01–P07)
- **Fokus:** Mesin Logika Persediaan (*Core In-Memory Stock Engine*) berbasis CLI interaktif.
- **Implementasi Silabus:** Variabel & Tipe Data (P2), String & Operator (P3), Percabangan Anti-Stok Minus (P4), Menu Loop `while True` (P5), Koleksi `list of dicts` & `tuple` (P6), Analisis DataFrame Pandas (P7).
- **Direktori Kerja:** `progress_p7/`.

### 2. Versi 2.0 (v2.0 — Final Project Menuju UAS | Silabus P09–P16)
- **Fokus:** Transformasi Penuh ke Aplikasi Desktop Native Modern dengan GUI Tkinter dan Database SQLite Permanen.
- **Implementasi Silabus:** Fungsi Modular `def` (P9), Multi-Modul & Exception Handling `try...except ValueError` (P10), Desktop Native GUI Tkinter & `ttk.Treeview` (P11–P12), Makalah Laporan Resmi format UBSI & Slide Presentasi PPT (P13–P14), dan Demonstrasi Live di Lab Kampus (P15–P16).
- **Direktori Kerja:** `app/` dan `main.py`.

---

## 📂 Struktur Direktori Proyek

```text
Stokku-Desktop/
├── docs/
│   ├── PRD.md                             # Dokumen Spesifikasi Kebutuhan Produk Lengkap
│   └── TASK.md                            # Rencana Kerja, Checklist & Matriks PIC
├── progress_p7/                           # FASE 1: Mesin In-Memory P1-P7 (Bahan UTS)
│   ├── data_store.py                      # [PIC: YUKEN] Inisialisasi list of dicts & data dummy
│   ├── validasi.py                        # [PIC: YUKEN] Logika validasi input & kode unik
│   ├── engine_stok.py                     # [PIC: YUKEN] Logika mutasi & kalkulasi aset
│   ├── display_cli.py                     # [PIC: MAHARDIKA] Formatting tabel CLI & tag visual
│   ├── laporan_pandas.py                  # [PIC: RENKYNA] Rekapitulasi DataFrame Pandas (P7)
│   ├── test_skenario.py                   # [PIC: PRISILA] Otomasi pengujian 7 kasus uji
│   └── main_p7.py                         # [PIC: YUKEN] Integrator menu utama program CLI
├── app/                                   # FASE 2: Desktop GUI Native & SQLite (Bahan UAS)
│   ├── __init__.py
│   ├── database/
│   │   └── db_manager.py                  # [PIC: YUKEN] Koneksi & query SQLite3
│   ├── services/
│   │   ├── stok_service.py                # [PIC: YUKEN] Aturan bisnis mutasi atomik
│   │   └── validator.py                   # [PIC: YUKEN] Proteksi try-except & sanitasi
│   ├── ui/
│   │   ├── main_window.py                 # [PIC: MAHARDIKA] Window utama Tkinter
│   │   ├── table_view.py                  # [PIC: MAHARDIKA] Komponen ttk.Treeview
│   │   └── dialogs.py                     # [PIC: MAHARDIKA] Form pop-up tambah/mutasi
│   └── reports/
│       └── pandas_reporter.py             # [PIC: RENKYNA] Modul pelaporan & ekspor
├── main.py                                # Titik masuk eksekusi aplikasi desktop
├── LICENSE                                # Lisensi Open-Source MIT
├── .gitignore                             # Berkas pengecualian Git
└── README.md                              # Dokumentasi utama proyek
```

---

## 💻 Cara Menjalankan Aplikasi

### 1. Menjalankan Versi CLI (Fase 1 - Progres P1–P7)
```bash
python progress_p7/main_p7.py
```

Untuk menjalankan script pengujian otomatis:
```bash
python progress_p7/test_skenario.py
```

### 2. Menjalankan Versi Desktop GUI (Fase 2 - Versi Final)
```bash
python main.py
```

---

## 📄 Lisensi

Proyek ini didistribusikan di bawah lisensi **MIT License**. Lihat berkas [LICENSE](LICENSE) untuk rincian selengkapnya.
