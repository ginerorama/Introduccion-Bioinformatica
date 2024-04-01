# Listas y Bucles

<br>
Una situación muy común en investigación con datos biologicos es tener una gran colección de datos (secuencias de ADN, posiciones de SNPs, mediciones de expresión génica) que necesitan ser procesados de la misma manera. En este tema, aprenderemos sobre las herramientas de programación fundamentales que permitirán que nuestros programas hagan esto. Hasta ahora, hemos aprendido sobre varios tipos de datos diferentes (strings, números y objetos de archivo), todos los cuales almacenan una sola pieza de información. Cuando hemos necesitado almacenar múltiples piezas de información (por ejemplo, las tres secuencias en el ejercicio X), simplemente hemos creado más variables para contenerlas:

<br>

```
# set the values of all the sequence variables 
seq_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG" 
seq_2 = "actgatcgacgatcgatcgatcacgact" 
seq_3 = "ACTGAC-ACTGT—ACTGTA----CATGTG" 
```

<br>

El enfoque mostró sus limitaciones al revisar el código; solo funcionaba con un pequeño número de secuencias conocidas de antemano. A medida que aumentara el número de secuencias, el código se volvería difícil de manejar, y sería imposible procesar un número desconocido de secuencias. Para abordar esto, necesitamos una nueva estructura de datos: `una lista`

<br>


Ademas hemos trabajado con script secuenciales con una estructura sencilla de abajo-arriba, que tiene la ventaja que hace muy facil seguir lo que hace el codigo paso a paso pero es muy ineficiente cuando analizamos muchos datos:
<br>

```
# make three files to hold the output 
output_1 = open(header_1 + ".fasta", "w") 
output_2 = open(header_2 + ".fasta", "w") 
output_3 = open(header_3 + ".fasta", "w")
```
<br>

Una vez más, solo fue posible resolver el ejercicio de esta manera porque conocíamos de antemano el número de archivos de salida que íbamos a necesitar. Al observar el código, está claro que estas tres líneas consisten básicamente en la misma instrucción que se ejecuta varias veces, con algunas variaciones leves. Esta idea de repetición con variación es increíblemente común en los problemas de programación, y Python tiene herramientas integradas para expresarla: `los bucles`.
