class MataKuliah:
    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama
        self.mahasiswa = []

    def tambah_mahasiswa(self, mhs):
        self.mahasiswa.append(mhs)

    def daftar_mahasiswa(self):
        return [m.nama for m in self.mahasiswa]

    def jumlah_mahasiswa(self):
        return len(self.mahasiswa)

class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama

# ==================================
# Bagian Contoh Penggunaan yang Diperbarui
# ==================================

## 1. Pembuatan Objek 📚🧑‍🎓

# Buat 2 Mata Kuliah
mk1 = MataKuliah("TI101", "Pemrograman Dasar")
mk2 = MataKuliah("MA102", "Kalkulus")

# Buat 3 Mahasiswa
m1 = Mahasiswa("23001", "Budi")
m2 = Mahasiswa("23002", "Siti")
m3 = Mahasiswa("23003", "Joko")

## 2. Pendaftaran Mahasiswa ke Mata Kuliah

# Daftarkan ke Mata Kuliah 1: Pemrograman Dasar (Budi, Siti, Joko)
mk1.tambah_mahasiswa(m1)
mk1.tambah_mahasiswa(m2)
mk1.tambah_mahasiswa(m3)

# Daftarkan ke Mata Kuliah 2: Kalkulus (Siti, Joko)
mk2.tambah_mahasiswa(m2)
mk2.tambah_mahasiswa(m3)


## 3. Menampilkan Hasil

print("====================================")
print(f"Mata Kuliah: {mk1.nama} ({mk1.kode})")
print(f"Jumlah Mahasiswa: {mk1.jumlah_mahasiswa()}")
print(f"Daftar Mahasiswa: {mk1.daftar_mahasiswa()}")

print("------------------------------------")
print(f"Mata Kuliah: {mk2.nama} ({mk2.kode})")
print(f"Jumlah Mahasiswa: {mk2.jumlah_mahasiswa()}")
print(f"Daftar Mahasiswa: {mk2.daftar_mahasiswa()}")
print("====================================")