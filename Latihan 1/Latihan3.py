class Motor:

 def __init__(self, merk, warna):
    self.merk = merk
    self.warna = warna
 
 def info(self):
    print(f"Motor {self.merk} berwarna {self.warna}")
 
motorA = Motor("Yamaha", "Biru")
motorA.info()
