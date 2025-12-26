class Mahasiswa:
    universitas = "STITEK Bontang"

    def __init__(self, nama, nim, jurusan, ipk=0.0):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = float(ipk)

    def perkenalan_diri(self):
        print(f"Nama: {self.nama}, NIM: {self.nim}")
        print(f"Jurusan: {self.jurusan}, Universitas: {Mahasiswa.universitas}")
        print(f"IPK: {self.ipk:.2f}")

    def update_ipk(self, ipk_baru):
        self.ipk = float(ipk_baru)
        print(f"IPK diperbarui menjadi {self.ipk:.2f}")

    def predikat_kelulusan(self):
        if self.ipk >= 3.5:
            return "Cumlaude"
        elif self.ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            return "Memuaskan"
        elif self.ipk >= 2.0:
            return "Lulus"
        return "Belum Lulus"


# Demonstrasi
m1 = Mahasiswa("Sarah Nursiana Pousther", "202412050", "Teknik Informatika", 3.77)
m2 = Mahasiswa("Naila Agustina", "202410265", "Sistem Informasi", 3.65)
m3 = Mahasiswa("Nur islamia", "202410277", "Teknik Informatika", 3.58)

m2.update_ipk(3.20)

for m in (m1, m2, m3):
    print("\n--- Data Mahasiswa ---")
    m.perkenalan_diri()
    print("Predikat:", m.predikat_kelulusan())
