# Modul Tampilan Terminal (display_cli.py) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Membangun modul tampilan antarmuka CLI terminal (progress_p7/display_cli.py) untuk aplikasi Stokku Desktop sesuai pembagian tugas Mahardika Athaillah (TASK-1.3).

**Architecture:** Modul murni Python tanpa pustaka pihak ketiga eksternal, mengimplementasikan utilitas format mata uang Rupiah, penentuan status stok visual, kartu ringkasan gudang, dan perenderan tabel ASCII terstruktur dengan lebar kolom adaptif/terstandarisasi.

**Tech Stack:** Python 3 (standard library murni: sys, typing).

**Spec:** docs/PRD.md dan docs/TASK.md (Bagian TASK-1.3, PIC: MAHARDIKA ATHAILLAH).

## Global Constraints

- Pustaka bawaan Python murni (tanpa external library seperti tabulate).
- Bebas karakter em dash pada teks antarmuka dan dokumentasi kode.
- Penanda visual status: [KRITIS] bila stok <= min_stok, [AMAN] bila stok > min_stok.
- Format mata uang Rupiah terstandarisasi: Rp diikuti spasi dan pemisah ribuan titik (contoh: Rp 75.000).
- Komentar kode hanya untuk aturan bisnis penting, dilarang komentar generik.

## Review Focus

- Penanganan daftar barang kosong (tabel tidak boleh crash atau berantakan saat data kosong).
- Penanganan angka stok 0 dan nilai negatif pada status stok.
- Penanganan nama barang panjang agar tidak merusak perataan kolom tabel.
- Dukungan format riwayat mutasi baik berupa dictionary maupun tuple data_store.
- Format nominal 0 rupiah tetap tampil valid sebagai Rp 0.

---

### Task 1: Setup Branch Git dan Skrip Pengujian Unit Tampilan

**Files:**
- Create: `tests/test_display_cli.py`

**Interfaces:**
- Consumes: `progress_p7.display_cli` (format_rupiah, status_stok, buat_baris_tabel, format_ringkasan)
- Produces: Test suite otomatis untuk validasi modul display_cli

- [ ] **Step 1: Buat branch baru untuk fitur tampilan CLI**
Run: `git checkout -b feat/tabel-cli-mahardika`
Expected: Switched to a new branch 'feat/tabel-cli-mahardika'

- [ ] **Step 2: Tulis test awal yang gagal pada tests/test_display_cli.py**
Membuat pengujian untuk format_rupiah, status_stok, format_ringkasan, dan tabel_barang.

- [ ] **Step 3: Jalankan pengujian untuk verifikasi kegagalan (RED)**
Run: `python -m unittest tests/test_display_cli.py`
Expected: FAIL / ModuleNotFoundError (karena modul progress_p7.display_cli belum ada).

---

### Task 2: Implementasi Fungsi Format dan Logika Status

**Files:**
- Create: `progress_p7/display_cli.py`

**Interfaces:**
- Produces:
  - `format_rupiah(nominal: int) -> str`
  - `status_stok(stok: int, min_stok: int) -> str`
  - `tampilkan_banner() -> None`
  - `tampilkan_ringkasan(total_sku: int, total_unit: int, total_aset: int, total_kritis: int) -> None`

- [ ] **Step 1: Implementasi fungsi pembantu format dan status di progress_p7/display_cli.py**
- [ ] **Step 2: Jalankan pengujian unit Task 2**
Run: `python -m unittest tests/test_display_cli.py`
Expected: Sebagian tes format dan status lolos (GREEN).

---

### Task 3: Implementasi Format Tabel Persediaan dan Riwayat Mutasi

**Files:**
- Modify: `progress_p7/display_cli.py`
- Modify: `tests/test_display_cli.py`

**Interfaces:**
- Produces:
  - `tampilkan_tabel_barang(daftar_barang: list) -> None`
  - `tampilkan_tabel_riwayat(daftar_mutasi: list) -> None`
  - `tampilkan_pesan_sukses(pesan: str) -> None`
  - `tampilkan_pesan_error(pesan: str) -> None`

- [ ] **Step 1: Tambahkan pengujian rendering tabel dengan data dummy dan data kosong**
- [ ] **Step 2: Implementasikan perenderan tabel dengan border ASCII rapi di progress_p7/display_cli.py**
- [ ] **Step 3: Jalankan seluruh pengujian unit**
Run: `python -m unittest tests/test_display_cli.py`
Expected: Seluruh tes PASS (100% lolos).

---

### Task 4: Verifikasi Mandiri dan Komit Standar Git

**Files:**
- Tracked: `progress_p7/display_cli.py`
- Tracked: `tests/test_display_cli.py`

- [ ] **Step 1: Eksekusi langsung modul display_cli.py via CLI untuk demonstrasi visual**
Run: `python progress_p7/display_cli.py`
Expected: Output banner, ringkasan kartu, tabel barang dengan status [KRITIS] dan [AMAN], serta tabel riwayat mutasi tercetak rapi tanpa glitch tampilan.

- [ ] **Step 2: Komit perubahan dengan pesan Bahasa Indonesia sesuai AGENTS.md**
Run: `git add progress_p7/display_cli.py tests/test_display_cli.py docs/superpowers/plans/2026-11-08-display-cli.md`
Run: `git commit -m "feat: implementasi antarmuka tabel cli dan format status stok"`
Expected: Commit tersimpan di branch `feat/tabel-cli-mahardika`.
