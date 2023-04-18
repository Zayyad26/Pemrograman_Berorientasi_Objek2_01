class Penulis:
    def __init__(self, nama):
        self.nama = nama
        self.buku = []

    def tambah_buku(self, judul):
        buku = Buku(judul, self)
        self.buku.append(buku)
        return buku

    def tampilkan_buku(self):
        print(f"Daftar buku yang ditulis oleh {self.nama}:")
        for buku in self.buku:
            print(buku.judul)

class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis

    def tampilkan_penulis(self):
        print(f"{self.judul} ditulis oleh {self.penulis.nama}.")

penulis1 = Penulis("Agatha Christie")

buku1 = penulis1.tambah_buku("Murder on the Orient Express")
buku2 = penulis1.tambah_buku("And Then There Were None")

penulis1.tampilkan_buku()
buku1.tampilkan_penulis()
buku2.tampilkan_penulis()
