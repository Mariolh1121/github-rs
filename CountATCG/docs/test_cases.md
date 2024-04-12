# Casos de prueba o escenarios

Este documento describe casos de prueba para el script de Python desarrollado para contar la ocurrencia de cada nucleótido en una secuencia de ADN contenida en un archivo de texto desde la línea de comandos. Los casos de prueba han sido diseñados considerando las diferentes funcionalidades del script, así como los posibles errores que puedan surgir. El archivo permite proporcionar la ruta de un archivo con la secuencia de ADN y contar la ocurrencia de todos los nucleótidos o uno en particular. Los casos de prueba cubren las características clave del programa y prueban varias condiciones para garantizar la robustez y confiabilidad del archivo.

### Caso de prueba 1: Secuencia con mayusculas y minisculas
```
nA = 0
nC = 0
nG = 0
nT = 0
sequence = ["a","T","C","G","A","A","A","A","A","G","G","G","G","T","T","T","T","C","a"]
for base in sequence:
    if base == 'A':
        nA+=1
    elif base == 'C':
        nC+=1
    elif base == 'G':
        nG+=1
    elif base == 'T':
        nT+=1
print(f"Contenido de Adenina = {nA} Guanina = {nG} Citosina = {nC}Timina = {nT}")
```

+ Output:
"Contenido de Adenina = 5 Guanina = 5 Citosina = 2Timina = 5"
+ No se cuentan todas las bases de la secuencia completa
