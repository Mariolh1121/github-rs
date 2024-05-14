"""
Programa que calcula la frecuencia de todos los codones en una secuencia de ADN.

Uso:
    python frecuencia_codones.py archivo_adn.txt

Argumentos:
    archivo_adn.txt: Nombre del archivo que contiene la secuencia de ADN.

Descripción:
    Este programa lee la secuencia de ADN desde un archivo y calcula la frecuencia de cada 
    codón de tres bases presentes en la secuencia. Los resultados se imprimirán en la salida estándar. 
    Asegúrese de que la secuencia de ADN solo contenga caracteres válidos ('A', 'C', 'G', 'T') y su longitud 
    sea múltiplo de tres.
"""

import argparse
from dna_analysis.operations.codon import read_dna_sequence, calculate_codon_frequency

def main():
    parser = argparse.ArgumentParser(description="Calcula la frecuencia de codones en una secuencia de ADN.")
    parser.add_argument("file", type=str, help="Archivo de ADN a procesar")
    args = parser.parse_args()
    
    try:
        dna_sequence = read_dna_sequence(args.file)
        codon_freq = calculate_codon_frequency(dna_sequence)
        
        print("Frecuencia de codones:")
        for codon, frequency in codon_freq.items():
            print(f"{codon}: {frequency}")
    except FileNotFoundError:
        print(f"Error: El archivo '{args.file}' no se encontró.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()