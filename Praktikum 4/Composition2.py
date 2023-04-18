class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.kelompok_kkm = None

    def bergabung_kelompok(self, kelompok):
        self.kelompok_kkm = kelompok
        kelompok.tambah_anggota(self)

    def tampilkan_kelompok(self):
        if self.kelompok_kkm:
            print(f"{self.nama} tergabung dalam kelompok KKM {self.kelompok_kkm.nama}.")
        else:
            print(f"{self.nama} belum bergabung dalam kelompok KKM.")

class KelompokKKM:
    def __init__(self, nama):
        self.nama = nama
        self.anggota = []

    def tambah_anggota(self, mhs):
        self.anggota.append(mhs)

    def tampilkan_anggota(self):
        print(f"Anggota Kelompok KKM {self.nama}:")
        for mhs in self.anggota:
            print(mhs.nama)
        

mhs1 = Mahasiswa("Ahmad", "12345")
mhs2 = Mahasiswa("Budi", "67890")

kelompok1 = KelompokKKM("Kelompok 1")

mhs1.bergabung_kelompok(kelompok1)
mhs2.bergabung_kelompok(kelompok1)

mhs1.tampilkan_kelompok()
mhs2.tampilkan_kelompok()

kelompok1.tampilkan_anggota()
