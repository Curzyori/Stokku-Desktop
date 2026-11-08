"""
Menu Utama & Integrator Program CLI Stokku Desktop (Pertemuan 4 & 5)
PIC: YUKEN VELINO (15260767 / @Curzyori) - Kelompok 4 Dasar Pemrograman 15.1C.30
Dosen Pengampu: Ali Mustopa, M.Kom (AOP) - UBSI
"""

import sys
from data_store import daftar_barang, log_mutasi
from engine_stok import (
    cek_status_stok,
    ringkasan_inventaris,
    tambah_barang_baru,
    transaksi_barang_keluar,
    transaksi_barang_masuk,
)
from validasi import (
    cari_barang_by_kode,
    validasi_angka_positif,
    validasi_kode_unik,
    validasi_string_tidak_kosong,
)


def cetak_banner_bawaan():
    print("=" * 72)
    print("            STOKKU DESKTOP - MANAJEMEN PERSEDIAAN GUDANG            ")
    print("           Tugas Proyek Mata Kuliah Dasar Pemrograman (894)         ")
    print("      Kelas 15.1C.30 - Universitas Bina Sarana Informatika (UBSI)    ")
    print("=" * 72)


def format_rupiah(angka: int) -> str:
    return f"Rp {angka:,.0f}".replace(",", ".")


def tampilkan_tabel_barang_bawaan():
    try:
        from display_cli import cetak_tabel_barang
        cetak_tabel_barang(daftar_barang)
        return
    except ImportError:
        pass

    print("\n" + "-" * 78)
    print(f"{'KODE':<8} | {'NAMA PRODUK':<30} | {'STOK':<6} | {'SATUAN':<6} | {'HARGA BELI':<12} | {'STATUS':<8}")
    print("-" * 78)

    if not daftar_barang:
        print(" Data inventaris masih kosong.")
    else:
        for item in daftar_barang:
            status = cek_status_stok(item["stok"], item["min_stok"])
            tag_status = f"[{status}]"
            harga_teks = format_rupiah(item["harga_beli"])
            print(f"{item['kode']:<8} | {item['nama'][:30]:<30} | {item['stok']:<6} | {item['satuan']:<6} | {harga_teks:<12} | {tag_status:<8}")

    print("-" * 78)
    ringkasan = ringkasan_inventaris(daftar_barang)
    print(f"Total SKU: {ringkasan['total_sku']} | Total Unit: {ringkasan['total_unit']} | Total Modal: {format_rupiah(ringkasan['total_aset'])} | Stok Kritis: {ringkasan['total_kritis']}")
    print("-" * 78)


def tampilkan_log_mutasi_bawaan():
    try:
        from display_cli import cetak_log_mutasi
        cetak_log_mutasi(log_mutasi)
        return
    except ImportError:
        pass

    print("\n" + "-" * 88)
    print(f"{'WAKTU':<19} | {'KODE':<8} | {'JENIS':<6} | {'JML':<5} | {'SEBELUM':<7} | {'SESUDAH':<7} | {'KETERANGAN':<20}")
    print("-" * 88)

    if not log_mutasi:
        print(" Belum ada riwayat mutasi transaksi.")
    else:
        for log in reversed(log_mutasi):
            waktu, kode, nama, jenis, jml, seb, ses, ket = log
            print(f"{waktu:<19} | {kode:<8} | {jenis:<6} | {jml:<5} | {seb:<7} | {ses:<7} | {ket[:20]:<20}")

    print("-" * 88)


def menu_tambah_barang():
    print("\n--- FORM TAMBAH BARANG BARU ---")
    kode_input = input("Masukkan Kode Barang (misal: ATK04): ").strip()
    valid_kode, hasil_kode = validasi_kode_unik(kode_input, daftar_barang)
    if not valid_kode:
        print(f"[Peringatan] {hasil_kode}")
        return

    nama_input = input("Masukkan Nama Produk: ").strip()
    valid_nama, hasil_nama = validasi_string_tidak_kosong(nama_input, "Nama barang")
    if not valid_nama:
        print(f"[Peringatan] {hasil_nama}")
        return

    kategori_input = input("Masukkan Kategori: ").strip()
    valid_kat, hasil_kat = validasi_string_tidak_kosong(kategori_input, "Kategori")
    if not valid_kat:
        print(f"[Peringatan] {hasil_kat}")
        return

    satuan_input = input("Masukkan Satuan (Pcs/Rim/Dus/Pack): ").strip()
    valid_sat, hasil_sat = validasi_string_tidak_kosong(satuan_input, "Satuan")
    if not valid_sat:
        print(f"[Peringatan] {hasil_sat}")
        return

    harga_beli_raw = input("Masukkan Harga Beli Modal (Rp): ").strip()
    valid_hb, harga_beli, pesan_hb = validasi_angka_positif(harga_beli_raw, "Harga beli", min_val=0)
    if not valid_hb:
        print(f"[Peringatan] {pesan_hb}")
        return

    harga_jual_raw = input("Masukkan Harga Jual (Rp): ").strip()
    valid_hj, harga_jual, pesan_hj = validasi_angka_positif(harga_jual_raw, "Harga jual", min_val=0)
    if not valid_hj:
        print(f"[Peringatan] {pesan_hj}")
        return

    stok_raw = input("Masukkan Kuantitas Stok Awal: ").strip()
    valid_stok, stok_awal, pesan_stok = validasi_angka_positif(stok_raw, "Stok awal", min_val=0)
    if not valid_stok:
        print(f"[Peringatan] {pesan_stok}")
        return

    min_stok_raw = input("Masukkan Batas Minimum Stok Aman (default: 5): ").strip()
    if not min_stok_raw:
        min_stok = 5
    else:
        valid_min, min_stok, pesan_min = validasi_angka_positif(min_stok_raw, "Batas minimum stok", min_val=1)
        if not valid_min:
            print(f"[Peringatan] {pesan_min}")
            return

    sukses, pesan = tambah_barang_baru(
        daftar_barang,
        log_mutasi,
        hasil_kode,
        hasil_nama,
        hasil_kat,
        hasil_sat,
        harga_beli,
        harga_jual,
        stok_awal,
        min_stok,
    )
    if sukses:
        print(f"[Berhasil] {pesan}")
    else:
        print(f"[Gagal] {pesan}")


def menu_barang_masuk():
    print("\n--- TRANSAKSI BARANG MASUK (RESTOCK) ---")
    kode_input = input("Masukkan Kode Barang: ").strip()
    item = cari_barang_by_kode(kode_input, daftar_barang)
    if item is None:
        print(f"[Peringatan] Barang dengan kode '{kode_input.upper()}' tidak ditemukan.")
        return

    print(f"Produk Terpilih: {item['nama']} (Sisa stok saat ini: {item['stok']} {item['satuan']})")
    jumlah_raw = input("Masukkan Kuantitas Masuk: ").strip()
    valid_jml, jumlah, pesan_jml = validasi_angka_positif(jumlah_raw, "Jumlah barang masuk", min_val=1)
    if not valid_jml:
        print(f"[Peringatan] {pesan_jml}")
        return

    keterangan = input("Masukkan Keterangan (default: Pasokan Pemasok): ").strip()
    if not keterangan:
        keterangan = "Pasokan Pemasok"

    sukses, pesan = transaksi_barang_masuk(daftar_barang, log_mutasi, item["kode"], jumlah, keterangan)
    if sukses:
        print(f"[Berhasil] {pesan}")
    else:
        print(f"[Gagal] {pesan}")


def menu_barang_keluar():
    print("\n--- TRANSAKSI BARANG KELUAR (ANTI-STOK MINUS) ---")
    kode_input = input("Masukkan Kode Barang: ").strip()
    item = cari_barang_by_kode(kode_input, daftar_barang)
    if item is None:
        print(f"[Peringatan] Barang dengan kode '{kode_input.upper()}' tidak ditemukan.")
        return

    print(f"Produk Terpilih: {item['nama']} (Sisa stok saat ini: {item['stok']} {item['satuan']})")
    jumlah_raw = input("Masukkan Kuantitas Keluar: ").strip()
    valid_jml, jumlah, pesan_jml = validasi_angka_positif(jumlah_raw, "Jumlah barang keluar", min_val=1)
    if not valid_jml:
        print(f"[Peringatan] {pesan_jml}")
        return

    keterangan = input("Masukkan Keterangan Alasan Keluar (default: Penjualan Toko): ").strip()
    if not keterangan:
        keterangan = "Penjualan Toko"

    sukses, pesan = transaksi_barang_keluar(daftar_barang, log_mutasi, item["kode"], jumlah, keterangan)
    if sukses:
        print(f"[Berhasil] {pesan}")
    else:
        print(f"[Batal] {pesan}")


def menu_laporan_analisis():
    print("\n--- LAPORAN ANALISIS PERSEDIAAN (MATERI P07) ---")
    try:
        from laporan_pandas import tampilkan_laporan_pandas
        tampilkan_laporan_pandas(daftar_barang, log_mutasi)
        return
    except ImportError:
        pass

    ringkasan = ringkasan_inventaris(daftar_barang)
    print("Ringkasan Statistik Persediaan Gudang (Modul Pandas P7 menyusul):")
    print(f"- Total Jenis Produk (SKU)   : {ringkasan['total_sku']}")
    print(f"- Total Kuantitas Unit Fisik : {ringkasan['total_unit']}")
    print(f"- Estimasi Nilai Modal Aset  : {format_rupiah(ringkasan['total_aset'])}")
    print(f"- Jumlah Barang Status Kritis: {ringkasan['total_kritis']}")


def jalankan_menu_utama():
    cetak_banner_bawaan()

    while True:
        print("\nMENU OPERASIONAL STOKKU:")
        print("1. Lihat Daftar Stok Barang & Status Kritis")
        print("2. Tambah Data Barang Baru")
        print("3. Transaksi Barang Masuk (Restock)")
        print("4. Transaksi Barang Keluar (Anti-Stok Minus)")
        print("5. Lihat Riwayat Mutasi Arus Barang")
        print("6. Laporan Analisis Persediaan (P7)")
        print("7. Jalankan Skrip Uji Otomatis (7 Kasus Uji)")
        print("0. Keluar dari Program")

        pilihan = input("Pilih menu [0-7]: ").strip()

        if pilihan == "1":
            tampilkan_tabel_barang_bawaan()
        elif pilihan == "2":
            menu_tambah_barang()
        elif pilihan == "3":
            menu_barang_masuk()
        elif pilihan == "4":
            menu_barang_keluar()
        elif pilihan == "5":
            tampilkan_log_mutasi_bawaan()
        elif pilihan == "6":
            menu_laporan_analisis()
        elif pilihan == "7":
            from test_skenario import jalankan_semua_pengujian
            jalankan_semua_pengujian()
        elif pilihan == "0":
            print("\nTerima kasih. Program Stokku Desktop ditutup.")
            break
        else:
            print("[Peringatan] Pilihan tidak valid. Silakan masukkan angka 0 sampai 7.")


if __name__ == "__main__":
    jalankan_menu_utama()
