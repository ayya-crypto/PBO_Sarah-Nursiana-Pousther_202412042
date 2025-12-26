# Berdasarkan image_258821.png dan permintaan sebelumnya
class Penulis:
    def __init__(self, nama):
        self.nama = nama

    def info_penulis(self):
        return f"Penulis: {self.nama}"

# Berdasarkan image_23be82.png (Composition)
class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        # Composition: Objek Penulis adalah atribut dari objek Buku
        self.penulis = penulis 

    def info_buku(self):
        # Memanggil metode dari objek Penulis yang merupakan bagian dari Buku
        return f"Judul Buku: {self.judul}\nOleh: {self.penulis.info_penulis()}"

# Instansiasi 
# 1. Buat objek Penulis (komponen)
penulis_a = Penulis("Andrea Hirata")

# 2. Buat objek Buku, memasukkan objek Penulis ke dalamnya
buku1 = Buku("Laskar Pelangi", penulis_a)

# 3. Cetak informasi
print(buku1.info_buku())