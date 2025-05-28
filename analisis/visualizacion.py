import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from typing import List
from modelos.entidades import Estudiante

def mostrar_rendimiento(estudiantes: List[Estudiante]) -> None:
    """Muestra el rendimiento académico de los estudiantes"""
    print("\n=== RENDIMIENTO ACADÉMICO ===")
    for i, estudiante in enumerate(estudiantes, 1):
        print(f"\nEstudiante #{i}")
        print(estudiante)
        print("Detalle de materias:")
        for materia in estudiante.materias:
            estado = "Aprobada" if materia.aprobada() else "Reprobada"
            print(f"- {materia.nombre}: {materia.nota} ({estado})")

def mostrar_estadisticas(estadisticas: dict) -> None:
    print("\n=== ESTADÍSTICAS GENERALES DEL GRUPO ===")
    
    print("\nPromedio por asignatura:")
    for materia, promedio in estadisticas['promedios'].items():
        print(f"- {materia.capitalize()}: {promedio:.2f}")
    
    print(f"\nPorcentaje de aprobación general: {estadisticas['porcentaje_aprobacion']:.2f}%")
    
    print("\nAsignaturas con mayor y menor rendimiento:")
    print(f"- Mayor rendimiento: {estadisticas['mejor_rendimiento'][0].capitalize()} ({estadisticas['mejor_rendimiento'][1]:.2f})")
    print(f"- Menor rendimiento: {estadisticas['peor_rendimiento'][0].capitalize()} ({estadisticas['peor_rendimiento'][1]:.2f})")

def generar_graficos_distribucion(estudiantes: List[Estudiante]) -> None:
    if not estudiantes:
        print("\nNo hay datos para generar gráficos.")
        return
    
    plt.style.use('seaborn-v0_8')
    nombres_materias = [materia.nombre for materia in estudiantes[0].materias]

    # Generar un gráfico por materia
    for i, materia_nombre in enumerate(nombres_materias):
        notas = [e.materias[i].nota for e in estudiantes]
        promedio, std_dev = np.mean(notas), np.std(notas)
        
        plt.figure(figsize=(10, 6))

        # Crear distribución normal teórica
        x = np.linspace(0, 10, 1000)
        y = norm.pdf(x, promedio, std_dev)
        
        # Graficar
        plt.plot(x, y, 'b-', linewidth=2, label='Distribución teórica')
        plt.fill_between(x, y, color='blue', alpha=0.1)
        
        # Graficar histograma de datos reales
        plt.hist(notas, bins=10, density=True, alpha=0.5, color='green', label='Datos reales')
        
        # Línea vertical para el promedio
        plt.axvline(promedio, color='red', linestyle='--', linewidth=2, label=f'Promedio: {promedio:.2f}')
        
        # Configuración del gráfico
        plt.title(f'Distribución de notas en {materia_nombre.capitalize()}\n'
                 f'Promedio: {promedio:.2f} - Desviación: {std_dev:.2f}')
        plt.xlabel('Notas')
        plt.ylabel('Densidad')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.xlim(0, 10)

        # Mostrar gráfico
        plt.tight_layout()
        plt.show()