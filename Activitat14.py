import math

class Figura():
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area() -> int:
        pass
    def perimetre() -> int:
        pass

class Cercle(Figura):
    def __init__(self, radi):
        self.radi = radi
    
    def area(self) -> int:
        return math.pi * self.radi **2
    
    def perimetre(self) -> int:
        return 2 * math.pi * self.radi
    
class Triangle(Figura):

    def __init__(self, base, altura, costat):
        super().__init__(base, altura)
        self.costat = costat
        
    def area(self) -> int:
        return self.base * self.altura / 2
    
    def perimetre(self) -> int:
        return self.costat * 3

class Rectangle(Figura):

    def area(self) -> int:
        return self.base * self.altura
    
    def perimetre(self) -> int:
        return self.base * 2 + self.altura * 2
    
class Quadrat(Rectangle):
    pass

print("")  
cercle = Cercle(3)
print("-- Cercle, Área: ", cercle.area(), ", Perímetre: ", cercle.perimetre(), "\n")
triangle = Triangle(2,3,2)
print("-- Triangle, Àrea: ", triangle.area(), ", Perímetre: ", triangle.perimetre(), "\n")
rectangle = Rectangle(2,3)
print("-- Rectangle, Àrea: ", rectangle.area(), ", Perímetre: ", rectangle.perimetre(), "\n")
quadrat = Quadrat(2,3)
print("-- Quadrat, Àrea: ", quadrat.area(), ", Perímetre: ", quadrat.perimetre(), "\n")