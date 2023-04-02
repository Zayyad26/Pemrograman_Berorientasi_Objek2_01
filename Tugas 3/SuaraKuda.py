from playsound import playsound
  
class Hewan:
    def speak(self):
        print("Suara Kuda")

class Kuda(Hewan):
    def speak(self):
        print("Brhiiikkkkkkk...")
file_path = "kuda.mp3"

def speak(animal):
        animal.speak()

hewan = Hewan()
kuda = Kuda()
speak(hewan)
speak(kuda)
playsound(file_path)
