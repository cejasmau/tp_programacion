# Si todavía no fue instalado, se debe correr el código: pip install faker

import csv
import random
from faker import Faker

def generar_csv_estudiantes(n_estudiantes: int = 20, nombre_archivo: str = 'estudiantes.csv') -> str:
    """Genera un archivo CSV con datos aleatorios de estudiantes y sus notas"""
    fake = Faker('es_ES')

    # Lista de materias
    materias = ['matemáticas', 'física', 'química', 'biología', 
                'literatura', 'historia', 'geografía', 'economía',
                 'inglés', 'artes', 'educación_fisica', 'computación']
    
    # Crea el archivo CSV
    with open(nombre_archivo, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['nombre', 'apellido'] + materias)
        writer.writeheader()
        
        # Generamos datos aleatorios para cada estudiante
        for _ in range(n_estudiantes):
            estudiante = {
                'nombre': fake.first_name(),
                'apellido': fake.last_name(),
                **{materia: random.randint(1, 10) for materia in materias}
            }
            writer.writerow(estudiante)
    
    return nombre_archivo