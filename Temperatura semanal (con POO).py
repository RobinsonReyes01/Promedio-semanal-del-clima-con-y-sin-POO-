class RegistroClima:
    """
    Clase para gestionar el registro y análisis de temperaturas semanales.

    Características principales:
    - Encapsulamiento de datos de temperatura
    - Métodos para entrada, cálculo y presentación de datos
    - Manejo de errores y validación de entrada
    """

    def __init__(self):
        """
        Constructor de la clase RegistroClima.

        Inicializa:
        - Lista privada de temperaturas (__temperaturas)
        - Lista de días de la semana (__dias)
        """
        # Atributo privado para almacenar temperaturas
        self.__temperaturas = []

        # Lista de días de la semana
        self.__dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

    def ingresar_temperaturas(self):
        """
        Método para recopilar temperaturas diarias.

        Funcionalidades:
        - Limpia registros anteriores
        - Solicita temperatura para cada día
        - Valida entradas numéricas
        - Almacena temperaturas en lista privada
        """
        # Limpiar los registros previos antes de nueva entrada
        self.__temperaturas.clear()

        # Ciclo para ingresar temperatura por día
        for dia in self.__dias:
            while True:
                try:
                    # Solicitar y convertir entrada a flotante
                    temperatura = float(input(f"Ingrese la temperatura para {dia}: "))
                    self.__temperaturas.append(temperatura)
                    break  # Salir del bucle si entrada es válida
                except ValueError:
                    # Manejar entradas no numéricas
                    print("Por favor, ingrese un valor numérico válido.")

    def calcular_promedio_semanal(self):
        """
        Calcula el promedio de temperaturas semanales.

        Returns:
            float: Promedio de temperaturas, 0 si no hay datos

        Características:
        - Manejo de lista vacía
        - Cálculo de promedio mediante suma y longitud
        """
        # Prevenir la división por cero
        if not self.__temperaturas:
            return 0

        # Calcular promedio de temperaturas
        return sum(self.__temperaturas) / len(self.__temperaturas)

    def mostrar_resultados(self, promedio):
        """
        Presenta informe de temperaturas y promedio semanal.

            promedio (float): Promedio de temperaturas calculado

        Funciones:
        - Imprimir temperaturas diarias
        - Muestra el promedio semanal
        """
        print("\n--- Reporte Semanal de Temperaturas ---")

        # Mostrar temperatura para cada día
        for dia, temperatura in zip(self.__dias, self.__temperaturas):
            print(f"{dia}: {temperatura}°C")

        # Imprimir promedio con formato de dos decimales
        print(f"\nPromedio Semanal: {promedio:.2f}°C")

    def ejecutar(self):
        """
        Método principal que coordina el flujo completo del programa.

        Pasos:
        1. Muestra el título
        2. Ingresa las temperaturs
        3. Calcular el promedio
        4. Mostrar los resultados
        """
        print("Calculadora de Promedio Semanal del Clima")
        self.ingresar_temperaturas()  # Recopilar datos
        promedio = self.calcular_promedio_semanal()  # Calcular promedio
        self.mostrar_resultados(promedio)  # Presentar resultados


def main():
    """
    Función principal para iniciar y ejecutar el programa.

    Crea una instancia de RegistroClima y ejecuta el proceso.
    """
    registro = RegistroClima()  # Crear objeto de la clase
    registro.ejecutar()  # Inicia el proceso


# Punto de entrada del programa
if __name__ == "__main__":
    main()