class ProgramStudi:
    # PERBAIKAN: Mengganti _init_ menjadi __init__
    def __init__(self, kode, ketua):
        self.kode = kode  # Public (dapat diakses/diubah langsung)
        self._ketua = ketua  # Protected (konvensi: diawali satu underscore)
        self.__anggaran = 500000000  # Private (name mangling: diawali dua underscore)

    # Getter protected
    def get_ketua(self):
        return self._ketua

    # Setter protected (Mengontrol perubahan nilai)
    def set_ketua(self, nama_baru):
        if not nama_baru:
            raise ValueError("Nama ketua tidak boleh kosong.")
        self._ketua = nama_baru

    # Getter private
    def get_anggaran(self):
        return self.__anggaran

    # Setter private (Mengontrol perubahan nilai)
    def set_anggaran(self, nilai):
        if nilai < 0:
            raise ValueError("Anggaran tidak boleh negatif.")
        self.__anggaran = nilai

    # Method untuk memodifikasi atribut private secara aman
    def kurangi_anggaran(self, jumlah):
        if jumlah < 0:
            raise ValueError("Jumlah harus positif.")
        if jumlah > self.__anggaran:
            raise ValueError("Anggaran tidak mencukupi.")
        self.__anggaran -= jumlah
        return self.__anggaran


# Contoh penggunaan
# PERBAIKAN: Mengganti _name_ menjadi __name__
if __name__ == "__main__":
    ps = ProgramStudi("TI", "Pak Wayan")

    print(f"--- Data Awal Program Studi {ps.kode} ---")
    print("Kode (Public):", ps.kode)
    # Akses Protected dan Private dilakukan melalui method Getter
    print("Ketua Prodi (Protected):", ps.get_ketua())
    print("Anggaran (Private):", f"Rp{ps.get_anggaran():,}".replace(",", "."))
    print("-" * 35)

    # 1. Mengubah Ketua (menggunakan Setter)
    ps.set_ketua("Bu Diah")
    print("Ketua Prodi diubah menjadi:", ps.get_ketua())

    # 2. Menggunakan method kontrol Anggaran
    ps.kurangi_anggaran(100000000)
    print("Anggaran dikurangi 100 Juta.")
    print("Anggaran Tersisa:", f"Rp{ps.get_anggaran():,}".replace(",", "."))