# ZAYYAD
# 210510002
# D3

class  Fahrenheit :
 def  __init__(self,  fahrenheit): 
  self.fahrenheit = fahrenheit
 
 def  to_celcius(self):
   return  5/9  *  (self.fahrenheit  -  32) 
 def  to_kelvin(self):
   return  5/9  *  (self.fahrenheit  -  32)  +  273 
 def  to_reamur(self):
   return  4/9  *  (self.fahrenheit  -  32) 
 
fahrenheit = Fahrenheit(20)
print(f"Konversi  derajat  Fahrenheit  ke  derajat  Celcius  adalah  : {fahrenheit.to_celcius()}")
print(f"Konversi  derajat  Fahrenheit  ke  derajat  Kelvin  adalah  : {fahrenheit.to_kelvin()}")
print(f"Konversi  derajat  Fahrenheit  ke  derajat  Reamur  adalah  : {fahrenheit.to_reamur()}")
