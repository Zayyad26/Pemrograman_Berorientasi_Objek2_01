class Komik:

 def __init__(self, judul, penulis):
    self.judul = judul
    self.penulis = penulis
 
 def info(self):
    print(f"Judul : {self.judul}\n Penulis : {self.penulis}")
 
komikA = Komik("DragonBall", "Akira Toriyama")
komikA.info()
