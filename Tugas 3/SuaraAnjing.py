from playsound import playsound
  
class Hewan:
    def speak(self):
        print("Suara Anjing")

class Anjing(Hewan):
    def speak(self):
        print("Gukk! guk..guk..gukkk!")
file_path = "anjing.mp3"

def speak(animal):
        animal.speak()

hewan = Hewan()
anjing = Anjing()
speak(hewan)
speak(anjing)
playsound(file_path)

