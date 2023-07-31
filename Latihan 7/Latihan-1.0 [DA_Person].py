class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Rifky", 21)

# Menambah atribut address secara dinamis
person.address = "RT.3/RW.2 Cigobang, Pasaleman, Kab.Cirebon."

# Mengubah nilai atribut age secara dinamis
person.age = 21
print("Nama =",person.name)
print("Umur =",person.age)
print("Alamat =",person.address)
