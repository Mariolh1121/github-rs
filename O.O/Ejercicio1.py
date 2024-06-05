class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def haz_ruido(self):
        print("AAAAAAAAAAAAH")

class Perro(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def haz_ruido(self):
        print("WOW")

class Gato(Animal):
    def __init__(self, nombre, edad, usa_arenero):
        super().__init__(nombre, edad)
        self.usa_arenero = usa_arenero

    def haz_ruido(self):
        print("Miauuu")

# Ejemplo de uso
mi_perro = Perro("Cooper", 3)
mi_gato = Gato("Whiskas", 2, True)

print(f"El nombre de tu perro es : {mi_perro.nombre}, tiene: {mi_perro.edad} años")
mi_perro.haz_ruido()

print(f"El nombre de tu gato es : {mi_gato.nombre}, tiene {mi_gato.edad}, y usa arenero = {mi_gato.usa_arenero}")
mi_gato.haz_ruido()