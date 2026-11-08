"""
Skrip Otomasi Pengujian 7 Kasus Uji (Test Runner)
PIC: YUKEN VELINO (15260767) - Kelompok 4 Dasar Pemrograman 15.1C.30
Target Evaluasi: Pertemuan 8 (UTS) - Dosen: Ali Mustopa, M.Kom (AOP)
"""

import sys
from data_store import daftar_barang, log_mutasi, reset_data
from engine_stok import (
    cek_status_stok,
    hitung_barang_kritis,
    hitung_total_aset_modal,
    hitung_total_kuantitas,
    ringkasan_inventaris,
    tambah_barang_baru,
    transaksi_barang_keluar,
    transaksi_barang_masuk,
)
from validasi import cari_barang_by_kode


def jalankan_semua_pengujian():
    reset_data()
    total_lulus = 0
    total_kasus = 7

    print("=" * 72)
    print(" PENGUJIAN OTOMATIS SISTEM STOKKU DESKTOP (FASE 1 - UTS P08)")
    print(" Mata Kuliah: Dasar Pemrograman (894) - Kelas 15.1C.30 UBSI")
    print(" Dosen Pengampu: Ali Mustopa, M.Kom (AOP)")
    print(" Test Runner & Backend Lead: YUKEN VELINO (15260767 / @Curzyori)")
    print("=" * 72)

    # -------------------------------------------------------------------------
    # TC-01: Inisialisasi Data Master & Saldo Awal
    # -------------------------------------------------------------------------
    print("\n[TC-01] Pengujian Inisialisasi Data Master & Log Mutasi Awal...")
    kondisi_tc1 = (
        len(daftar_barang) == 3
        and len(log_mutasi) == 3
        and cari_barang_by_kode("ATK01", daftar_barang) is not None
        and cari_barang_by_kode("ATK02", daftar_barang) is not None
        and cari_barang_by_kode("KRT01", daftar_barang) is not None
    )
    if kondisi_tc1:
        total_lulus += 1
        print("  Status: LULUS (3 data dummy master dan 3 log mutasi awal terpasang)")
    else:
        print("  Status: GAGAL (Inisialisasi data tidak sesuai spesifikasi)")

    # -------------------------------------------------------------------------
    # TC-02: Tambah Barang Valid & Proteksi Kode Duplikat
    # -------------------------------------------------------------------------
    print("\n[TC-02] Pengujian Penambahan Barang Baru & Proteksi Kode Duplikat...")
    sukses_tambah, _ = tambah_barang_baru(
        daftar_barang,
        log_mutasi,
        kode="ATK03",
        nama="Penghapus Joyko B40",
        kategori="ATK",
        satuan="Pcs",
        harga_beli=1500,
        harga_jual=2500,
        stok_awal=20,
        min_stok=5,
    )
    # Uji duplikasi kode (case-insensitive: "atk01" vs "ATK01")
    sukses_duplikat, pesan_duplikat = tambah_barang_baru(
        daftar_barang,
        log_mutasi,
        kode="atk01",
        nama="Buku Tulis Duplikat",
        kategori="ATK",
        satuan="Pcs",
        harga_beli=3000,
        harga_jual=4000,
        stok_awal=5,
        min_stok=2,
    )
    item_atk03 = cari_barang_by_kode("ATK03", daftar_barang)
    kondisi_tc2 = (
        sukses_tambah is True
        and item_atk03 is not None
        and item_atk03["stok"] == 20
        and sukses_duplikat is False
        and len(daftar_barang) == 4
    )
    if kondisi_tc2:
        total_lulus += 1
        print(f"  Status: LULUS (Barang baru tersimpan, kode kembar ditolak: '{pesan_duplikat}')")
    else:
        print("  Status: GAGAL (Validasi kode unik bermasalah)")

    # -------------------------------------------------------------------------
    # TC-03: Transaksi Barang Masuk (Restock)
    # -------------------------------------------------------------------------
    print("\n[TC-03] Pengujian Transaksi Barang Masuk (Restock)...")
    stok_sebelum_masuk = cari_barang_by_kode("ATK01", daftar_barang)["stok"]
    sukses_masuk, pesan_masuk = transaksi_barang_masuk(
        daftar_barang,
        log_mutasi,
        kode="ATK01",
        jumlah=10,
        keterangan="Pasokan Tambahan Pabrik",
    )
    item_atk01 = cari_barang_by_kode("ATK01", daftar_barang)
    kondisi_tc3 = (
        sukses_masuk is True
        and item_atk01["stok"] == (stok_sebelum_masuk + 10)
        and log_mutasi[-1][3] == "MASUK"
        and log_mutasi[-1][4] == 10
    )
    if kondisi_tc3:
        total_lulus += 1
        print(f"  Status: LULUS (Stok awal {stok_sebelum_masuk} -> akhir {item_atk01['stok']}, log masuk tercatat)")
    else:
        print("  Status: GAGAL (Transaksi barang masuk tidak berjalan semestinya)")

    # -------------------------------------------------------------------------
    # TC-04: Transaksi Barang Keluar Normal
    # -------------------------------------------------------------------------
    print("\n[TC-04] Pengujian Transaksi Barang Keluar Normal...")
    stok_sebelum_keluar = cari_barang_by_kode("ATK01", daftar_barang)["stok"]
    sukses_keluar, pesan_keluar = transaksi_barang_keluar(
        daftar_barang,
        log_mutasi,
        kode="ATK01",
        jumlah=5,
        keterangan="Penjualan Toko",
    )
    stok_sesudah_keluar = cari_barang_by_kode("ATK01", daftar_barang)["stok"]
    kondisi_tc4 = (
        sukses_keluar is True
        and stok_sesudah_keluar == (stok_sebelum_keluar - 5)
        and log_mutasi[-1][3] == "KELUAR"
        and log_mutasi[-1][4] == 5
    )
    if kondisi_tc4:
        total_lulus += 1
        print(f"  Status: LULUS (Stok awal {stok_sebelum_keluar} -> akhir {stok_sesudah_keluar}, log keluar tercatat)")
    else:
        print("  Status: GAGAL (Transaksi barang keluar normal bermasalah)")

    # -------------------------------------------------------------------------
    # TC-05: Proteksi Anti-Stok Minus
    # -------------------------------------------------------------------------
    print("\n[TC-05] Pengujian Validasi Mutlak Anti-Stok Minus...")
    item_atk02 = cari_barang_by_kode("ATK02", daftar_barang)
    stok_awal_atk02 = item_atk02["stok"]  # Bernilai 4
    jumlah_log_sebelum = len(log_mutasi)

    # Mencoba mengeluarkan 10 unit padahal stok hanya 4
    sukses_minus, pesan_minus = transaksi_barang_keluar(
        daftar_barang,
        log_mutasi,
        kode="ATK02",
        jumlah=10,
        keterangan="Penjualan Ekstrem Melebihi Stok",
    )
    stok_akhir_atk02 = cari_barang_by_kode("ATK02", daftar_barang)["stok"]
    jumlah_log_sesudah = len(log_mutasi)

    kondisi_tc5 = (
        sukses_minus is False
        and stok_akhir_atk02 == stok_awal_atk02  # Stok tidak boleh berkurang
        and stok_akhir_atk02 >= 0
        and jumlah_log_sesudah == jumlah_log_sebelum  # Log tidak mencatat transaksi batal
    )
    if kondisi_tc5:
        total_lulus += 1
        print(f"  Status: LULUS (Transaksi dibatalkan otomatis: '{pesan_minus}', stok utuh {stok_akhir_atk02})")
    else:
        print("  Status: GAGAL (Proteksi stok minus bobol)")

    # -------------------------------------------------------------------------
    # TC-06: Peringatan Dini Status Stok Kritis
    # -------------------------------------------------------------------------
    print("\n[TC-06] Pengujian Deteksi Status Stok Kritis (stok <= min_stok)...")
    status_atk02 = cek_status_stok(item_atk02["stok"], item_atk02["min_stok"])  # 4 <= 5 -> KRITIS
    item_krt01 = cari_barang_by_kode("KRT01", daftar_barang)
    status_krt01_awal = cek_status_stok(item_krt01["stok"], item_krt01["min_stok"])  # 10 > 3 -> AMAN

    # Kurangi stok KRT01 dari 10 menjadi 2 (sehingga <= min_stok 3)
    transaksi_barang_keluar(daftar_barang, log_mutasi, "KRT01", 8, "Penjualan Kertas")
    item_krt01_update = cari_barang_by_kode("KRT01", daftar_barang)
    status_krt01_akhir = cek_status_stok(item_krt01_update["stok"], item_krt01_update["min_stok"])

    kondisi_tc6 = (
        status_atk02 == "KRITIS"
        and status_krt01_awal == "AMAN"
        and status_krt01_akhir == "KRITIS"
        and hitung_barang_kritis(daftar_barang) >= 2
    )
    if kondisi_tc6:
        total_lulus += 1
        print(f"  Status: LULUS (ATK02: {status_atk02}, KRT01 transisi: {status_krt01_awal} -> {status_krt01_akhir})")
    else:
        print("  Status: GAGAL (Deteksi status kritis tidak akurat)")

    # -------------------------------------------------------------------------
    # TC-07: Perhitungan Total Unit Fisik & Akumulasi Aset Modal
    # -------------------------------------------------------------------------
    print("\n[TC-07] Pengujian Perhitungan Akurasi Total Unit & Nilai Modal Gudang...")
    # Hitung nilai ekspektasi secara mandiri
    unit_ekspektasi = sum(b["stok"] for b in daftar_barang)
    aset_ekspektasi = sum(b["stok"] * b["harga_beli"] for b in daftar_barang)

    unit_hitung = hitung_total_kuantitas(daftar_barang)
    aset_hitung = hitung_total_aset_modal(daftar_barang)
    ringkasan = ringkasan_inventaris(daftar_barang)

    kondisi_tc7 = (
        unit_hitung == unit_ekspektasi
        and aset_hitung == aset_ekspektasi
        and ringkasan["total_unit"] == unit_ekspektasi
        and ringkasan["total_aset"] == aset_ekspektasi
    )
    if kondisi_tc7:
        total_lulus += 1
        print(f"  Status: LULUS (Total Fisik: {unit_hitung} unit | Estimasi Modal: Rp {aset_hitung:,.0f})")
    else:
        print("  Status: GAGAL (Perhitungan akumulasi aset menyimpang)")

    # -------------------------------------------------------------------------
    # Ringkasan Hasil Pengujian
    # -------------------------------------------------------------------------
    print("\n" + "=" * 72)
    persentase = (total_lulus / total_kasus) * 100
    print(f" HASIL AKHIR: {total_lulus} dari {total_kasus} kasus uji LULUS ({persentase:.1f}%)")
    print("=" * 72)

    if total_lulus == total_kasus:
        print(" KESIMPULAN: Mesin Logika Stokku Desktop Fase 1 Siap untuk Penilaian UTS.")
        return 0
    else:
        print(" KESIMPULAN: Masih ada kasus uji yang gagal. Periksa kembali logika kode.")
        return 1


if __name__ == "__main__":
    kode_keluar = jalankan_semua_pengujian()
    sys.exit(kode_keluar)
