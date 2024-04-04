'''
ATCG count
       

1.0
        

Mario Alberto Limón Hernández
        

DESCRIPTION: Counts number of ATCG nucleotides
        

CATEGORY
        

USAGE

    % python programName
    

ARGUMENTS


METHOD


SEE ALSO


        
'''
nA = 0
nC = 0
nG = 0
nT = 0
with open('archivo.txt', 'r') as file:
    lines = file.read()
sequence = lines.upper()
for base in sequence:
    if base == 'A':
        nA+=1
    elif base == 'C':
        nC+=1
    elif base == 'G':
        nG+=1
    elif base == 'T':
        nT+=1
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



