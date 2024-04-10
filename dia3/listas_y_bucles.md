# Listas y Bucles


Una situación muy común en investigación es el trabajar con una gran colección de datos (secuencias de ADN, posiciones de SNPs, mediciones de expresión génica) que necesitan ser procesados de la misma manera. En este tema, aprenderemos sobre las herramientas de programación fundamentales que permitirán que nuestros programas hagan esto. Hasta ahora, hemos aprendido sobre varios tipos de datos diferentes (strings, números y objetos de archivo), todos los cuales almacenan una sola pieza de información. Cuando hemos necesitado almacenar múltiples piezas de información (por ejemplo, las tres secuencias en el ejercicio X), simplemente hemos creado más variables para contenerlas:

<br>

```python
# set the values of all the sequence variables 
seq_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG" 
seq_2 = "actgatcgacgatcgatcgatcacgact" 
seq_3 = "ACTGAC-ACTGT—ACTGTA----CATGTG" 
```

<br>

El enfoque mostró sus limitaciones al revisar el código; solo funcionaba con un pequeño número de secuencias conocidas de antemano. A medida que aumentara el número de secuencias, el código se volvería difícil de manejar, y sería imposible procesar un número desconocido de secuencias. Para abordar esto, necesitamos una nueva estructura de datos:`una lista`



Ademas hemos trabajado con scripts secuenciales con una estructura sencilla de arriba-abajo, que tiene la ventaja que hace muy facil seguir lo que hace el codigo paso a paso pero es muy ineficiente cuando analizamos muchos datos:
<br>

```python
# Set the values of all the header variables
header_1 = "ABC123"
header_2 = "DEF456"
header_3 = "HIJ789"

# Set the values of all the sequence variables
seq_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
seq_2 = "actgatcgacgatcgatcgatcacgact"
seq_3 = "ACTGAC-ACTGT—ACTGTA----CATGTG"

# Make three files to hold the output
output_1 = open(header_1 + ".fasta", "w")
output_2 = open(header_2 + ".fasta", "w")
output_3 = open(header_3 + ".fasta", "w")

# Write one sequence to each output file
output_1.write('>' + header_1 + '\n' + seq_1 + '\n')
output_2.write('>' + header_2 + '\n' + seq_2.upper() + '\n')
output_3.write('>' + header_3 + '\n' + seq_3.replace('-', '') + '\n')

# Close the output files
output_1.close()
output_2.close()
output_3.close()

```

Una vez más, solo fue posible resolver el ejercicio de esta manera porque conocíamos de antemano el número de archivos de salida que íbamos a necesitar. Al observar el código, está claro que estas tres líneas consisten básicamente en la misma instrucción que se ejecuta varias veces, con algunas variaciones leves. Esta idea de repetición con variación es increíblemente común en los problemas de programación, y Python tiene herramientas integradas para expresarla: `los bucles`.

<br>


Crear listas y recuperar elementos
--------------------------------------


**crear una lista** 


Para crear una nueva lista, colocamos varias strings o números dentro de corchetes, separados por comas:

```python
apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"] 
conserved_sites = [24, 56, 132] 
```

**Cada elemento individual en una lista se llama elemento**. Para obtener un solo elemento de la lista, escriba el nombre de la variable seguido del index del elemento que desea entre corchetes:


```python
apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"] 
conserved_sites = [24, 56, 132] 
print(apes[0]) 
first_site = conserved_sites[2] 
```

**index** 


Si queremos ir en la otra dirección, es decir, sabemos qué elemento queremos pero no sabemos el índice, podemos usar el método `index`:

```python
apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"] 
chimp_index = apes.index("Pan troglodytes") 
#chimp_index is now 1 
```

Recuerda que en Python empezamos a contar desde cero en lugar de uno, por lo que el primer elemento de una lista siempre está en el índice cero. Si damos un número negativo, Python comienza a contar desde el final de la lista en lugar de desde el principio, por lo que es fácil obtener el último elemento de una lista:

```python
last_ape = apes[-1]
```

<br>

**rangos[:]** 


¿Qué pasa si queremos obtener más de un elemento de una lista? Podemos dar una posición de inicio y de final, separadas por dos puntos, para especificar un rango de elementos:


```python
ranks = ["kingdom","phylum", "class", "order", "family"] 
lower_ranks = ranks[2:5] 
# lower ranks are class, order and family Does this look familiar? 
```

Es exactamente la misma notación que usamos para obtener substrings, y funciona exactamente de la misma manera: los números son inclusivos al principio y exclusivos al final. El hecho de que usemos la misma notación para strings y listas sugiere una relación más profunda entre los dos tipos. De hecho, **lo que hacemos al extraer subcadenas es tratar una cadena como si fuera una lista de caracteres**.


<br>


Trabajando con listas
--------------------------

**append**

Para agregar otro elemento al final de una lista existente, podemos usar el método append:

```
apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
apes.append("Pan paniscus") 
```

`append` es un método interesante porque realmente cambia la variable en la que se usa: en el ejemplo anterior, la lista de apes pasa de tener tres elementos a tener cuatro. 



**len**

Podemos obtener la longitud de una lista usando la función `len()`, al igual que hicimos para las strings:

```python
apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"] 
print("There are " + str(len(apes)) + " apes") 
apes.append("Pan paniscus") 
print("Now there are " + str(len(apes)) + " apes") 
```

La salida muestra que el número de elementos en apes realmente ha cambiado:

```python
There are 3 apes 
Now there are 4 apes 
```

Podemos concatenar dos listas de la misma manera que lo hicimos con cadenas, usando el símbolo más:

```python
apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"] 
monkeys = ["Papio ursinus", "Macaca mulatta"] 
primates = apes + monkeys
print(str(len(apes)) + " apes") 
print(str(len(monkeys)) + " monkeys") 
print(str(len(primates)) + " primates") 

```
Como podemos ver en la salida, esto no cambia ninguna de las dos listas originales, sino que crea una lista completamente nueva que contiene elementos de ambas: 


```python
3 apes 
2 monkeys 
5 primates 
```

**Reverse y sort**

Son dos métodos de lista que cambian la variable en la que se usan. Tanto `reverse` como `sort` funcionan cambiando el orden de los elementos en la lista. Si queremos imprimir una lista para ver cómo funciona esto, necesitamos usar str (como lo hicimos al imprimir números):

```python
ranks = ["kingdom","phylum", "class", "order", "family"]
print("at the start : " + str(ranks)) 
ranks.reverse()
print("after reversing : " + str(ranks)) 
ranks.sort() 
print("after sorting : " + str(ranks)) 
```

Si echamos un vistazo a la salida, podemos ver cómo cambia el orden de los elementos en la lista mediante estos dos métodos: 

```python
at the start : ['kingdom', 'phylum', 'class', 'order', 'family'] 
after reversing : ['family', 'order', 'class', 'phylum', 'kingdom'] 
after sorting : ['class', 'family', 'kingdom', 'order', 'phylum'] 
```

Por defecto, **Python ordena las cadenas alfabéticamente y los números de forma numérica ascendente.**

<br>

Creando un Bucle For
------------------------

Imaginemos que queremos tomar nuestra lista de simios: 

```python
apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"] 
```
e imprimir cada elemento en una línea separada, así:


```python
Homo sapiens is an ape 
Pan troglodytes is an ape 
Gorilla gorilla is an ape
```

Una forma de hacerlo sería simplemente imprimir cada elemento por separado::

```python
print(apes[0] + " is an ape") 
print(apes[1] + " is an ape") 
print(apes[2] + " is an ape") 
```

pero esto es muy repetitivo y depende de que sepamos el número de elementos en la lista. Lo que necesitamos es una forma de decir algo así como **"para cada elemento en la lista de simios, imprimir el elemento, seguido de las palabras 'es un simio'"**. La sintaxis de bucle de Python nos permite expresar esas instrucciones así:

```python
for ape in apes: 
	print(ape + " is an ape") 
```

Tomémonos un momento para mirar las diferentes partes de este bucle. Comenzamos escribiendo for x in y, donde y es el nombre de la lista que queremos procesar y x es el nombre que queremos usar para el elemento actual cada vez que pasa el bucle. x es solo un nombre de variable (por lo que sigue todas las reglas que ya hemos aprendido sobre los nombres de variables), pero se comporta ligeramente diferente a todas las demás variables que hemos visto hasta ahora.

En todos los ejemplos anteriores, creamos una variable y almacenamos algo en ella, y luego el valor de esa variable no cambia a menos que lo cambiemos nosotros mismos. En contraste, cuando creamos una variable para usar en un bucle, no establecemos su valor; el valor de la variable se establecerá automáticamente en cada elemento de la lista a su vez, y será diferente cada vez que pase el bucle.

Es importante destacar que la variable de bucle x solo existe dentro del bucle: se crea al comienzo de cada iteración del bucle y desaparece al final. Esto significa que una vez que el bucle ha terminado de ejecutarse por última vez, esa variable desaparece para siempre.

Esta **primera línea del bucle termina con dos puntos**, y todas **las líneas subsiguientes (solo una, en este caso) están identadas o sangradas**. Las **líneas identadas pueden comenzar con cualquier número de tabulaciones o espacios, pero todas deben estar sangradas de la misma manera**. Este patrón: una línea que termina con dos puntos, seguida de algunas líneas sangradas, es muy común en Python,  


Un grupo de líneas sangradas a menudo se llama **bloque de código**. En este caso, nos referimos al bloque sangrado como el **cuerpo del bucle**, y las líneas dentro de él se ejecutarán una vez para cada elemento en la lista.

Aquí hay un ejemplo de un bucle con un cuerpo más complicado:

```python
apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"] 
for ape in apes: 
	name_length = len(ape) 
	first_letter = ape[0] 
	print(ape + " is an ape. Its name starts with " + first_letter) 
	print("Its name has " + str(name_length) + " letters") 
```	
	
**El cuerpo del bucle** en el código anterior tiene cuatro sentencias, dos de las cuales son sentencias con la función print, por lo que cada vez que pasa el bucle obtendremos dos líneas de salida. Si observamos la salida, podemos ver las seis líneas:

```python
Homo sapiens is an ape. Its name starts with H 
Its name has 12 letters 
Pan troglodytes is an ape. Its name starts with P 
Its name has 15 letters 
Gorilla gorilla is an ape. Its name starts with G 
Its name has 15 letters 
```

¿Por qué es mejor el enfoque anterior que imprimir estas seis líneas en seis declaraciones separadas? El enfoque anterior utilizando un bucle For es mucho mas potente porque reduce la redundancia al requerir solo dos sentencias de impresión en lugar de seis escritas una a una. Además, facilita la modificación del código, ya que los cambios solo se necesitan realizar una vez en lugar de tres veces separadas. Además, al usar un bucle, no es necesario modificar el código del bucle si se agregan elementos a la lista, lo que lo hace más flexible y adaptable a diferentes cantidades de elementos en la lista.

<br>

Usar un string como una lista 
------------------

¿Podemos también usar la notación de bucle para procesar una cadena como si fuera una lista? Sí, si escribimos una declaración de bucle con una cadena en la posición donde normalmente encontraríamos una lista, Python trata cada carácter en la cadena como un elemento separado. Esto nos permite procesar muy fácilmente una cadena de un carácter a la vez:

```python
dna = "atgcat" 
for nucleotide in dna: 
    print("nucleotide is " + nucleotide)
```

En este caso, simplemente estamos imprimiendo cada carácter individual:

```python
nucleotide is  a 
nucleotide is  t
nucleotide is  g 
nucleotide is  c 
nucleotide is  a 
nucleotide is  t
```

El proceso de repetir un conjunto de instrucciones para cada elemento de una lista (o carácter en una cadena) se llama **iteración**, y a menudo hablamos de iterar sobre una `lista` o `cadena`.

<br>

Splitting a string to make a list
---------------------------------

Hasta ahora todas nuestras listas han sido escritas manualmente. Sin embargo, hay muchas funciones y métodos en Python que producen listas como salida. Uno de esos métodos que resulta particularmente interesante para los biólogos es el método `split`, que funciona con `strings`. **split toma un solo argumento, llamado delimitador**, y divide la cadena original donde vea el delimitador, produciendo una lista. Aquí tienes un ejemplo:

```python
names = "melanogaster,simulans,yakuba,ananassae" 
species = names.split(",","r") 
print(str(species))
```

Podemos ver en la salida que la cadena se ha dividido donde había una coma, dejándonos con una lista de strings:

```python
['melanogaster', 'simulans', 'yakuba', 'ananassae']
```

Una vez que hemos creado una lista de esta manera, podemos iterar sobre ella usando un **bucle for**, al igual que cualquier otra lista


<br>

Iterar sobre líneas en un archivo
---------------------------------

Otra cosa muy útil sobre la que podemos iterar es un archivo. Así como una cadena puede simular ser una lista al usar un bucle, podemos hacer lo mismo con un archivo. Cuando tratamos una cadena como una lista, cada carácter se convierte en un elemento individual, pero cuando tratamos un archivo como una lista, cada línea se convierte en un elemento individual. **Esto facilita mucho el procesamiento de un archivo línea por línea**:

```python
file = open("input.txt") 
for line in file: 
	#do something with the line
	print(line)
```

<br>


# EJERCICIOS


Ejercicio_1. Procesamiento de ADN en un archivo
----------------------------------

El archivo `input.txt` contiene varias secuencias de ADN, una por línea. Cada secuencia comienza con el mismo fragmento de 14 pares de bases, un adaptador de secuenciación que debería haber sido eliminado. Escribe un programa que 

1. recorte este adaptador y escriba las secuencias limpias en un nuevo archivo y
1. imprima la longitud de cada secuencia en la pantalla.


Ejercicio_2. Concatenación de exones de ADN genómico
----------------------------------------

El archivo `genomic_dna.txt` contiene una sección de ADN genómico, y el archivo exons.txt contiene una lista de posiciones de inicio/fin de exones. Cada exón está en una línea separada y las posiciones de inicio y fin están separadas por una coma. 

Escribe un programa que extraiga los segmentos de exones, los concatene y los escriba en un nuevo archivo.



