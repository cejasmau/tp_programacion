class Materia:
    """Clase que representa una materia con su nota"""
    def __init__(self, nombre, nota=0):
        self.nombre = nombre
        self.nota = nota

    def __str__(self):
        return f"{self.nombre}: {self.nota}"

    def aprobada(self):
        """Determina si la materia está aprobada"""
        return self.nota >= 6

class Estudiante:
    """Clase que representa un estudiante con sus materias y calificaciones"""
    def __init__(self, nombre, apellido, materias):
        self.nombre = nombre
        self.apellido = apellido
        self.materias = {m.nombre: m for m in materias}

    def promedio_general(self):
        """Calcula el promedio general del estudiante"""
        notas = [m.nota for m in self.materias.values()]
        return sum(notas) / len(notas) if notas else 0

    def materias_aprobadas(self):
        """Retorna la cantidad de materias aprobadas"""
        return sum(1 for m in self.materias.values() if m.aprobada())

    def __str__(self):
        """Representación legible del estudiante."""
        return (f"Estudiante: {self.nombre} {self.apellido}\n"
                f"Promedio: {self.promedio_general():.2f}\n"
                f"Materias aprobadas: {self.materias_aprobadas()}/{len(self.materias)}")