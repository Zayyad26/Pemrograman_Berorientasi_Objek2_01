from playsound import playsound
  
class Hewan:
    def speak(self):
        print("Suara Singa")

class Singa(Hewan):
    def speak(self):
        print("Ggrrraauurrrrkk...")
file_path = "lion.mp3"

def speak(animal):
        animal.speak()

hewan = Hewan()
singa = Singa()
speak(hewan)
speak(singa)
playsound(file_path)
