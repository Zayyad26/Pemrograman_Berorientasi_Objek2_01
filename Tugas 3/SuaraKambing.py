from playsound import playsound
  
class Hewan:
    def speak(self):
        print("Suara Kambing")

class Kambing(Hewan):
    def speak(self):
        print("Mbeeekkk...")
file_path = "lamb.mp3"

def speak(animal):
        animal.speak()

hewan = Hewan()
lamb = Kambing()
speak(hewan)
speak(lamb)
playsound(file_path)
