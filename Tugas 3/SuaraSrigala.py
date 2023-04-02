from playsound import playsound
  
class Hewan:
    def speak(self):
        print("Suara Serigala")

class Wolf(Hewan):
    def speak(self):
        print("Aauuuukkkkk...ukkk")
file_path = "wolf.mp3"

def speak(animal):
        animal.speak()

hewan = Hewan()
wolf = Wolf()
speak(hewan)
speak(wolf)
playsound(file_path)
