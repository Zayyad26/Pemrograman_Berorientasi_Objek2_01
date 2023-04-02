class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar

    def luas_param(self, panjang):
        return panjang * self.lebar

    def luas_params(self, panjang, lebar):
        return panjang * lebar

persegi_panjang = PersegiPanjang(4, 5)

# Memanggil metode luas() tanpa parameter
print("Luas persegi panjang: ", persegi_panjang.luas())

# Memanggil metode luas() dengan 1 parameter
print("Luas persegi panjang dengan panjang 6: ", persegi_panjang.luas_param(6))

# Memanggil metode luas() dengan 2 parameter
print("Luas persegi panjang dengan panjang 6 dan lebar 8: ", persegi_panjang.luas_params(6, 8))
