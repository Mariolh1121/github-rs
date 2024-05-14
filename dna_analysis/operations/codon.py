def read_dna_sequence(filename):
    """
    Lee la secuencia de ADN de un archivo.
    
    Args:
        filename (str): Nombre del archivo.
        
    Returns:
        str: Secuencia de ADN.
    """
    with open(filename, 'r') as file:
        sequence = file.read().strip()
    
    # Verificar que la secuencia solo contiene A, C, G, T
    assert all(c in 'ACGTN' for c in sequence), "La secuencia contiene caracteres no válidos."
    
    # Verificar que la longitud de la secuencia es múltiplo de tres
    assert len(sequence) % 3 == 0, "La longitud de la secuencia de ADN no es múltiplo de tres."
    
    return sequence

def calculate_codon_frequency(sequence):
    """
    Calcula la frecuencia de cada codón en la secuencia de ADN.

    Args:
        sequence (str): Secuencia de ADN.
        
    Returns:
        dict: Diccionario con la frecuencia de cada codón.
    """
    codon_frequency = {}
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i+3]
        if codon in codon_frequency:
            codon_frequency[codon] += 1
        else:
            codon_frequency[codon] = 1
    return codon_frequency