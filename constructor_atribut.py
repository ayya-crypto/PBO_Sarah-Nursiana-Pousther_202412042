class Kendaraan:
    # Class attribute
    bahan_bakar = "Bensin"  # Contoh: Semua kendaraan menggunakan bensin

    # Constructor
    def __init__(self, merek, warna, tahun):
        # Instance attributes
        self.merek = merek
        self.warna = warna
        self.tahun = tahun

    def info_kendaraan(self):
        return f"Mobil {self.merek} {self.warna} ({self.tahun}) menggunakan {self.bahan_bakar}"

# Instansiasi object
mobil1 = Kendaraan("Toyota", "hitam", 2020)
mobil2 = Kendaraan("Honda", "putih", 2018)

# Output
print(mobil1.info_kendaraan())
print(mobil2.info_kendaraan())
print(f"Bahan bakar standar: {Kendaraan.bahan_bakar}")