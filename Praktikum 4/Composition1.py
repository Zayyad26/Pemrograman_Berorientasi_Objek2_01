class Peneliti:
    def __init__(self, nama, bidang):
        self.nama = nama
        self.bidang = bidang
        self.jurnal = None

    def buat_jurnal(self, judul, tahun):
        self.jurnal = Jurnal(judul, tahun)

    def tampilkan_jurnal(self):
        if self.jurnal:
            print(f"{self.nama} telah menerbitkan jurnal \"{self.jurnal.judul}\" pada tahun {self.jurnal.tahun}.")
        else:
            print(f"{self.nama} belum menerbitkan jurnal.")

class Jurnal:
    def __init__(self, judul, tahun):
        self.judul = judul
        self.tahun = tahun

# membuat objek peneliti
peneliti1 = Peneliti("Ahmad", "Fisika")

# membuat jurnal untuk peneliti1
peneliti1.buat_jurnal("Pengaruh Temperatur Terhadap Kepadatan Air", 2023)

# menampilkan informasi jurnal peneliti1
peneliti1.tampilkan_jurnal()

# membuat objek peneliti lainnya
peneliti2 = Peneliti("Budi", "Biologi")

# mencoba menampilkan informasi jurnal peneliti2 (belum ada jurnal yang dibuat)
peneliti2.tampilkan_jurnal()
