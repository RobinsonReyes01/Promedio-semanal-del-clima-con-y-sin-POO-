# Función para gestionar la entrada de datos de temperatura
def ingresar_temperaturas():
    """
    Recopila las temperaturas diarias de la semana.

    Características:
    - Solicita temperaturas para cada día de la semana
    - Valida la entrada para garantizar valores numéricos
    - Maneja posibles errores de entrada del usuario

    Returns:
        list: Lista de temperaturas ingresadas
    """
    temperaturas = []  # Lista para almacenar las temperaturas
    dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

    # Bucle para recopilar temperaturas de cada día
    for dia in dias:
        while True:
            try:
                # Solicitar temperatura e intentar convertirla a float
                temperatura = float(input(f"Ingrese la temperatura para {dia}: "))
                temperaturas.append(temperatura)
                break  # Sale del bucle si la entrada es válida
            except ValueError:
                # Manejar entradas no numéricas
                print("Por favor, ingrese un valor numérico válido.")

    return temperaturas


# Función para calcular el promedio semanal de temperaturas
def calcular_promedio_semanal(temperaturas):
    """
    Calcula el promedio de las temperaturas recopiladas.

    Args:
        temperaturas (list): Lista de temperaturas diarias

    Returns:
        float: Promedio de temperaturas, 0 si la lista está vacía
    """
    # Validación de lista vacía para evitar división por cero
    if not temperaturas:
        return 0

    # Cálculo del promedio mediante suma total dividida por número de días
    return sum(temperaturas) / len(temperaturas)


# Función para presentar los resultados de manera estructurada
def mostrar_resultados(temperaturas, promedio):
    """
    Muestra un informe detallado de las temperaturas.
    Imprime:
    - Las temperaturas de cada día
    - El promedio semanal
    """
    print("\n--- Reporte Semanal de Temperaturas ---")
    dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

    # Mostrar la temperatura para cada día utilizando el comando zip
    for dia, temperatura in zip(dias, temperaturas):
        print(f"{dia}: {temperatura}°C")

    # Mostrarv el promedio con formato de dos decimales
    print(f"\nPromedio Semanal: {promedio:.2f}°C")


# Función principal que coordina la ejecución del programa
def main():
    """
    Función principal que orquesta el flujo del programa.

    Pasos:
    1. Mostrar nombre del programa
    2. Ingresar las temperaturas
    3. Calcular el promedio
    4. Muestra resultados
    """
    print("Calculadora de Promedio Semanal del Clima")
    temperaturas = ingresar_temperaturas()  # Recopilar datos
    promedio = calcular_promedio_semanal(temperaturas)  # Calcular promedio
    mostrar_resultados(temperaturas, promedio)  # Presentar resultados


# Punto de entrada del programa
if __name__ == "__main__":
    main()