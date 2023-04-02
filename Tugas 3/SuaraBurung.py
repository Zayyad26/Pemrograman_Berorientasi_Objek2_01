from playsound import playsound
  
class Hewan:
    def speak(self):
        print("Suara Burung")

class Burung(Hewan):
    def speak(self):
        print("Kiekk..kiekk..brrrkk..kieekk")
file_path = "burung.mp3"

def speak(animal):
        animal.speak()

hewan = Hewan()
burung = Burung()
speak(hewan)
speak(burung)
playsound(file_path)
