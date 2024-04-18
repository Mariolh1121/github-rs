# Nombre del Proyecto

Fecha: 08/01/2024

**Participantes**:

- Mario Limón <email:mariolh@lcg.unam.mx>

## Descripción del Problema

Contar la frecuencia de ATCG de un archivo 

## Especificación de Requisitos

+ El programa debería de acumular la frecuencia de "A", "T", "C" Y "G".
+ El programa debe aceptar un archivo de una secuencia de DNA.
+ Los nucleotidos contados deben pasar como un argumento opcional de la línea de comandos.

## Análisis y Diseño
+ El programa será desarrollado en el lenguaje de programación Python para asegurar una amplia compatibilidad y facilidad de uso.

+ La lectura de los argumentos de línea de comandos debería ser implementada utilizando la biblioteca argparse para Python para permitir interfaces de línea de comandos flexibles y amigables para el usuario.

+ El código desarrollado para el programa debería adherirse a los estándares PEP8 para el estilo de código de Python. Esto mejora la legibilidad y mantenibilidad del código.

#### Caso de uso: 

```
         +---------------+
         |   User        |
         +-------+-------+
                 |
                 | 1. Archivo se secuencai
                 v
         +-------+-------+
         |   count-atgc  |
         |               |
         |               |
         |               |
         +---------------+
```

- **Actor**: Usuario
- **Descripción**:
  El código toma un archvivo y devuelve un conteo de la cantidad de nucleotidos que contiene la cádena de DNA, etc 
- **Flujo principal**:
  + El usuario abre el archivo después de ejectuar el programa a traves de la línea de comando
  + El usuario puede proporcionar el nucleotido que desea contar (opcional)
  + El programa lee el archivo y lo guarda en una variable
  + El programa cuenta la ocurrencia de ATCG
- **Flujos alternativos**:
  + El archivo no exíste o no se puede leer -> El sistema manda error
  + No hay nucleotidos dentro del archivo -> El sistema por default intenta contar la ocurrencia de estos nucleotidos.
  + El archivo esta vació -> EL sistema manda un error en automatico
