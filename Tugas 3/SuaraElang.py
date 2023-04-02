from playsound import playsound
  
class Hewan:
    def speak(self):
        print("Suara Burung Elang")

class Elang(Hewan):
    def speak(self):
        print("Kyakk..kyakk..kkyakkk")
file_path = "elang.mp3"

def speak(animal):
        animal.speak()

hewan = Hewan()
el = Elang()
speak(hewan)
speak(el)
playsound(file_path)
