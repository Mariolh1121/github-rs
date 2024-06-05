class Animal():
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad
  def haz_ruido(self):
    print("AAHHH")

class Perro(Animal):
  def haz_ruido(self):
    print("Guau guau")

class Gato(Animal):
  def __init__(self, nombre, edad, usa_arenero):
    super().__init__(nombre, edad)
    self.usa_arenero = usa_arenero
  def haz_ruido(self):
    print("Miau miau")
  
perro = Perro("Golliat", 1)
ruido = perro.haz_ruido()
print(f"El nombre de tu perro es {perro.nombre}, tiene {perro.edad} año")
ruido
