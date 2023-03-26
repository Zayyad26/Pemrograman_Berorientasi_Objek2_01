class Siswa:

 def __init__(self, nama, nis):
    self.nama = nama
    self.nis = nis
 
 def info(self):
    print(f"Nama : {self.nama}\n Nis :  {self.nis}")
 
siswaB = Siswa("Yanto", "201785431")
siswaB.info()
