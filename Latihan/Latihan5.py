class KeretaApi:

 def __init__(self, kereta, tujuan):
    self.kereta = kereta
    self.tujuan = tujuan
 
 def info(self):
    print(f"kereta : {self.kereta}\n tujuan : {self.tujuan}")
 
keretaA = KeretaApi("CirebonExpress", "Cirebon - Bandung")
keretaA.info()
