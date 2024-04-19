'''
ATCG count
       

2.0
        

Mario Alberto Limón Hernández
        

DESCRIPTION: 
This script counts the occurrence of nucleotides 'A', 'T', 'G' and 'C' in a file with a .txt extension.
The file is provided as a positional argument from the command line.

Options:
inputfile: Path to the input file containing DNA sequences.
        
-n  --nucleotides: Nucleotides to be counted.
        

USAGE

    % Count of ATCG
    

ARGUMENTS

-Raw file

METHOD

-Counting nomber of each nucleotide by reading the file


        
'''
import argparse

def count_nucleotides(sequence, nucleotides):
    if not sequence:
        raise ValueError("El archivo está vacío, no se puede contar los nucleótidos.")

    valid_characters = set('ATGC')
    for nucleotide in sequence:
           if nucleotide not in valid_characters:
                  print(f"Sequence contains {nucleoetide}, it is invalid character")

    sequence = sequence.upper()  # Convertir a mayúsculas para contar independientemente de la capitalización
    nA = sequence.count('A')
    nC = sequence.count('C')
    nG = sequence.count('G')
    nT = sequence.count('T')
    counts = {'A': nA, 'C': nC, 'G': nG, 'T': nT}
    return {n: counts.get(n, 0) for n in nucleotides} if nucleotides else counts

parser = argparse.ArgumentParser(description='Count occurrences of nucleotides in a DNA sequence file.')
parser.add_argument('filename', metavar='FILENAME', type=str, help='Name of the file containing the DNA sequence')
parser.add_argument('-n', '--nucleotides', metavar='N', nargs='+', type=str, help='List of nucleotides to count')
args = parser.parse_args()

try:
    with open(args.filename, 'r') as file:
        sequence = file.read().strip().upper()
        counts = count_nucleotides(sequence, args.nucleotides)
        for nucleotide, count in counts.items():
            print(f"Frecuencia de {nucleotide}: {count}")
except FileNotFoundError:
    print("Sorry, couldn't find the file.")
except ValueError as e:
    print(f"Error: {e}")
# Posteriormente se imprime

# ===========================================================================
# = File                            imports
# ===========================================================================





# ===========================================================================
# =                            Command Line Options
# ===========================================================================






# ===========================================================================
# =                            functions
# ===========================================================================





# ===========================================================================
# =                            main
# ===========================================================================


# step 1.


# step 2.


# step 3.



