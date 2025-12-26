class ManajerInventori:
    """
    Class untuk mengelola inventori barang.
    Setiap barang disimpan sebagai pasangan (nama_barang: jumlah).
    """
    def __init__(self):
        # Instance attribute: menggunakan dictionary untuk menyimpan inventori {nama_barang: jumlah}
        self.inventori = {}

    def tambah_barang(self, nama_barang, jumlah):
        """
        Method untuk MENAMBAH jumlah barang ke inventori.
        Jika barang sudah ada, stoknya diperbarui. Jika belum, barang ditambahkan.
        """
        if jumlah > 0:
            # Menggunakan .get() untuk mendapatkan jumlah stok saat ini (atau 0 jika barang baru)
            self.inventori[nama_barang] = self.inventori.get(nama_barang, 0) + jumlah
            print(f"Berhasil menambahkan {jumlah} unit {nama_barang}. Stok saat ini: {self.inventori[nama_barang]}")
        else:
            print("Jumlah barang yang ditambahkan harus positif.")

    def hapus_barang(self, nama_barang, jumlah):
        """
        Method untuk MENGURANGI jumlah barang (mengambil/menjual) dari inventori.
        Melakukan pengecekan ketersediaan stok.
        """
        if nama_barang not in self.inventori:
            print(f"Barang '{nama_barang}' tidak ada dalam inventori.")
            return

        if jumlah > 0:
            stok_saat_ini = self.inventori[nama_barang]
            
            if stok_saat_ini >= jumlah:
                self.inventori[nama_barang] -= jumlah
                print(f"Berhasil mengurangi {jumlah} unit {nama_barang}. Stok tersisa: {self.inventori[nama_barang]}")
                
                # Opsional: Hapus item dari dictionary jika stoknya menjadi nol
                if self.inventori[nama_barang] == 0:
                    del self.inventori[nama_barang]
                    print(f"Barang '{nama_barang}' habis dan dihapus dari inventori.")
            else:
                print(f"Gagal mengurangi. Stok '{nama_barang}' tidak mencukupi. Tersedia: {stok_saat_ini}.")
        else:
            print("Jumlah barang yang dihapus harus positif.")


    def lihat_inventori(self):
        """Menampilkan semua barang dan jumlahnya di inventori."""
        if not self.inventori:
            print("\n Inventori kosong.")
            return

        print("\n--- Daftar Inventori ---")
        for barang, jumlah in self.inventori.items():
            print(f"- {barang}: {jumlah} unit")
        print("------------------------")

# --- Contoh Penggunaan dan Testing ---
manajer = ManajerInventori()

print("--- TESTING PENAMBAHAN ---")
manajer.tambah_barang("Monitor 24 inch", 10)
manajer.tambah_barang("Keyboard Mekanik", 5)
manajer.tambah_barang("Monitor 24 inch", 5) # Penambahan stok yang sudah ada
manajer.lihat_inventori()

print("\n--- TESTING PENGURANGAN ---")
manajer.hapus_barang("Keyboard Mekanik", 2) # Pengurangan berhasil
manajer.hapus_barang("Monitor 24 inch", 15) # Pengurangan yang menghabiskan stok
manajer.hapus_barang("Mouse Wireless", 1) # Barang tidak ada
manajer.hapus_barang("Monitor 24 inch", 1) # Stok tidak mencukupi (sudah habis)

manajer.lihat_inventori()