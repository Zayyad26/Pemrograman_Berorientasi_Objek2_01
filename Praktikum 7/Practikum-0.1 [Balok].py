class Balok:
    def __init__(self, p, l, t):
        self.p = p
        self.l = l
        self.t = t

    def volume(self):
        return self.p * self.l * self.t

    def luas_permukaan(self):
        return 2 * (self.p * self.l + self.p * self.t + self.l * self.t)

    def __str__(self):
        return "Balok dengan panjang {}, lebar {}, dan tinggi {}".format(self.p, self.l, self.t)

balok = Balok(6, 4, 3)
print("{} memiliki volume {}".format(balok, balok.volume()))
print("{} memiliki luas permukaan {}".format(balok, balok.luas_permukaan()))
