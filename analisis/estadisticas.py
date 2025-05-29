import numpy as np
from typing import List, Dict
from modelos.entidades import Estudiante

def calcular_estadisticas_grupo(estudiantes: List[Estudiante]) -> Dict[str, float]:
    if not estudiantes:
        return {}
    
    nombres_materias = [materia.nombre for materia in estudiantes[0].materias]
    
    # Promedios por asignatura
    promedios = {
        materia: np.mean([e.materias[i].nota for e in estudiantes])
        for i, materia in enumerate(nombres_materias)
    }
    
    # Porcentaje de aprobación general
    total_materias = len(estudiantes) * len(estudiantes[0].materias)
    aprobadas = sum(1 for e in estudiantes for m in e.materias if m.aprobada())
    porcentaje_aprobacion = (aprobadas / total_materias) * 100 if total_materias > 0 else 0
    
    # Materias con mejor/peor rendimiento
    materia_max = max(promedios.items(), key=lambda x: x[1])
    materia_min = min(promedios.items(), key=lambda x: x[1])
    
    return {
        'promedios': promedios,
        'porcentaje_aprobacion': porcentaje_aprobacion,
        'mejor_rendimiento': materia_max,
        'peor_rendimiento': materia_min
    }