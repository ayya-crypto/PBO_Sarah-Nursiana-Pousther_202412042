# Membuat class Pelanggan
class Pelanggan:
    def __init__(self, id_pelanggan, nama, email):
        self.id_pelanggan = id_pelanggan
        self.nama = nama
        self.email = email

# Membuat dictionary pelanggan (id sebagai key)
data_pelanggan = {
    "PL001": Pelanggan("PL001", "Hasan", "hasan@gmail.com"),
    "PL002": Pelanggan("PL002", "Ainun", "ainun@gmail.com"),
    "PL003": Pelanggan("PL003", "Sheila", "sheila@gmail.com")
}

# Fungsi untuk menambah pelanggan
def tambah_pelanggan(data_pelanggan, id_pelanggan, nama, email):
    if id_pelanggan in data_pelanggan:
        print("ID pelanggan sudah ada.")
    else:
        data_pelanggan[id_pelanggan] = Pelanggan(id_pelanggan, nama, email)
        print("Pelanggan berhasil ditambahkan.")

# Fungsi untuk menghapus pelanggan
def hapus_pelanggan(data_pelanggan, id_pelanggan):
    if id_pelanggan in data_pelanggan:
        del data_pelanggan[id_pelanggan]
        print("Pelanggan berhasil dihapus.")
    else:
        print("ID pelanggan tidak ditemukan.")

# Fungsi untuk mencari pelanggan
def cari_pelanggan(data_pelanggan, id_pelanggan):
    if id_pelanggan in data_pelanggan:
        return data_pelanggan[id_pelanggan]
    else:
        return None

# --- BAGIAN UNTUK MENGHASILKAN OUTPUT ---

# 1. Menampilkan Daftar Pelanggan Awal
print("=== Daftar Pelanggan ===")
for p in data_pelanggan.values():
    print("-" * 30)
    print(f"ID    : {p.id_pelanggan}")
    print(f"Nama  : {p.nama}")
    print(f"Email : {p.email}")
print("-" * 30)

# 2. Contoh Operasi
print("\n=== Contoh Operasi ===")

# Tambah pelanggan baru (PL004)
tambah_pelanggan(data_pelanggan, "PL004", "Zaila", "zaila@gmail.com")

# Cari pelanggan (PL002)
p_cari = cari_pelanggan(data_pelanggan, "PL002")
if p_cari:
    print(f"\nPelanggan ditemukan: {p_cari.nama} - {p_cari.email}")

# Hapus pelanggan (PL001)
hapus_pelanggan(data_pelanggan, "PL001")

# 3. Menampilkan Daftar Pelanggan Terbaru
print("\n=== Daftar Pelanggan Terbaru ===")
for p in data_pelanggan.values():
    print(f"{p.id_pelanggan} | {p.nama} | {p.email}")