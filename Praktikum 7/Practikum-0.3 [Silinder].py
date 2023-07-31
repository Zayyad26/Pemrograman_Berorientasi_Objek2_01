import math

class Silinder:
    def __init__(self, r, t):
        self.r = r
        self.t = t

    def volume(self):
        return math.pi * self.r ** 2 * self.t

    def luas_permukaan(self):
        return 2 * math.pi * self.r * (self.r + self.t)

    def __str__(self):
        return "Silinder dengan jari-jari {} dan tinggi {}".format(self.r, self.t)

silinder = Silinder(5, 10)
print("{} memiliki volume {}".format(silinder, silinder.volume()))
print("{} memiliki luas permukaan {}".format(silinder, silinder.luas_permukaan()))
