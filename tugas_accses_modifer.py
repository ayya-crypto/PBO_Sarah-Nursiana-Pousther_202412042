class Mahasiswa:
    # Magic method untuk inisialisasi objek
    def __init__(self, nim, nama, semester, ipk):
        # Public Attributes: Dapat diakses dan diubah langsung
        self.nim = nim
        self.nama = nama
        
        # Protected Attribute: Konvensi diawali satu underscore (_)
        self._semester = semester
        
        # Private Attribute: Name Mangling diawali dua underscore (__)
        self.__ipk = ipk  

    # --- Methods untuk Protected Attribute (_semester) ---
    
    # Getter protected
    def get_semester(self):
        return self._semester

    # Setter protected (dengan validasi sederhana)
    def set_semester(self, semester_baru):
        if semester_baru < 1:
            raise ValueError("Semester harus minimal 1.")
        self._semester = semester_baru

    # --- Methods untuk Private Attribute (__ipk) ---
    
    # Getter private
    def get_ipk(self):
        # Memastikan IPK ditampilkan dengan format dua angka di belakang koma
        return f"{self.__ipk:.2f}"

    # Setter private (dengan validasi)
    def set_ipk(self, nilai_ipk):
        if not (0.0 <= nilai_ipk <= 4.0):
            raise ValueError("Nilai IPK harus berada di antara 0.0 dan 4.0.")
        self.__ipk = nilai_ipk
        
    # Method untuk demonstrasi perhitungan dengan atribut private
    def cek_status_kelulusan(self):
        if self.__ipk >= 3.5:
            return "Cumlaude"
        elif self.__ipk >= 2.75:
            return "Sangat Memuaskan"
        else:
            return "Memuaskan"


# Contoh Penggunaan dan Demonstrasi Hak Akses
# ----------------------------------------------
if __name__ == "__main__":
    mhs = Mahasiswa("12345678", "Ali Mustofa", 3, 3.85)
    
    print("--- Data Awal Mahasiswa ---")
    print(f"NIM (Public): {mhs.nim}")
    print(f"Nama (Public): {mhs.nama}")
    print(f"Semester (Protected via Getter): {mhs.get_semester()}")
    print(f"IPK (Private via Getter): {mhs.get_ipk()}")
    print("-" * 30)

    # 1. Mengakses/Mengubah Public (Langsung)
    mhs.nama = "Ali Mustofa (Revisi)"
    print(f"Nama diubah langsung: {mhs.nama}")

    # 2. Mengubah Protected (Disarankan via Setter)
    mhs.set_semester(4)
    print(f"Semester diubah via Setter: {mhs.get_semester()}")

    # 3. Mengubah Private (Wajib via Setter)
    mhs.set_ipk(3.92)
    print(f"IPK diubah via Setter: {mhs.get_ipk()}")
    print(f"Status Kelulusan Prediksi: {mhs.cek_status_kelulusan()}")
    
    # Mencoba mengakses IPK Private secara langsung (akan gagal)
    try:
        print(f"\nMencoba akses langsung IPK: {mhs.__ipk}")
    except AttributeError as e:
        print(f"\nMencoba akses langsung IPK: GAGAL. Error: {e}")