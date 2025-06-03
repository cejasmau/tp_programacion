# Si todavía no fue instalado, se debe correr el código: pip install dataclasses

from dataclasses import dataclass

# Usamos dataclasses para definir las entidades de nuestro modelo de forma más sencilla y legible.
@dataclass
class Materia:
    nombre: str
    nota: int
    
    def aprobada(self) -> bool:
        return self.nota >= 6

@dataclass
class Estudiante:
    nombre: str
    apellido: str
    materias: list  # Vamos a definir Materia como Lista de objetos
    
    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido} - Promedio: {self.calcular_promedio():.2f}"
    
    def calcular_promedio(self) -> float:
        if not self.materias:
            return 0.0
        return sum(materia.nota for materia in self.materias) / len(self.materias)