class Penulis:
    def __init__(self, nama):
        self.nama = nama
        self.komik = []

    def tambah_komik(self, judul, tahun):
        komik = Komik(judul, tahun, self)
        self.komik.append(komik)
        return komik

    def tampilkan_komik(self):
        print(f"Daftar komik yang ditulis oleh {self.nama}:")
        for komik in self.komik:
            print(komik.judul)

class Komik:
    def __init__(self, judul, tahun, penulis):
        self.judul = judul
        self.tahun = tahun
        self.penulis = penulis

    def tampilkan_penulis(self):
        print(f"{self.judul} ditulis oleh {self.penulis.nama}.")

penulis1 = Penulis("Gempita")

komik1 = penulis1.tambah_komik("Si Nopal", 2022)
komik2 = penulis1.tambah_komik("Pak Dukun", 2023)

penulis1.tampilkan_komik()
komik1.tampilkan_penulis()
komik2.tampilkan_penulis()
        
