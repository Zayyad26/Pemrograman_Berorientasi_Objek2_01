class Kendaraan:
    def __init__(self, nama):
        self.nama = nama

    def info(self):
        print("Ini adalah kendaraan:", self.nama)

class Mobil(Kendaraan):
    def __init__(self, nama, merk):
        super().__init__(nama)
        self.merk = merk

    def info(self):
        print("Ini adalah mobil:", self.nama, "merk", self.merk)

class Motor(Kendaraan):
    def __init__(self, nama, merk):
        super().__init__(nama)
        self.merk = merk

    def info(self):
        print("Ini adalah motor:", self.nama, "merk", self.merk)

kendaraan = Kendaraan("Roda Empat dan Roda Dua")
kendaraan.info()

mobil = Mobil("Mobil", "Toyota")
mobil.info()

motor = Motor("Motor", "Honda")
motor.info()
