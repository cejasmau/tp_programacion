import csv
from typing import List
from modelos.entidades import Estudiante, Materia

def procesar_csv(ruta_csv: str) -> List[Estudiante]:
    """Procesa el CSV y crea instancias de Estudiante con sus Materias"""
    estudiantes = []
    
    with open(ruta_csv, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        materias_disponibles = [field for field in reader.fieldnames if field not in ['nombre', 'apellido']]
        
        for row in reader:
            materias = [Materia(nombre, int(row[nombre])) for nombre in materias_disponibles]
            estudiantes.append(Estudiante(row['nombre'], row['apellido'], materias))
    
    return estudiantes
