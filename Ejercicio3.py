# Crea una nueva subclase Trabajador que sobrescriba presentarse() para que incluya su empresa.

class persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.profesion}.")

ana = persona("Ana", 32 , "arquitecta")

ana.presentarse()

class estudiante(persona):
    def __init__(self, nombre, edad, profesion, asignatura):
        super().__init__(nombre, edad, profesion)
        self.asignatura = asignatura
        
    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.profesion} de {self.asignatura}.")

juan = estudiante("Juan", 20, "estudiante", "matemáticas")
juan.presentarse()

class trabajador(persona):
    def __init__(self, nombre, edad, profesion, empresa):
        super().__init__(nombre, edad, profesion)
        self.empresa = empresa
    
    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.profesion} en {self.empresa}.")

pedro = trabajador("Pedro", 30, "ingeniero", "Google")
pedro.presentarse()