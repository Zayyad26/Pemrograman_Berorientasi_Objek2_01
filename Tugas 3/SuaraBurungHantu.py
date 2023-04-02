from playsound import playsound
  
class Hewan:
    def speak(self):
        print("Suara Burung Hantu")

class Owl(Hewan):
    def speak(self):
        print("Uukk..uuukk..uukk")
file_path = "burung hantu.mp3"

def speak(animal):
        animal.speak()

hewan = Hewan()
owl = Owl()
speak(hewan)
speak(owl)
playsound(file_path)
