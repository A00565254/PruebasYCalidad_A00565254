# pylint: disable=invalid-name
"""
Guillermo Contreras Pedroza
A00565254

Módulo para la conversión de números a sistemas binario y hexadecimal.
Este programa lee un archivo de texto, procesa cada número utilizando
algoritmos de división sucesiva y guarda los resultados en un archivo.
"""
import sys
import time


def to_binary(n):
    """Convierte un número entero a binario usando algoritmos básicos."""
    if n == 0:
        return "0"
    binary = ""
    is_negative = False
    if n < 0:
        is_negative = True
        n = abs(n)

    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2

    return "-" + binary if is_negative else binary


def to_hexadecimal(n):
    """Convierte un número entero a hexadecimal usando algoritmos básicos."""
    if n == 0:
        return "0"
    hex_chars = "0123456789ABCDEF"
    hex_result = ""
    is_negative = False
    if n < 0:
        is_negative = True
        n = abs(n)

    while n > 0:
        remainder = n % 16
        hex_result = hex_chars[remainder] + hex_result
        n = n // 16

    return "-" + hex_result if is_negative else hex_result


def main():
    """
    Punto de entrada del programa. Gestiona la lectura de argumentos,
    el procesamiento del archivo y la escritura de resultados.
    """
    start_time = time.time()

    # Validar parámetros de entrada (Req 1 & 5)
    if len(sys.argv) != 2:
        print("Uso: python convertNumbers.py fileWithData.txt")
        return

    file_path = sys.argv[1]
    results = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                raw_data = line.strip()
                if not raw_data:
                    continue

                try:
                    # Intentar convertir a entero (Req 3)
                    number = int(float(raw_data))

                    # Realizar conversiones (Req 2)
                    bin_val = to_binary(number)
                    hex_val = to_hexadecimal(number)

                    res_str = f"N: {number} -> BIN: {bin_val} | HEX: {hex_val}"
                    results.append(res_str)
                except ValueError:
                    print(f"Error: '{raw_data}' no es un número válido. Omitiendo...")
                    continue
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no fue encontrado.")
        return

    # Calcular tiempo (Req 7)
    elapsed_time = time.time() - start_time
    time_info = f"Tiempo transcurrido: {elapsed_time:.6f} segundos"
    results.append(time_info)

    # Mostrar y guardar resultados (Req 2)
    final_output = "\n".join(results)
    print(final_output)

    try:
        with open("ConvertionResults.txt", "w", encoding="utf-8") as f:
            f.write(final_output)
    except OSError as e:
        print(f"Error al guardar los resultados: {e}")


if __name__ == "__main__":
    main()
