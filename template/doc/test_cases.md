# Casos de prueba o escenarios

Este documento describe los casos de prueba para el script de Python desarrollado para calcular la suma de números de un archivo. El objetivo de estas pruebas es validar y garantizar que el script funciona correctamente y cumple con las especificaciones.

Los casos de prueba se han diseñado teniendo en cuenta las diferentes funcionalidades del script así como los posibles errores que puedan surgir.

El script está diseñado para leer números desde un archivo proporcionado como entrada, con la capacidad de manejar tanto números enteros como de punto flotante. La suma de estos números se calcula y se imprime en el formato especificado. El script también está diseñado para manejar errores como la ausencia del archivo de entrada y datos de entrada que no son números de base 10.

Los casos de prueba cubren las características clave del programa y prueban varias condiciones para garantizar la robustez y fiabilidad del script.

La ejecución exitosa de estos casos de prueba asegura que el script está listo para su uso y puede manejar diferentes condiciones de entrada y situaciones de error.

A continuación, presentamos los detalles de los casos de prueba. Cada caso de prueba incluye una descripción del caso de prueba, los datos de entrada utilizados y el resultado esperado.
    
    
### Caso de prueba 1: Comprobación de la suma de números enteros

- Descripción: Verificar que el script puede sumar correctamente números enteros.
- Datos de entrada: Archivo con los números "10", "5".
- Resultado esperado: 15


### Caso de prueba 2: Comprobación de la suma de números decimales

- Descripción: Verificar que el script puede sumar correctamente números decimales.
- Datos de entrada: Archivo con los números "5.6", "2.4".
- Resultado esperado: 8.0


### Caso de prueba 3: Comprobación de error para datos no numéricos
- Descripción: Verificar que el script maneja correctamente los datos que no son números.
- Datos de entrada: Archivo con el texto "five", "ten".
- Resultado esperado: Error, introducir números de base 10


### Caso de prueba 4: Comprobación de error para archivo no existente
- Descripción: Verificar que el script maneja correctamente los archivos no existentes.
- Datos de entrada: Ruta a un archivo que no existe.
- Resultado esperado: Error, archivo no encontrado
        
        