class Persegi:

 def __init__(self, panjang, lebar):
    self.panjang = panjang
    self.lebar = lebar
 
 def luas(self):
    return (self.panjang * self.lebar)
 
persegiA = Persegi(7, 5)
print(f"Luas Persegi : {persegiA.luas()}")
