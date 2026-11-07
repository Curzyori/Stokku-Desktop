# RENCANA TUGAS & TAHAPAN KERJA (TASK.md)
# STOKKU DESKTOP — KELOMPOK 4 (KELAS 15.1C.30)

- **Mata Kuliah:** Dasar Pemrograman (Kode: 894) — UBSI
- **Dosen Pengampu:** Ali Mustopa, M.Kom (Kode Dosen: AOP)
- **Tim Pengembang (Kelompok 4):**
  - **15260767 — YUKEN VELINO** — Project Lead, Backend Logic & Data Validation
  - **15260673 — MAHARDIKA ATHAILLAH** — Frontend UI & Presentation Designer
  - **15260847 — RENKYNA AFTANIA NASUTION** — Reporting Module (Pandas P7) & Academic Documentation
  - **15260722 — PRISILA HUTAJULU** *(Status: Anggota Sementara / Tentatif — Test Runner & Notulen)*

---

## IKHTISAR RENCANA KERJA

Proyek **Stokku Desktop** dikerjakan dalam dua fase utama mengikuti kalender akademik perkuliahan:
1. **Fase 1 (Target Besok / Evaluasi UTS Pertemuan 8):** Implementasi Mesin Logika *In-Memory* berbasis CLI interaktif murni materi **Pertemuan 1 s.d. 7**.
2. **Fase 2 (Menuju Evaluasi UAS Pertemuan 11–16):** Evolusi ke **Aplikasi Desktop Native Tkinter** dengan basis data permanen **SQLite3**, fungsi modular (P9), multi-file dengan `try-except` (P10), makalah akademik, dan slide demonstrasi.

---

## FASE 1: TARGET BESOK (PROGRES P1–P7 / EVALUASI UTS)

### Strategi Pencegahan Konflik Kode (Isolated File Architecture)
Agar setiap orang dapat mengerjakan bagiannya secara paralel tanpa saling menimpa kode:
- **YUKEN** fokus di `progress_p7/data_store.py` (struktur data), `progress_p7/validasi.py` (logika validasi & anti-minus), dan `progress_p7/engine_stok.py` (mutasi & kalkulasi aset).
- **MAHARDIKA** fokus di `progress_p7/display_cli.py` (formatting tabel, alignment, border garis, banner).
- **RENKYNA** fokus di `progress_p7/laporan_pandas.py` (rekap DataFrame P7) dan penyusunan draf makalah laporan UBSI.
- **PRISILA (Tentatif)** fokus di `progress_p7/test_skenario.py` (script pengujian otomatis).
- File `progress_p7/main_p7.py` hanya bertindak sebagai perangkai (*integrator*) yang mengimpor modul masing-masing.

---

### Bagian 1: Inisialisasi & Struktur Data (P01, P02, P06)
- [ ] **TASK-1.1:** Setup direktori kerja `progress_p7/` dan inisialisasi file modular. *(PIC: YUKEN)*
- [ ] **TASK-1.2:** Implementasi `progress_p7/data_store.py`:
  - List `daftar_barang` berisi kumpulan dictionary produk dengan atribut lengkap.
  - List `log_mutasi` berisi kumpulan tuple riwayat kejadian mutasi.
  - Mengisi 3 data dummy awal untuk demonstrasi. *(PIC: YUKEN)*

### Bagian 2: Tampilan & Logika Bisnis (P03, P04, P05, P07)
- [ ] **TASK-1.3:** Implementasi `progress_p7/display_cli.py`:
  - Fungsi cetak banner pembuka aplikasi Stokku.
  - Fungsi format tabel daftar barang rapi (lebar kolom proporsional, pemisah `===`, format mata uang Rupiah).
  - Format tag visual: `[KRITIS]` untuk barang dengan stok $\le$ batas minimum dan `[AMAN]`. *(PIC: MAHARDIKA)*
- [ ] **TASK-1.4:** Implementasi `progress_p7/validasi.py`:
  - Fungsi validasi kode barang baru (cek keunikan kode agar tidak duplikat via operator `in`).
  - Fungsi validasi input angka bulat positif $> 0$.
  - Fungsi validasi batas stok keluar tidak boleh melebihi stok yang ada di gudang. *(PIC: YUKEN)*
- [ ] **TASK-1.5:** Implementasi `progress_p7/engine_stok.py`:
  - Logika transaksi penambahan barang baru ke list.
  - Logika transaksi barang masuk (restock) $\rightarrow$ `stok += jumlah` & catat log.
  - Logika transaksi barang keluar $\rightarrow$ validasi anti-stok minus $\rightarrow$ `stok -= jumlah` & catat log.
  - Logika kalkulasi total unit fisik dan estimasi total aset modal gudang. *(PIC: YUKEN)*
- [ ] **TASK-1.6:** Implementasi `progress_p7/laporan_pandas.py`:
  - Konversi list data barang ke objek `pandas.DataFrame`.
  - Menampilkan ringkasan data tabular inventaris untuk pembuktian materi P07. *(PIC: RENKYNA)*
- [ ] **TASK-1.7:** Implementasi `progress_p7/main_p7.py`:
  - Perulangan menu `while True` dan seleksi percabangan `if...elif...else`.
  - Mengintegrasikan modul `data_store`, `display_cli`, `validasi`, `engine_stok`, dan `laporan_pandas`. *(PIC: YUKEN)*

### Bagian 3: Pengujian & Dokumentasi UTS (P08)
- [ ] **TASK-1.8:** Implementasi `progress_p7/test_skenario.py`:
  - Otomasi pengujian 7 kasus uji (TC-01 s.d. TC-07) tanpa input manual untuk pembuktian ke dosen. *(PIC: PRISILA)*
- [ ] **TASK-1.9:** Penyusunan draf Bab II Makalah Progres UTS dan 5 slide presentasi ringkas. *(PIC: MAHARDIKA & RENKYNA)*

---

## FASE 2: ROADMAP VERSI 2.0 (MENUJU EVALUASI UAS P09–P16)

### Bagian 4: Modularisasi Fungsi & Exception Handling (Slide 09 & 10)
- [ ] **TASK-2.1 (Slide 09 - Fungsi Modular):**
  - Memecah kode logika menjadi fungsi-fungsi terpisah dengan kata kunci `def`.
  - Menetapkan parameter posisional, keyword, dan default (`min_stok=5`).
  - Mengembalikan nilai hasil kalkulasi dan status operasi via `return`.
  - Mengisolasi variabel lokal agar tidak mencemari scope global. *(PIC: Yuken)*
- [ ] **TASK-2.2 (Slide 10 - Exception Handling):**
  - Memasang blok proteksi `try...except ValueError` pada seluruh pembacaan input angka.
  - Memasang validasi kustom dengan memicu kata kunci `raise ValueError("Pesan")`.
  - Menangani error basis data via `sqlite3.IntegrityError` untuk mencegah crash. *(PIC: Tiara)*

### Bagian 5: Basis Data SQLite Permanen (Slide 10 & Praktikum)
- [ ] **TASK-2.3:** Membuat modul `app/database.py`.
- [ ] **TASK-2.4:** Membuat fungsi `init_db()` yang otomatis membuat tabel `barang` dan `riwayat_transaksi` jika berkas `stok_gudang.db` belum ada.
- [ ] **TASK-2.5:** Membuat fungsi query SQL aman (parameterized queries):
  - `get_semua_barang()`
  - `tambah_barang(data)`
  - `update_barang(id, data)`
  - `hapus_barang(id)`
  - `catat_mutasi(barang_id, jenis, kuantitas, keterangan)` menggunakan transaksi atomik (`commit`/`rollback`).
  - `get_riwayat_mutasi(filter_jenis)` *(PIC: Yuken)*

### Bagian 6: Antarmuka Desktop Native Tkinter (Slide 11 & 12)
- [ ] **TASK-2.6:** Membuat modul antarmuka `app/ui.py`.
- [ ] **TASK-2.7:** Membangun layout Window Utama Tkinter:
  - Header & Panel Kartu Ringkasan (Total SKU, Total Unit, Total Nilai Aset, Barang Kritis).
  - Kolom Live Search pencarian instan nama atau kode.
  - Komponen tabel `ttk.Treeview` lengkap dengan vertical scrollbar.
  - Konfigurasi tag warna: baris stok kritis diberi warna kuning/merah muda secara otomatis.
- [ ] **TASK-2.8:** Membuat Dialog Modal Form:
  - Form Tambah / Edit Barang.
  - Form Transaksi Barang Masuk (Restock).
  - Form Transaksi Barang Keluar (dengan pesan validasi stok).
- [ ] **TASK-2.9:** Membuat Tab Riwayat Transaksi Mutasi dengan tombol filter (`SEMUA`, `MASUK`, `KELUAR`). *(PIC: Dika & Yuken)*

### Bagian 7: Entry Point & Integrasi Sistem
- [ ] **TASK-2.10:** Membuat file `main.py` di root proyek sebagai entry point eksekusi:
  ```python
  from app.database import init_db
  from app.ui import StokkuApp

  if __name__ == "__main__":
      init_db()
      app = StokkuApp()
      app.run()
  ```
  *(PIC: Yuken)*

### Bagian 8: Makalah Akademik, Slide PPT & Live Demo (Slide 13–16)
- [ ] **TASK-2.11 (Makalah Resmi UBSI):**
  - Menyusun dokumen makalah laporan akhir sesuai format resmi:
    - Cover (Logo UBSI, Nama Dosen: Ali Mustopa, M.Kom - AOP, Kelompok 4).
    - Kata Pengantar & Daftar Isi.
    - Bab I: Pendahuluan (Latar Belakang, Maksud/Tujuan, Ruang Lingkup).
    - Bab II: Pembahasan (Analisis Sistem, Skema Database, Mockup UI, Pembahasan Kode Materi P1–P10).
    - Bab III: Penutup (Kesimpulan & Saran).
    - Daftar Pustaka & Lampiran Source Code serta Screenshot Running. *(PIC: Tiara)*
- [ ] **TASK-2.12 (Slide Presentasi PPT):**
  - Membuat slide presentasi PowerPoint (.pptx) profesional:
    - Slide 1: Judul Proyek & Tim Pengembang.
    - Slide 2: Latar Belakang Masalah UMKM.
    - Slide 3: Flowchart & Arsitektur Sistem.
    - Slide 4: Pembuktian Pemetaan Materi Silabus P1–P10.
    - Slide 5: Tangkapan Layar Aplikasi Berjalan.
    - Slide 6: Kesimpulan & Sesi Q&A. *(PIC: Dika)*
- [ ] **TASK-2.13 (Uji Coba Demo Final):**
  - Menjalankan uji coba skenario ekstrem (input huruf, nilai negatif, stok minus, kode duplikat).
  - Memastikan aplikasi 100% bebas crash saat demonstrasi di hadapan Dosen Pengampu Ali Mustopa, M.Kom. *(PIC: Seluruh Anggota Tim)*

---

## MATRIKS TANGGUNG JAWAB ANGGOTA TIM
| ID Tugas | Deskripsi Tugas | Berkas Modul | Penanggung Jawab (PIC) | Target Selesai |
| :--- | :--- | :--- | :---: | :---: |
| **TASK-1.1 s.d. 1.2** | Inisialisasi Koleksi & Data Dummy | `progress_p7/data_store.py` | YUKEN VELINO | Besok |
| **TASK-1.3** | Formatting Tabel CLI & Tag Kritis | `progress_p7/display_cli.py` | MAHARDIKA ATHAILLAH | Besok |
| **TASK-1.4** | Logika Validasi Input & Kode Unik | `progress_p7/validasi.py` | YUKEN VELINO | Besok |
| **TASK-1.5** | Logika Mutasi, Anti-Minus & Aset | `progress_p7/engine_stok.py` | YUKEN VELINO | Besok |
| **TASK-1.6** | Modul Analisis Pandas DataFrame | `progress_p7/laporan_pandas.py` | RENKYNA AFTANIA N. | Besok |
| **TASK-1.7** | Integrasi Menu Program Utama | `progress_p7/main_p7.py` | YUKEN VELINO | Besok |
| **TASK-1.8** | Otomasi Pengujian 7 Kasus Uji | `progress_p7/test_skenario.py` | PRISILA HUTAJULU | Besok |
| **TASK-1.9** | Draf Bab II Makalah & Slide PPT | `docs/` & PPT | MAHARDIKA & RENKYNA | Evaluasi P8 |
| **TASK-2.1 s.d. 2.2** | Fungsi Modular & Error Handling | `app/services/` & `validator.py`| YUKEN & RENKYNA | Pasca UTS |
| **TASK-2.3 s.d. 2.5** | Basis Data Relasional SQLite3 | `app/database/db_manager.py` | YUKEN VELINO | Pasca UTS |
| **TASK-2.6 s.d. 2.9** | Antarmuka Desktop Tkinter & ttk | `app/ui/` | MAHARDIKA ATHAILLAH | Pasca UTS |
| **TASK-2.10** | Entry Point Aplikasi Desktop | `main.py` | YUKEN VELINO | Pasca UTS |
| **TASK-2.11** | Makalah Lengkap Format UBSI | `docs/makalah/` | RENKYNA AFTANIA N. | Menuju UAS |
| **TASK-2.12** | Slide Presentasi Final PPT | `presentation/` | MAHARDIKA ATHAILLAH | Menuju UAS |
| **TASK-2.13** | Live Demo & Pengujian Akhir | Keseluruhan Sistem | Tim Kelompok 4 | Pertemuan 11–16 |
