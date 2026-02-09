# pylint: disable=invalid-name
"""
Guillermo Contreras Pedroza
A00565254

Módulo para contar la frecuencia de palabras en un archivo de texto.
Este programa identifica palabras distintas y su frecuencia de aparición,
generando resultados tanto en consola como en un archivo externo,
utilizando algoritmos básicos sin librerías externas.
"""
import sys
import time


def get_words_from_file(file_path):
    """Lee el archivo y extrae palabras ignorando errores de datos."""
    words = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Separar palabras manualmente basándose en espacios
                current_word = ""
                for char in line:
                    if char.isspace():
                        if current_word:
                            words.append(current_word)
                            current_word = ""
                    else:
                        current_word += char
                # Agregar la última palabra de la línea si existe
                if current_word:
                    words.append(current_word)
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no existe.")
        return None
    except OSError as e:
        print(f"Error inesperado al leer el archivo: {e}")
        return None
    return words


def count_frequencies(word_list):
    """Calcula la frecuencia usando algoritmos básicos (sin librerías)."""
    distinct_words = []
    counts = []

    for word in word_list:
        found = False
        # Buscamos si la palabra ya está en nuestra lista de distintas
        for i, d_word in enumerate(distinct_words):
            if d_word == word:
                counts[i] += 1
                found = True
                break

        # Si no se encontró, es una palabra nueva
        if not found:
            distinct_words.append(word)
            counts.append(1)

    return distinct_words, counts


def main():
    """
    Punto de entrada del programa. Coordina la lectura del archivo,
    el conteo de frecuencias y la salida de resultados (consola y archivo).
    """
    start_time = time.time()

    # Validar que se reciba el parámetro del archivo (Req 1 & 5)
    if len(sys.argv) != 2:
        print("Uso: python wordCount.py fileWithData.txt")
        return

    file_path = sys.argv[1]

    # Obtener palabras manejando errores (Req 3)
    words = get_words_from_file(file_path)
    if words is None:
        return

    # Calcular frecuencias (Req 2)
    distinct_words, counts = count_frequencies(words)

    # Calcular tiempo transcurrido (Req 7)
    elapsed_time = time.time() - start_time

    # Preparar resultados
    output_lines = []
    for i, word in enumerate(distinct_words):
        output_lines.append(f"{word}: {counts[i]}")

    time_info = f"Tiempo transcurrido: {elapsed_time:.6f} segundos"
    output_lines.append(time_info)

    # Imprimir en pantalla y guardar en archivo (Req 2)
    result_content = "\n".join(output_lines)
    print(result_content)

    try:
        with open("WordCountResults.txt", "w", encoding="utf-8") as f:
            f.write(result_content)
    except OSError as e:
        print(f"Error al escribir el archivo de resultados: {e}")


if __name__ == "__main__":
    main()
