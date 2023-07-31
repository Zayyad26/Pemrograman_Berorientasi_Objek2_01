import math

class Bola:
    def __init__(self, r):
        self.r = r

    def volume(self):
        return 4 / 3 * math.pi * self.r ** 3

    def luas_permukaan(self):
        return 4 * math.pi * self.r ** 2

    def __str__(self):
        return "Bola dengan jari-jari {}".format(self.r)

bola = Bola(5)
print("{} memiliki volume {}".format(bola, bola.volume()))
print("{} memiliki luas permukaan {}".format(bola, bola.luas_permukaan()))
