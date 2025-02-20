# Crea una clase Figura con un método calcular_area() vacío (pass). Luego, crea las 
# clases Circulo y Rectangulo que implementen este método.

class Figura:
    def calcular_area(self):
        pass
    
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
        
    def calcular_area(self):
        return 3.14 * self.radio ** 2

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura

circulo = Circulo(5)
print(circulo.calcular_area())

rectangulo = Rectangulo(4, 6)
print(rectangulo.calcular_area())