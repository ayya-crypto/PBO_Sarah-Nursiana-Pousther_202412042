class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def info(self):
        return f"Person: {self.nama} ({self.umur} tahun)"

class Mahasiswa(Person):
    def __init__(self, nama, umur, nim):
        # Memanggil konstruktor class induk (Person)
        super().__init__(nama, umur)
        # Menambahkan atribut baru
        self.nim = nim

    def info(self):
        # Perbaikan di sini: Memastikan kurung kurawal digunakan untuk semua variabel 
        # dan format output lebih jelas.
        return f"Mahasiswa: {self.nama}, NIM {self.nim} ({self.umur} tahun)"

# Instansiasi
p = Person("Karel", 30)
m = Mahasiswa("Riana", 20, "202412076")

print(p.info())
print(m.info())