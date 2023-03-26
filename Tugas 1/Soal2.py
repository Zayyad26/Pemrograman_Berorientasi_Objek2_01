
#ZAYYAD
#210510002
#D3

class  Konversi  :
    
 def __init__(self,  celcius): 
     self.celcius = celcius
 def  to_fahrenheit(self):
    return  (self.celcius  *  9/5)  +  32 
 def  to_kelvin(self): 
    return  (self.celcius  +  273.15) 
 def  to_reamur(self):
    return  (self.celcius  *  4/5)

celciusA  =  Konversi(75) 
celciusB  =  Konversi(90) 
celciusC  =  Konversi(60)

print(f"Konversi  derajat  Celcius  ke  derajat  Fahrenheit  adalah  : {celciusA.to_fahrenheit()}")
print(f"Konversi  derajat  Celcius  ke  derajat  Kelvin  adalah  : {celciusB.to_kelvin()}")
