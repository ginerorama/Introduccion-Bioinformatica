# Diccionarios


Creando un diccionario
----------------------

la sintaxis para crear un diccionario es similar al de crear una lista, pero usamos llaves en lugar de corchetes. Cada par de datos consiste en una clave (*Key*) y un valor (*value*), y ambos configuran un elemento del diccionario. Cuando almacenamos elementos en un diccionario, los separamos con comas. Dentro de un elemento individual, separamos la clave y el valor con dos puntos. Aquí hay un fragmento de código que crea un diccionario de enzimas de restricción (usando datos del capítulo anterior) con tres elementos:

```python
enzymes = { 'EcoRI':r'GAATTC', 'AvaII':r'GG(A|T)CC', 'BisI':'GC[ATGC]GC' }
```
<br>
En este caso, las claves y los valores son ambos strings. Podemos representar y escribir el diccionario en varias lineas, lo que facilita su interpretación y no afecta al código en absoluto.

```python
enzymes = {
   'EcoRI' : r'GAATTC',
   'AvaII' : r'GG(A|T)CC',
   'BisI'  : r'GC[ATGC]GC'
}
```

para buscar el motivo de una enzima en particular, escribimos el nombre del diccionario, seguido de la clave entre corchetes:

```python
print(enzymes['BisI'])
```
El código se parece mucho a usar una lista, pero en lugar de dar el índice del elemento que queremos, estamos dando la clave para el valor que queremos recuperar.

Los diccionarios son una forma muy útil de almacenar datos, pero vienen con algunas restricciones:

1. las **claves** solo pueden ser **strings** o **números**, por lo que no podemos, por ejemplo, crear un diccionario donde las claves sean objetos de archivo. 
1. las **claves** deben ser **únicas**: no podemos almacenar múltiples valores para la misma clave
1. Los **valores** pueden ser de **cualquier tipo de dato** que queramos. 


En programas reales, es relativamente raro que queramos crear un diccionario todo de una vez como en el ejemplo anterior. A menudo, querremos crear un diccionario vacío y luego agregar pares de clave/valor a él.

Aquí tienes un fragmento de código que almacena los datos de las enzimas de restricción uno por uno en un diccionario:

```python
enzymes = {}
enzymes['EcoRI'] = r'GAATTC'
enzymes['AvaII'] =  r'GG(A|T)CC'
enzymes['BisI'] =  r'GC[ATGC]GC'
```
<br>

Podemos eliminar una clave de un diccionario usando el método **pop()**. pop devuelve el valor y elimina la clave al mismo tiempo:

```python
enzymes = {
   'EcoRI' : r'GAATTC',
   'AvaII' : r'GG(A|T)CC',
   'BisI'  : r'GC[ATGC]GC'
}
# Eliminar la enzima EcoRI del diccionario
enzymes.pop('EcoRI')
print(enzymes)

enzymes = {'AvaII':r'GG(A|T)CC', 'BisI':'GC[ATGC]GC' }
```

imaginemos un script que realice un conteo de todos los tripeletes de nucleotidos en una secuencia de ADN y lo imprima en pantalla, para ello necesitariamos un diccionario:

```python
dna = "AATGATCGATCGTACGCTGA"
counts = {}
for base1 in ['A', 'T', 'G', 'C']:
    for base2 in ['A', 'T', 'G', 'C']:
       for base3 in ['A', 'T', 'G', 'C']:
           trinucleotide = base1 + base2 + base3
           count = dna.count(trinucleotide)
           counts[trinucleotide] = count
print(counts)
```

Podemos ver en la salida que los trinucleótidos y sus conteos están almacenados juntos en una variable.

```python
{'ACC': 0, 'ATG': 1, 'AAG': 0, 'AAA': 0, 'ATC': 2, 'AAC': 0, 'ATA': 0,
'AGG': 0, 'CCT': 0, 'CTC': 0, 'AGC': 0, 'ACA': 0, 'AGA': 0, 'CAT': 0,
'AAT': 1, 'ATT': 0, 'CTG': 1, 'CTA': 0, 'ACT': 0, 'CAC': 0, 'ACG': 1,
'CAA': 0, 'AGT': 0, 'CAG': 0, 'CCG': 0, 'CCC': 0, 'CTT': 0, 'TAT': 0,
'GGT': 0, 'TGT': 0, 'CGA': 1, 'CCA': 0, 'TCT': 0, 'GAT': 2, 'CGG': 0,
'TTT': 0, 'TGC': 0, 'GGG': 0, 'TAG': 0, 'GGA': 0, 'TAA': 0, 'GGC': 0,
'TAC': 1, 'TTC': 0, 'TCG': 2, 'TTA': 0, 'TTG': 0, 'TCC': 0, 'GAA': 0,
'TGG': 0, 'GCA': 0, 'GTA': 1, 'GCC': 0, 'GTC': 0, 'GCG': 0, 'GTG': 0,
'GAG': 0, 'GTT': 0, 'GCT': 1, 'TGA': 2, 'GAC': 0, 'CGT': 1, 'TCA': 0,
'CGC': 1}
```
ahora si queremos obtener el valor de un triplete en concreto solo tenemos que llamar al diccionario utilizando en la clave el trinucelotido correspondiente, por ejemplo 'ACG':

```python
print(counts['ACG'])
1
```

Un problema que tiene nustro diccionario es que tiene muchos ceros, ¿como podríamos quedarnos solo con aquellos tripletes que estén presentes al menos una vez en la secuencia de ADN?:

```python
dna = "AATGATCGATCGTACGCTGA"
counts = {}
for base1 in ['A', 'T', 'G', 'C']:
    for base2 in ['A', 'T', 'G', 'C']:
       for base3 in ['A', 'T', 'G', 'C']:
           trinucleotide = base1 + base2 + base3
           count = dna.count(trinucleotide)
           if count > 0:
              counts[trinucleotide] = count
print(counts)
```

Cuando observamos la salida del código anterior, podemos ver que la cantidad de datos que estamos almacenando es mucho menor:

```python
{'ATG': 1, 'ACG': 1, 'ATC': 2, 'GTA': 1, 'CTG': 1, 'CGC': 1, 'GAT': 2,
'CGA': 1, 'AAT': 1, 'TGA': 2, 'GCT': 1, 'TAC': 1, 'TCG': 2, 'CGT': 1}
```
Ahora tenemos un nuevo problema con el que lidiar. Buscar el recuento para un trinucleótido dado funciona bien cuando el recuento es positivo, ¿pero que pasa si el recuento es cero?, dicho trinucleotido no está en el diccionario:

```python
print(counts['AAA'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'AAA'
```

obtendremos un **KeyError**.

¿Como podemos solucionar esto?. Podemos verificar la existencia de una clave en un diccionario (así como podemos verificar la existencia de un elemento en una lista) y solo intentar recuperarlo una vez que sepamos que existe:

```python
if 'AAA' in counts:
    print(counts('AAA'))
```

Iterar sobre un diccionario
---------------------------

*metodo Keys e items.*

**Iterar sobre claves (método Keys)**
Cuando se usa en un diccionario, el método keys devuelve una lista de todas las claves en el diccionario:

```python
print(counts.keys())

['ATG', 'ACG', 'ATC', 'GTA', 'CTG', 'CGC', 'GAT', 'CGA', 'AAT', 'TGA',
'GCT', 'TAC', 'TCG', 'CGT']
```

usando el metodo Key es muy facil iterar sobre el diccioario usando las claves:
```python
for trinucleotide in counts.keys():
    if counts[trinucleotide] == 2:
       print(trinucleotide)
       
ATC
GAT
TGA
TCG    
```


**Iterar sobre elementos (items)**

En el código de ejemplo anterior, lo primero que necesitamos hacer dentro del bucle es buscar el valor para la clave actual. Este es un patrón muy común al iterar sobre diccionarios, tan común, de hecho, que Python tiene una abreviatura especial para ello. En lugar de hacer esto:

```python
for key in my_dict.keys():
	value = my_dict[key]
	# hacer algo con la clave y el valor
```

Podemos usar el método items para iterar sobre pares de datos, en lugar de solo claves:

```python
for key, value in my_dict.items():
	#hacer algo con la clave y el valor
```


El método items hace algo ligeramente diferente a lo visto hasta ahora; en lugar de devolver un solo valor o una lista de valores, devuelve una lista de pares de valores. Por eso tenemos que dar dos nombres de variables al principio del bucle. Así es como podemos usar el método items para procesar nuestro diccionario de recuentos de trinucleótidos como antes:

```python
for trinucleotide, count in counts.items():
    if count == 2:
       print(trinucleotide)
```

Este método generalmente es preferido para iterar sobre elementos en un diccionario, ya que el codigo es mas claro y conciso.
