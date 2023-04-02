from playsound import playsound
  
class Hewan:
    def speak(self):
        print("Suara Gajah")

class Gajah(Hewan):
    def speak(self):
        print("kwanggggggggkk...")
file_path = "elephant.mp3"

def speak(animal):
        animal.speak()

hewan = Hewan()
el = Gajah()
speak(hewan)
speak(el)
playsound(file_path)
