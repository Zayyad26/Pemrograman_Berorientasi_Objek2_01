#ZAYYAD
#210510002
#D3

class Celcius: 

 @staticmethod
 def  to_fahrenheit(Celcius): return  (Celcius  *  9/5)  +  32
 @staticmethod
 def  to_kelvin(Celcius): return  Celcius  +  273.15
 @staticmethod
 def  to_reamur(Celcius): return  Celcius  *  4/5

mycelcius1  =  75
mycelcius2  =  60
mycelcius3  =  90

myfahrenheit  =  Celcius.to_fahrenheit(mycelcius1)
print("Konversi",  mycelcius1,  "derajat  Celcius  adalah",  myfahrenheit,  "derajat Fahrenheit")
mykelvin  =  Celcius.to_kelvin(mycelcius2)
print("Konversi",  mycelcius2,  "derajat  Celcius  adalah",  mykelvin,  "derajat Kelvin")
myreamur  =  Celcius.to_reamur(mycelcius3)
print("Konversi",  mycelcius3,  "derajat  Celcius  adalah",  myreamur,  "derajat Reamur")
