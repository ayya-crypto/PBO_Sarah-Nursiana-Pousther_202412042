import math

class Bentuk:
    def __init__(self):
        # Tambahkan __init__ jika kelas ini akan diinisialisasi
        pass
        
    def luas(self):
        return 0

class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi

class Lingkaran(Bentuk):
    def __init__(self, r):
        self.r = r

    def luas(self):
        # Pastikan menggunakan math.pi
        return math.pi * self.r * self.r

# Demonstrasi Polymorphism (Perbaikan pada instansiasi)
bentuk_list = [
    Bentuk(),
    Persegi(4),    # Instansiasi yang benar
    Lingkaran(7)   # Instansiasi yang benar
]

for b in bentuk_list:
    # Menggunakan f-string untuk output yang rapi
    print(f"{b.__class__.__name__} -> luas = {b.luas():.2f}")