class Dosen:
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn

    def perkenalan(self):
        return f"Halo, saya {self.nama} dengan NIDN {self.nidn}"

# Pembuatan object
dosen1 = Dosen("Abadi Nugroho", "12345")
dosen2 = Dosen("Rianindya Chandra", "67890")

print(dosen1.perkenalan())
print(dosen2.perkenalan())