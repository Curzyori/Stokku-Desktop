import unittest
from io import StringIO
import sys

class TestDisplayCLI(unittest.TestCase):
    def setUp(self):
        self.held_output = StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.held_output

    def tearDown(self):
        sys.stdout = self.original_stdout

    def test_format_rupiah(self):
        from progress_p7.display_cli import format_rupiah
        self.assertEqual(format_rupiah(0), "Rp 0")
        self.assertEqual(format_rupiah(75000), "Rp 75.000")
        self.assertEqual(format_rupiah(1250000), "Rp 1.250.000")

    def test_status_stok(self):
        from progress_p7.display_cli import status_stok
        self.assertEqual(status_stok(0, 5), "[KRITIS]")
        self.assertEqual(status_stok(3, 5), "[KRITIS]")
        self.assertEqual(status_stok(5, 5), "[KRITIS]")
        self.assertEqual(status_stok(6, 5), "[AMAN]")
        self.assertEqual(status_stok(100, 5), "[AMAN]")

    def test_tampilkan_banner(self):
        from progress_p7.display_cli import tampilkan_banner
        tampilkan_banner()
        output = self.held_output.getvalue()
        self.assertIn("STOKKU DESKTOP", output)
        self.assertIn("Manajemen Persediaan Gudang UMKM", output)

    def test_tampilkan_ringkasan(self):
        from progress_p7.display_cli import tampilkan_ringkasan
        tampilkan_ringkasan(total_sku=3, total_unit=45, total_aset=4500000, total_kritis=1)
        output = self.held_output.getvalue()
        self.assertIn("RINGKASAN STATUS GUDANG", output)
        self.assertIn("Total Jenis (SKU) : 3", output)
        self.assertIn("Total Unit Fisik  : 45", output)
        self.assertIn("Rp 4.500.000", output)
        self.assertIn("1 Produk", output)

    def test_tabel_barang_kosong(self):
        from progress_p7.display_cli import tampilkan_tabel_barang
        tampilkan_tabel_barang([])
        output = self.held_output.getvalue()
        self.assertIn("Belum ada data barang di inventaris gudang.", output)

    def test_tabel_barang_berisi(self):
        from progress_p7.display_cli import tampilkan_tabel_barang
        sample_data = [
            {
                "kode_barang": "BRG001",
                "nama_barang": "Beras Rojolele 5kg",
                "kategori": "Sembako",
                "satuan": "Karung",
                "harga_beli": 65000,
                "harga_jual": 75000,
                "stok": 20,
                "min_stok": 5
            },
            {
                "kode_barang": "BRG002",
                "nama_barang": "Minyak Goreng 2L",
                "kategori": "Sembako",
                "satuan": "Pouch",
                "harga_beli": 28000,
                "harga_jual": 33000,
                "stok": 3,
                "min_stok": 5
            }
        ]
        tampilkan_tabel_barang(sample_data)
        output = self.held_output.getvalue()
        self.assertIn("BRG001", output)
        self.assertIn("Beras Rojolele 5kg", output)
        self.assertIn("Rp 75.000", output)
        self.assertIn("[AMAN]", output)
        self.assertIn("BRG002", output)
        self.assertIn("[KRITIS]", output)

    def test_tabel_riwayat_mutasi(self):
        from progress_p7.display_cli import tampilkan_tabel_riwayat
        tampilkan_tabel_riwayat([])
        output_kosong = self.held_output.getvalue()
        self.assertIn("Belum ada riwayat transaksi mutasi.", output_kosong)

        self.held_output.truncate(0)
        self.held_output.seek(0)

        sample_mutasi = [
            {
                "tanggal": "2026-11-08 10:00:00",
                "kode_barang": "BRG001",
                "nama_barang": "Beras Rojolele 5kg",
                "jenis_transaksi": "MASUK",
                "jumlah": 10,
                "stok_sebelum": 10,
                "stok_sesudah": 20,
                "keterangan": "Pasokan Agen Utama"
            }
        ]
        tampilkan_tabel_riwayat(sample_mutasi)
        output_isi = self.held_output.getvalue()
        self.assertIn("BRG001", output_isi)
        self.assertIn("MASUK", output_isi)
        self.assertIn("+10", output_isi)
        self.assertIn("Pasokan Agen Utama", output_isi)

    def test_notifikasi(self):
        from progress_p7.display_cli import tampilkan_pesan_sukses, tampilkan_pesan_error
        tampilkan_pesan_sukses("Data tersimpan")
        tampilkan_pesan_error("Input tidak valid")
        output = self.held_output.getvalue()
        self.assertIn("[SUKSES] Data tersimpan", output)
        self.assertIn("[ERROR] Input tidak valid", output)

if __name__ == "__main__":
    unittest.main()
