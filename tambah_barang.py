class ManajerInventori:
    """
    Class untuk mengelola inventori barang.
    Setiap barang disimpan sebagai pasangan (nama_barang: jumlah).
    """
    def __init__(self):
        # Instance attribute untuk menyimpan inventori
        self.inventori = {}

    def tambah_barang(self, nama_barang, jumlah):
        """Menambahkan jumlah barang ke inventori."""
        if jumlah > 0:
            # Gunakan .get() untuk menangani kasus barang baru
            self.inventori[nama_barang] = self.inventori.get(nama_barang, 0) + jumlah
            print(f"Berhasil menambahkan {jumlah} unit {nama_barang}.")
        else:
            print("Jumlah barang harus positif.")

    def hapus_barang(self, nama_barang, jumlah):
        """Mengurangi jumlah barang dari inventori."""
        if nama_barang not in self.inventori:
            print(f"Barang '{nama_barang}' tidak ada dalam inventori.")
            return

        if jumlah > 0:
            if self.inventori[nama_barang] >= jumlah:
                self.inventori[nama_barang] -= jumlah
                print(f"Berhasil mengurangi {jumlah} unit {nama_barang}.")
                
                # Hapus item jika jumlahnya menjadi nol
                if self.inventori[nama_barang] == 0:
                    del self.inventori[nama_barang]
                    print(f"Barang '{nama_barang}' habis dan dihapus dari inventori.")
            else:
                print(f"Saldo barang '{nama_barang}' tidak mencukupi. Tersisa: {self.inventori[nama_barang]}.")
        else:
            print("Jumlah barang yang dihapus harus positif.")


    def lihat_inventori(self):
        """Menampilkan semua barang dan jumlahnya di inventori."""
        if not self.inventori:
            print("Inventori kosong.")
            return

        print("\n--- Daftar Inventori ---")
        for barang, jumlah in self.inventori.items():
            print(f"- {barang}: {jumlah} unit")
        print("------------------------")

# --- Contoh Penggunaan (Testing) ---

# 1. Buat objek ManajerInventori
manajer = ManajerInventori()

# 2. Tambah barang
manajer.tambah_barang("Laptop", 10)
manajer.tambah_barang("Mouse", 50)
manajer.tambah_barang("Laptop", 5) # Tambah lagi

# 3. Lihat inventori
manajer.lihat_inventori()

# 4. Hapus barang
manajer.hapus_barang("Mouse", 20)
manajer.hapus_barang("Monitor", 1) # Barang tidak ada
manajer.hapus_barang("Laptop", 15) # Hapus yang jumlahnya pas

# 5. Lihat inventori setelah perubahan
manajer.lihat_inventori()