from playsound import playsound
  
class Hewan:
    def speak(self):
        print("Suara Ayam")

class Ayam(Hewan):
    def speak(self):
        print("Kukuu...ruyuukkk...")
file_path = "Ayam Jago.mp3"

def speak(animal):
        animal.speak()

hewan = Hewan()
ayam = Ayam()
speak(hewan)
speak(ayam)
playsound(file_path)
