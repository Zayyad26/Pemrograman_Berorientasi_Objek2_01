# ZAYYAD
# 210510002
# D3

class Reamur :
 def    __init__  (self,  reamur)  : 
     self.reamur = reamur

 def  to_celcius(self):  
    return  5/4  *  self.reamur
 def  to_kelvin(self):
    return  5/4  *  self.reamur  +  273 
 def  to_fahrenheit(self):
    return  (9/4  *  self.reamur)  +  32 

reamur  =  Reamur(15) 
print(f"Konversi  derajat  Reamur  ke  derajat  Celcius  adalah  : {reamur.to_celcius()}")
print(f"Konversi  derajat  Reamur  ke  derajat  Kelvin  adalah  :  {reamur.to_kelvin()}") 
print(f"Konversi  derajat  Reamur  ke  derajat  Fahrenheit  adalah  : {reamur.to_fahrenheit()}")

