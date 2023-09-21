import math
from abc import ABC, abstractmethod

class Figura(ABC):
    
    def __init__(self, base, altura):
        self._base = base
        self._altura = altura

    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, base):
        self._base = base

    @property
    def altura(self):
        return self._altura 
    
    @altura.setter
    def altura(self, altura):
        self._altura = altura

    @abstractmethod    
    def area() -> int:
        pass
    
    @abstractmethod
    def perimetre() -> int:
        pass

class Cercle(Figura):
    def __init__(self, radi):
        self._radi = radi
    
    def area(self) -> int:
        return math.pi * self._radi **2
    
    def perimetre(self) -> int:
        return 2 * math.pi * self._radi
    
class Triangle(Figura):

    def __init__(self, base, altura, costat):
        super().__init__(base, altura)
        self._costat = costat
        
    def area(self) -> int:
        return self._base * self._altura / 2
    
    def perimetre(self) -> int:
        return self._costat * 3

class Rectangle(Figura):

    def area(self) -> int:
        return self._base * self._altura
    
    def perimetre(self) -> int:
        return self._base * 2 + self._altura * 2
    
class Quadrat(Rectangle):
    pass

print("")  
cercle = Cercle(3)
print("-- Cercle, Área: ", cercle.area(), ", Perímetre: ", cercle.perimetre(), "\n")
triangle = Triangle(2,3,2)
print("-- Triangle, Àrea: ", triangle.area(), ", Perímetre: ", triangle.perimetre(), "\n")
rectangle = Rectangle(2,3)
print("-- Rectangle, Àrea: ", rectangle.area(), ", Perímetre: ", rectangle.perimetre(), "\n")
quadrat = Quadrat(2,2)
print("-- Quadrat, Àrea: ", quadrat.area(), ", Perímetre: ", quadrat.perimetre(), "\n")
