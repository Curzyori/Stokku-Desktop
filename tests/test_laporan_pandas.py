"""
Unit Test Modul Laporan Pandas P7 (progress_p7/laporan_pandas.py)
PIC: RENKYNA AFTANIA NASUTION (15260847)
"""

import unittest
from progress_p7.laporan_pandas import (
    format_rupiah,
    cek_ketersediaan_pandas,
    buat_dataframe_barang,
    buat_dataframe_mutasi,
    rekapitulasi_kategori,
    filter_mutasi_berdasarkan_jenis,
    ringkasan_statistik_deskriptif,
)

DUMMY_BARANG = [
    {
        "kode": "ATK01",
        "nama": "Buku Tulis Kiky 38 Lembar",
        "kategori": "ATK",
        "satuan": "Pcs",
        "harga_beli": 3500,
        "harga_jual": 5000,
        "stok": 15,
        "min_stok": 5,
    },
    {
        "kode": "ATK02",
        "nama": "Pulpen Faster C600 Hitam",
        "kategori": "ATK",
        "satuan": "Pcs",
        "harga_beli": 2500,
        "harga_jual": 3500,
        "stok": 4,
        "min_stok": 5,
    },
    {
        "kode": "KRT01",
        "nama": "Kertas HVS Sinar Dunia A4 75gr",
        "kategori": "Kertas",
        "satuan": "Rim",
        "harga_beli": 42000,
        "harga_jual": 48000,
        "stok": 10,
        "min_stok": 3,
    },
]

DUMMY_MUTASI = [
    ("2026-11-11 10:00:00", "ATK01", "Buku Tulis Kiky 38 Lembar", "MASUK", 15, 0, 15, "Saldo Awal"),
    ("2026-11-11 10:05:00", "ATK02", "Pulpen Faster C600 Hitam", "MASUK", 4, 0, 4, "Saldo Awal"),
    ("2026-11-11 10:10:00", "KRT01", "Kertas HVS Sinar Dunia A4 75gr", "MASUK", 10, 0, 10, "Saldo Awal"),
    ("2026-11-11 10:30:00", "ATK01", "Buku Tulis Kiky 38 Lembar", "KELUAR", 3, 15, 12, "Penjualan Toko"),
]


class TestLaporanPandas(unittest.TestCase):
    def test_format_rupiah(self):
        self.assertEqual(format_rupiah(0), "Rp 0")
        self.assertEqual(format_rupiah(3500), "Rp 3.500")
        self.assertEqual(format_rupiah(420000), "Rp 420.000")
        self.assertEqual(format_rupiah(-5000), "-Rp 5.000")
        self.assertEqual(format_rupiah("tidak-valid"), "Rp 0")

    def test_buat_dataframe_barang(self):
        if not cek_ketersediaan_pandas():
            self.skipTest("Pandas tidak terpasang di sistem.")

        df = buat_dataframe_barang(DUMMY_BARANG)
        self.assertIsNotNone(df)
        self.assertEqual(len(df), 3)
        self.assertIn("Nilai Modal", df.columns)
        self.assertIn("Estimasi Omzet", df.columns)
        self.assertIn("Potensi Laba", df.columns)
        self.assertIn("Status", df.columns)

        # Cek baris 1 (ATK01: stok 15, harga_beli 3500 -> modal 52500, min_stok 5 -> AMAN)
        row1 = df[df["Kode"] == "ATK01"].iloc[0]
        self.assertEqual(row1["Nilai Modal"], 15 * 3500)
        self.assertEqual(row1["Status"], "AMAN")

        # Cek baris 2 (ATK02: stok 4, min_stok 5 -> KRITIS)
        row2 = df[df["Kode"] == "ATK02"].iloc[0]
        self.assertEqual(row2["Status"], "KRITIS")

    def test_buat_dataframe_mutasi(self):
        if not cek_ketersediaan_pandas():
            self.skipTest("Pandas tidak terpasang di sistem.")

        df_mutasi = buat_dataframe_mutasi(DUMMY_MUTASI)
        self.assertIsNotNone(df_mutasi)
        self.assertEqual(len(df_mutasi), 4)
        self.assertIn("Jenis", df_mutasi.columns)
        self.assertIn("Keterangan", df_mutasi.columns)

    def test_rekapitulasi_kategori(self):
        if not cek_ketersediaan_pandas():
            self.skipTest("Pandas tidak terpasang di sistem.")

        df = buat_dataframe_barang(DUMMY_BARANG)
        rekap = rekapitulasi_kategori(df)
        self.assertIsNotNone(rekap)
        self.assertEqual(len(rekap), 2)  # ATK dan Kertas

        rekap_atk = rekap[rekap["Kategori"] == "ATK"].iloc[0]
        self.assertEqual(rekap_atk["Total_SKU"], 2)
        self.assertEqual(rekap_atk["Total_Unit"], 19)

    def test_filter_mutasi(self):
        if not cek_ketersediaan_pandas():
            self.skipTest("Pandas tidak terpasang di sistem.")

        df_mutasi = buat_dataframe_mutasi(DUMMY_MUTASI)
        df_masuk = filter_mutasi_berdasarkan_jenis(df_mutasi, "MASUK")
        df_keluar = filter_mutasi_berdasarkan_jenis(df_mutasi, "KELUAR")

        self.assertEqual(len(df_masuk), 3)
        self.assertEqual(len(df_keluar), 1)

    def test_ringkasan_statistik_deskriptif(self):
        if not cek_ketersediaan_pandas():
            self.skipTest("Pandas tidak terpasang di sistem.")

        df = buat_dataframe_barang(DUMMY_BARANG)
        stats = ringkasan_statistik_deskriptif(df)

        self.assertEqual(stats["total_sku"], 3)
        self.assertEqual(stats["total_unit"], 29)
        # Total modal = (15*3500) + (4*2500) + (10*42000) = 52500 + 10000 + 420000 = 482500
        self.assertEqual(stats["total_modal"], 482500)
        self.assertEqual(stats["jumlah_kritis"], 1)


if __name__ == "__main__":
    unittest.main()

