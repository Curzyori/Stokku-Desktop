# Rencana Tugas dan Tahapan Kerja (TASK)
## Stokku Desktop, Kelompok 4 (Kelas 15.1C.30)

- Mata Kuliah: Dasar Pemrograman (Kode: 894), UBSI
- Dosen Pengampu: Ali Mustopa, M.Kom (Kode Dosen: AOP)
- Anggota Tim (Kelompok 4):
  - 15260767 - YUKEN VELINO [@Curzyori](https://github.com/Curzyori) (Project Lead, Logika Backend, Validasi Data, dan Test Runner)
  - 15260673 - MAHARDIKA ATHAILLAH [@dikah4300](https://github.com/dikah4300) (Tampilan Antarmuka dan Desain Presentasi)
  - 15260847 - RENKYNA AFTANIA NASUTION [@renkynatania-dotcom](https://github.com/renkynatania-dotcom) (Modul Laporan Pandas P7 dan Naskah Makalah)

---

## Ikhtisar Rencana Kerja

Proyek Stokku Desktop dikerjakan dalam dua fase utama mengikuti agenda perkuliahan semester 1:
1. Fase 1 (Evaluasi UTS Pertemuan 8): Pembuatan logika dasar berbasis terminal (CLI) dengan struktur data di memori, mencakup materi perkuliahan Pertemuan 1 sampai 7.
2. Fase 2 (Evaluasi UAS Pertemuan 11-16): Pengembangan antarmuka desktop menggunakan Tkinter dan penyimpanan SQLite permanen, penerapan fungsi modular (P9), penanganan kesalahan dengan `try-except` (P10), serta penyusunan naskah makalah dan materi presentasi.

---

## Fase 1: Target Evaluasi UTS (Progres P1-P7)

### Pembagian Modul Kerja Mandiri
Untuk mencegah konflik perubahan berkas pada git:
- YUKEN mengerjakan `progress_p7/data_store.py` (struktur data), `progress_p7/validasi.py` (pemeriksaan input dan stok minus), `progress_p7/engine_stok.py` (mutasi kuantitas dan total nilai modal), serta `progress_p7/test_skenario.py` (skrip pengujian otomatis 7 skenario transaksi).
- MAHARDIKA mengerjakan `progress_p7/display_cli.py` (tata letak tabel, batas kolom, garis pemisah, dan format tampilan).
- RENKYNA mengerjakan `progress_p7/laporan_pandas.py` (analisis DataFrame Pandas P7) dan penyusunan naskah makalah evaluasi UTS.
- Berkas `progress_p7/main_p7.py` bertindak sebagai penyatu modul yang mengimpor seluruh fungsi di atas ke dalam menu utama.

---

### Bagian 1: Struktur Data dan Inisialisasi (P01, P02, P06)
- [x] TASK-1.1: Pembuatan folder `progress_p7/` dan berkas modul kerja. (PIC: YUKEN)
- [x] TASK-1.2: Implementasi `progress_p7/data_store.py`:
  - Variabel list `daftar_barang` berisi kumpulan dictionary untuk menyimpan atribut produk.
  - Variabel list `log_mutasi` berisi kumpulan tuple riwayat mutasi barang.
  - Data awal dummy sebanyak 3 produk untuk keperluan demonstrasi program. (PIC: YUKEN)

### Bagian 2: Tampilan Terminal dan Logika Program (P03, P04, P05, P07)
- [x] TASK-1.3: Implementasi `progress_p7/display_cli.py`:
  - Fungsi pencetakan banner pembuka program.
  - Fungsi format tabel daftar barang (lebar kolom rapi, pemisah garis, dan format mata uang Rupiah).
  - Penanda visual status: `[KRITIS]` untuk barang dengan stok kurang dari atau sama dengan batas minimum, dan `[AMAN]` untuk stok cukup. (PIC: MAHARDIKA)
- [x] TASK-1.4: Implementasi `progress_p7/validasi.py`:
  - Validasi kode barang baru (memeriksa keunikan kode menggunakan operator `in`).
  - Validasi input angka bilangan bulat positif (kuantitas lebih dari 0).
  - Validasi batas kuantitas keluar agar tidak melebihi persediaan fisik di gudang. (PIC: YUKEN)
- [x] TASK-1.5: Implementasi `progress_p7/engine_stok.py`:
  - Fungsi penambahan barang baru ke dalam list.
  - Fungsi transaksi barang masuk (restock), menambah stok dan mencatat riwayat mutasi.
  - Fungsi transaksi barang keluar dengan proteksi pencegah stok minus, mengurangi stok jika valid dan mencatat riwayat mutasi.
  - Fungsi perhitungan total unit fisik dan estimasi total nilai modal persediaan. (PIC: YUKEN)
- [x] TASK-1.6: Implementasi `progress_p7/laporan_pandas.py`:
  - Konversi list data barang ke dalam objek `pandas.DataFrame`.
  - Pembuatan ringkasan data tabular persediaan untuk pemenuhan materi Pertemuan 7. (PIC: RENKYNA)
- [x] TASK-1.7: Implementasi `progress_p7/main_p7.py`:
  - Perulangan menu utama menggunakan `while True` dan pemilihan opsi menu dengan `if-elif-else`.
  - Integrasi modul `data_store`, `display_cli`, `validasi`, `engine_stok`, dan `laporan_pandas`. (PIC: YUKEN)

### Bagian 3: Pengujian dan Dokumen Progres UTS (P08)
- [x] TASK-1.8: Implementasi `progress_p7/test_skenario.py`:
  - Pembuatan skrip otomatis untuk menjalankan 7 skenario pengujian transaksi (TC-01 sampai TC-07) tanpa input manual saat penilaian. (PIC: YUKEN)
- [x] TASK-1.9: Penyusunan draf makalah Progres UTS (`docs/makalah/MAKALAH_STOKKU_DESKTOP.md`) dan deck presentasi 10 slide (`docs/presentasi/STOKKU_DESKTOP_PROGRES_P7.pptx`), termasuk slide 1 layar kosong dan slide 8 dokumentasi kegiatan dari `docs/assets/`. (PIC: RENKYNA untuk makalah, YUKEN untuk deck)

---

## Fase 2: Rencana Menuju Evaluasi UAS (P09-P16)
> **Status: seluruh item Fase 2 belum dikerjakan.** Direktori `app/` dan berkas `main.py` belum ada di repositori, sehingga semua kotak centang di bawah masih kosong.
>
> Catatan: TASK-2.11 dan TASK-2.12 adalah target versi UAS (final). Versi UTS-nya sudah selesai lebih awal melalui TASK-1.9, yaitu `docs/makalah/MAKALAH_STOKKU_DESKTOP.md` dan `docs/presentasi/STOKKU_DESKTOP_PROGRES_P7.pptx`.

### Bagian 4: Modularisasi Fungsi dan Penanganan Eksepsi (P09, P10)
- [ ] TASK-2.1 (P09 - Fungsi Modular):
  - Memecah blok kode menjadi fungsi mandiri dengan kata kunci `def`.
  - Menerapkan parameter posisional, kata kunci, dan nilai bawaan (`min_stok=5`).
  - Mengembalikan nilai status dan hasil perhitungan melalui `return`.
  - Membatasi variabel lokal agar tidak bergantung pada variabel global. (PIC: YUKEN)
- [ ] TASK-2.2 (P10 - Penanganan Eksepsi):
  - Memasang blok pelindung `try...except ValueError` pada pembacaan input angka dari pengguna.
  - Membuat pesan kesalahan kustom menggunakan kata kunci `raise`.
  - Menangani potensi benturan data unik pada basis data melalui `sqlite3.IntegrityError`. (PIC: YUKEN)

### Bagian 5: Penyimpanan Data Permanen SQLite (P10)
- [ ] TASK-2.3: Pembuatan modul koneksi basis data `app/database/db_manager.py`.
- [ ] TASK-2.4: Pembuatan fungsi `init_db()` untuk membuat tabel `barang` dan `riwayat_transaksi` secara otomatis jika berkas `stok_gudang.db` belum tersedia.
- [ ] TASK-2.5: Pembuatan fungsi query SQL aman menggunakan parameter pengganti:
  - `get_semua_barang()`
  - `tambah_barang(data)`
  - `update_barang(id, data)`
  - `hapus_barang(id)`
  - `catat_mutasi(barang_id, jenis, kuantitas, keterangan)` dengan transaksi database (`commit` dan `rollback`).
  - `get_riwayat_mutasi(filter_jenis)` (PIC: YUKEN)

### Bagian 6: Antarmuka Desktop Tkinter (P11, P12)
- [ ] TASK-2.6: Pembuatan modul jendela antarmuka pada folder `app/ui/`.
- [ ] TASK-2.7: Perancangan jendela utama Tkinter:
  - Panel ringkasan data (total jenis barang, total unit, total estimasi modal, barang kritis).
  - Kolom pencarian langsung berdasarkan nama atau kode barang.
  - Komponen tabel `ttk.Treeview` disertai bilah penggulung vertikal.
  - Pengaturan warna baris untuk membedakan barang dengan stok kritis secara otomatis. (PIC: MAHARDIKA)
- [ ] TASK-2.8: Pembuatan dialog form input data:
  - Form dialog penambahan dan perubahan data barang.
  - Form dialog pencatatan barang masuk (restock).
  - Form dialog pencatatan barang keluar dengan peringatan stok tidak mencukupi. (PIC: MAHARDIKA)
- [ ] TASK-2.9: Pembuatan tab tampilan riwayat transaksi mutasi disertai tombol penyaring (`SEMUA`, `MASUK`, `KELUAR`). (PIC: MAHARDIKA dan YUKEN)

### Bagian 7: Titik Masuk Program Utama
- [ ] TASK-2.10: Pembuatan berkas `main.py` di direktori utama proyek sebagai titik masuk eksekusi antarmuka desktop. (PIC: YUKEN)

### Bagian 8: Makalah Akademik, Slide Presentasi, dan Demonstrasi (P13-P16)
- [ ] TASK-2.11 (Makalah Resmi UBSI):
  - Penyusunan dokumen makalah laporan akhir sesuai pedoman resmi UBSI:
    - Halaman Judul (Logo UBSI, Nama Dosen: Ali Mustopa, M.Kom, Kelompok 4).
    - Kata Pengantar dan Daftar Isi.
    - Bab I: Pendahuluan (Latar Belakang, Maksud dan Tujuan, Ruang Lingkup).
    - Bab II: Pembahasan (Analisis Kebutuhan, Perancangan Database, Desain Antarmuka, dan Penjelasan Kode Program Sesuai Silabus P1-P10).
    - Bab III: Penutup (Kesimpulan dan Saran Pengembangan).
    - Daftar Pustaka dan Lampiran Cuplikan Kode Program serta Tangkapan Layar Aplikasi. (PIC: RENKYNA)
- [ ] TASK-2.12 (Slide Presentasi PPT):
  - Penyusunan materi presentasi PowerPoint (.pptx dan .pdf) di folder `docs/presentasi/`:
    - Slide 1: Judul Proyek dan Anggota Kelompok.
    - Slide 2: Latar Belakang Masalah Pengelolaan Stok.
    - Slide 3: Diagram Alur Kerja dan Struktur Modul.
    - Slide 4: Pembuktian Penerapan Silabus Materi P1-P10.
    - Slide 5: Tangkapan Layar Program Berjalan.
    - Slide 6: Kesimpulan. (PIC: MAHARDIKA)
- [ ] TASK-2.13 (Uji Coba Demonstrasi Akhir):
  - Uji coba skenario input keliru (input huruf pada kolom angka, nilai minus, dan kuantitas keluar berlebih).
  - Memastikan program berjalan stabil tanpa error saat demonstrasi di hadapan Dosen Pengampu. (PIC: Seluruh Anggota Tim)

---

## Matriks Tanggung Jawab Anggota Tim

| ID Tugas | Deskripsi Tugas | Berkas / Modul Terkait | Penanggung Jawab (PIC) | Target Penyelesaian |
| :--- | :--- | :--- | :---: | :---: |
| **TASK-1.1 s.d. 1.2** | Struktur Data dan Data Awal | `progress_p7/data_store.py` | YUKEN VELINO | Evaluasi UTS |
| **TASK-1.3** | Format Tampilan CLI dan Status Kritis | `progress_p7/display_cli.py` | MAHARDIKA ATHAILLAH | Evaluasi UTS |
| **TASK-1.4** | Validasi Input dan Keunikan Kode | `progress_p7/validasi.py` | YUKEN VELINO | Evaluasi UTS |
| **TASK-1.5** | Logika Mutasi Stok dan Nilai Aset | `progress_p7/engine_stok.py` | YUKEN VELINO | Evaluasi UTS |
| **TASK-1.6** | Modul Analisis Pandas DataFrame | `progress_p7/laporan_pandas.py` | RENKYNA AFTANIA N. | Evaluasi UTS |
| **TASK-1.7** | Menu Utama Program Terminal | `progress_p7/main_p7.py` | YUKEN VELINO | Evaluasi UTS |
| **TASK-1.8** | Skrip Pengujian Otomatis 7 Kasus | `progress_p7/test_skenario.py` | YUKEN VELINO | Evaluasi UTS |
| **TASK-1.9** | Makalah UTS dan Slide PPT | `docs/makalah/` & `docs/presentasi/` | RENKYNA (makalah) & YUKEN (slide) | Selesai |
| **TASK-2.1 s.d. 2.2** | Fungsi Modular dan Penanganan Eksepsi | `app/services/` | YUKEN VELINO | Pasca UTS |
| **TASK-2.3 s.d. 2.5** | Basis Data Relasional SQLite3 | `app/database/db_manager.py` | YUKEN VELINO | Pasca UTS |
| **TASK-2.6 s.d. 2.9** | Antarmuka Desktop Tkinter dan Tabel | `app/ui/` | MAHARDIKA ATHAILLAH | Pasca UTS |
| **TASK-2.10** | Titik Masuk Eksekusi Aplikasi Desktop | `main.py` | YUKEN VELINO | Pasca UTS |
| **TASK-2.11** | Makalah Lengkap Format Resmi UBSI | `docs/makalah/` | RENKYNA AFTANIA N. | Menuju UAS |
| **TASK-2.12** | Slide Presentasi Final PPT | `docs/presentasi/` | MAHARDIKA ATHAILLAH | Menuju UAS |
| **TASK-2.13** | Demonstrasi dan Pengujian Akhir | Keseluruhan Program | Seluruh Anggota Tim | Pertemuan 11-16 |
