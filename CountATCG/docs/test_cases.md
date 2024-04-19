# Casos de prueba o escenarios

Este documento describe casos de prueba para el script de Python desarrollado para contar la ocurrencia de cada nucleótido en una secuencia de ADN contenida en un archivo de texto desde la línea de comandos. Los casos de prueba han sido diseñados considerando las diferentes funcionalidades del script, así como los posibles errores que puedan surgir. El archivo permite proporcionar la ruta de un archivo con la secuencia de ADN y contar la ocurrencia de todos los nucleótidos o uno en particular. Los casos de prueba cubren las características clave del programa y prueban varias condiciones para garantizar la robustez y confiabilidad del archivo.

### Caso de prueba 1: Secuencia con mayusculas y minisculas
+ Descripción: Verificar que el script puede contar de manera adecuada las ocurrencias de ATGC en una secuencia dada sin importar si se encuentra en mayúsculas o en minúsculas
+ Archivo con la siguiente secuencia: AGAGAGACCCGGTTTAGCGCAGT
+ Resultado esperado:
  + Frecuencia de A: 6
    Frecuencia de C: 5
    Frecuencia de G: 8
    Frecuencia de T: 4
```
python .\template_program.py ..\test\adn.seq.txt
```
### Caso de prueba 1: Secuencia con mayusculas y minisculas
+ Descripción: Verificar que el script puede contar de manera adecuada las ocurrencias de ATGC en una secuencia dada sin importar si se encuentra en mayúsculas o en minúsculas
+ Archivo con la siguiente secuencia: aaaAaaggGcTaaga
+ Resultado esperado:
Frecuencia de A: 9
Frecuencia de C: 1
Frecuencia de G: 4
Frecuencia de T: 1
```
python .\template_program.py ..\test\Lower.txt
```
### Caso de prueba 2: Comprobación de error para cuando el archivo introducido esta vacio
+ Descripción: Verificar que el script maneja correctamente los archivos estan vacios.
+ Archivo vació
+ Resultado esperado: Error: El archivo está vacío, no se puede contar los nucleótidos.
Frecuencia de A: 9
Frecuencia de C: 1
Frecuencia de G: 4
Frecuencia de T: 1
```
python .\template_program.py ..\test\empty.txt
```
### Caso de prueba 3: Comprobación de error para cuando el archivo introducido no existe
+ Descripción: Verificar que el script maneja correctamente los archivos no existen
+ Archivo no existente
+ Resultado esperado: Sorry, couldn't find the file.

```
python .\template_program.py ..\test\lol.txt
```
### Caso de prueba 4: Comprobación de error para cuando el archivo introducido contiene una secuencia con caracteres no validos
+ Descripción: Verificar que el script maneja correctamente los archivos con secuencias no validas
+ Archivo con secuencia no valida
+ Resultado esperado:Sequence contains U, it is invalid character
Sequence contains U, it is invalid character
Sequence contains U, it is invalid character
Sequence contains U, it is invalid character
Sequence contains N, it is invalid character
Sequence contains N, it is invalid character
Sequence contains N, it is invalid character
Sequence contains N, it is invalid character
Frecuencia de A: 6
Frecuencia de C: 0
Frecuencia de G: 5
Frecuencia de T: 3

```
python .\template_program.py ..\test\adn2.seq.txt
```
