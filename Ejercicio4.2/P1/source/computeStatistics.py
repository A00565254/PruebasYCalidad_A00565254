# pylint: disable=invalid-name
"""
Guillermo Contreras Pedroza
A00565254
Este módulo calcula estadísticas descriptivas (media, mediana, moda, etc.)
a partir de un archivo de texto con números, cumpliendo con los estándares
de la tarea de programación.
"""
import sys
import time


def sort_list(data):
    """Algoritmo de ordenamiento (Bubble Sort) para encontrar la mediana."""
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


def get_stats(numbers):
    """Calcula estadísticas descriptivas usando algoritmos básicos."""
    n = len(numbers)
    if n == 0:
        return None

    # --- Media ---
    total_sum = 0.0
    for x in numbers:
        total_sum += x
    mean = total_sum / n

    # --- Mediana ---
    # Ordenamos una copia para no alterar el orden original si fuera necesario
    sorted_nums = sort_list(list(numbers))
    if n % 2 == 0:
        median = (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2
    else:
        median = sorted_nums[n // 2]

    # --- Moda ---
    counts = {}
    for x in numbers:
        counts[x] = counts.get(x, 0) + 1

    max_freq = 0
    mode = numbers[0]
    for key, value in counts.items():
        if value > max_freq:
            max_freq = value
            mode = key

    # --- Varianza y Desviación Estándar ---
    sum_sq_diff = 0.0
    for x in numbers:
        sum_sq_diff += (x - mean) ** 2

    variance = sum_sq_diff / n
    std_dev = variance ** 0.5

    return mean, median, mode, variance, std_dev


def main():
    """Calcula la media, mediana, moda, varianza y desviación estándar.

    Args:
        numbers (list): Una lista de números flotantes.

    Returns:
        tuple: Contiene (media, mediana, moda, varianza, desviación).
    """
    start_time = time.time()

    if len(sys.argv) != 2:
        print("Uso: python computeStatistics.py fileWithData.txt")
        return

    file_path = sys.argv[1]
    numbers = []

    # Lectura y manejo de errores (Req 3)
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                val = line.strip()
                if not val:
                    continue
                try:
                    numbers.append(float(val))
                except ValueError:
                    print(f"Error: '{val}' no es un número válido. Saltando...")
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no existe.")
        return

    if not numbers:
        print("Error: No se encontraron datos numéricos para procesar.")
        return

    # Cálculos
    stats = get_stats(numbers)
    elapsed_time = time.time() - start_time

    # Formateo de resultados (Req 2)
    mean, median, mode, variance, std_dev = stats
    results = (
        f"--- Estadísticas Descriptivas ---\n"
        f"Media: {mean:.4f}\n"
        f"Mediana: {median:.4f}\n"
        f"Moda: {mode}\n"
        f"Varianza: {variance:.4f}\n"
        f"Desviación Estándar: {std_dev:.4f}\n"
        f"Tiempo transcurrido: {elapsed_time:.6f} segundos\n"
    )

    # Salida a pantalla y archivo
    print(results)
    with open("StatisticsResults.txt", "w", encoding="utf-8") as f:
        f.write(results)


if __name__ == "__main__":
    main()
