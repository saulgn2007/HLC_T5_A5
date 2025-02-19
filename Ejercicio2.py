# Extiende la clase Persona creando una subclase Estudiante, agregando un nuevo atributo grado 
# y sobrescribiendo el método presentarse().

class persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.profesion}.")

p = persona("Ana", 32 , "arquitecta")

p.presentarse()