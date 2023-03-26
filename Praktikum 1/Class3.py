# ZAYYAD
# 210510002
# D3

class Kelvin :
 def  __init__   (self,  kelvin)  : 
    self.kelvin = kelvin

 def  to_celcius(self):  
    return  self.kelvin  -  273
 def  to_reamur(self):
    return  4/5  *  (self.kelvin  -  273) 
 def  to_fahrenheit(self):
    return  9/5  *  (self.kelvin  -  273)  +  32
 

kelvin  =  Kelvin(25)

print(f"Konversi  derajat  Kelvin  ke  derajat  Celcius  adalah  : {kelvin.to_celcius()}")
print(f"Konversi  derajat  Kelvin  ke  derajat  Reamur  adalah  :  {kelvin.to_reamur()}") 
print(f"Konversi  derajat  Kelvin  ke  derajat  Fahrenheit  adalah  : {kelvin.to_fahrenheit()}")
