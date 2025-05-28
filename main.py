from datos.generador_datos import generar_csv_estudiantes
from datos.procesamiento import procesar_csv
from analisis.visualizacion import mostrar_rendimiento, mostrar_estadisticas, generar_graficos_distribucion
from analisis.estadisticas import calcular_estadisticas_grupo

def main():
    # Generar y procesar datos
    archivo = generar_csv_estudiantes()
    estudiantes = procesar_csv(archivo)
    
    # Mostrar resultados
    mostrar_rendimiento(estudiantes)
    estadisticas = calcular_estadisticas_grupo(estudiantes)
    mostrar_estadisticas(estadisticas)
    generar_graficos_distribucion(estudiantes)

if __name__ == "__main__":
    main()