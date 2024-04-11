# Test Condicionales


Pruebas condicionales
---------------------
Los programas necesitan tomar decisiones
Si observamos los ejemplos y ejercicios que hemos realizado hasta ahora, algo que destaca es la falta de toma de decisiones. Hemos pasado de hacer cálculos simples en bits individuales de datos a llevar a cabo procedimientos más complicados en colecciones de datos, pero la forma en que se ha tratado cada bit de datos (una secuencia, una base, un nombre de especie, un exón) ha sido idéntica.
Sin embargo, los problemas de la vida real a menudo requieren que nuestros programas actúen como tomadores de decisiones; examinar una propiedad de algún dato y decidir qué hacer con él. En este tema, veremos cómo hacer eso utilizando **declaraciones condicionales**

Las **declaraciones condicionales** son características de Python que nos permiten construir *puntos de decisión* en nuestro código. Permiten que nuestros programas decidan qué acción tomar entre varias posibles, instrucciones como "*imprimir el nombre de la secuencia si tiene más de 300 bases*" o "*agrupar dos muestras juntas si fueron recolectadas a menos de 10 metros de distancia*".
Sin embargo, antes de poder comenzar a usar declaraciones condicionales, necesitamos entender las condiciones.

<br>

Condiciones, Verdadero y Falso
-------------------------------
Una **condición** es simplemente un fragmento de código que puede producir una respuesta verdadera (*True*) o falsa (*False*). La forma más fácil de entender cómo funcionan las condiciones en Python es probar algunos ejemplos. El siguiente ejemplo imprime el resultado de probar (o evaluar) varias condiciones diferentes, algunos ejemplos matemáticos, algunos usando métodos de cadenas y uno para probar si un valor está incluido en una lista:


```python
# igual que
print(3 == 5)
False
# mayor que
print(3 > 5)
False
# menor que
print(3 <=5)
True
# no igual 
print(5 != 3)
True
# mayor que
print(len("ATGC") > 5)
False
# mayor que
print("GAATTC".count("T") > 1)
True
# comienza con "ATG"? resultado True o False
print("ATGCTT".startswith("ATG"))
True
# acaba con TTT?
print("ATGCTT".endswith("TTT"))
False
# es mayuscula?
print("ATGCTT".isupper())
True
# es minuscula
print("ATGCTT".islower())
False
# imprime V si est en la lista
print("V" in ["V", "W", "L"])
True
```

¿qué se está imprimiendo realmente aquí? A primera vista, parece que estamos imprimiendo las cadenas "True" y "False", pero esas cadenas no aparecen en ningún lugar de nuestro código. Lo que realmente se está imprimiendo son los **valores especiales integrados que Python utiliza para representar verdadero y falso**: están en mayúsculas para que sepamos que son estos valores especiales.

Podemos demostrar que estos valores son especiales intentando imprimirlos. El siguiente código se ejecuta sin errores (nota la ausencia de comillas):

```python
print(True)
True
print(False)
False
print(True or False)
True
```


Mientras que si intentamos imprimir palabras arbitrarias sin comillas obtenemos un error:

```python
print(Hello)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Hello' is not defined
```


Ahora que ya sabemos cómo expresar pruebas condicionales, veamos qué podemos hacer con ellas.



IF statements (declaracion con IF)
-------------------------------------


Las declaraciones `if` son el tipo más simple de declaración condicional. La sintaxis es bastante sencilla de entender:


```python
expression_level = 125
if expression_level > 100:
    print("el gen está altamente expresado")
```


Escribimos la palabra **if**, seguida de una condición, y terminamos la primera línea **con dos puntos**. A continuación, hay un **bloque de líneas de código** indentadas (el cuerpo de la declaración if), que **solo se ejecutará si la condición es verdadera**. Este patrón de dos puntos más bloque indentado debería resultarte familiar de los capítulos sobre bucles y funciones.

La mayor parte del tiempo, la declaración if la usamos para probar una propiedad de alguna variable cuyo valor no conocemos en el momento en que estamos escribiendo el programa. El ejemplo anterior es obviamente inútil, ¡ya que el valor de la variable **expression_level** no va a cambiar!

Aquí tienes un ejemplo ligeramente más interesante: vamos a definir una lista de nombres de acceso a genes e imprimir solo aquellos que comienzan con "a":

```python
#imprimir solo los que comienzan por a
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'ad727']
for accession in accs:
    if accession.startswith('a'):
       print(accession)
       
#output       
ab56
ay93
ap97
ad727
```

las líneas de código dentro del bucle están indentadas (como hemos visto antes), pero la línea de código dentro de la declaración if está indentada dos veces, una vez para el **bucle for** y otra vez para el **if**. Observar múltiples niveles de indentación en Pythones muy común una vez que empezamos a trabajar con programas más grandes. 

Python está bastante preparado para tener tantos niveles de indentación como sea necesario, pero tendrás que llevar un seguimiento cuidadoso de qué líneas de código pertenecen a qué nivel. Si te encuentras escribiendo un trozo de código que requiere más de tres niveles de indentación, generalmente es una indicación de que ese trozo de código debería convertirse en una función.



else statements
-----------------

El **else statement** está estrechamente relacionado con el **if statement**. Los ejemplos anteriores utilizan un tipo de toma de decisiones de sí/no: ¿deberíamos imprimir el número de acceso al gen o no? A menudo necesitamos un tipo de decisión de "o esto, o lo otro", donde tenemos dos acciones posibles a tomar. Para hacer esto, podemos agregar la declaracion **else** después del final del cuerpo de un **if statement**:

```python
expression_level = 125
if expression_level > 100:
   print("el gen está altamente expresado")
else:
    print("el gen está bajo expresado")
```

El *else statement* no tiene ninguna condición propia; más bien, el cuerpo del else statement se ejecuta cuando el if statement al que está adjunto no se ejecuta.

Aquí hay un ejemplo que utiliza if y else para dividir una lista de nombres de acceso en dos archivos diferentes: los nombres de acceso que comienzan con "a" van al primer archivo y todos los demás nombres de acceso van al segundo archivo.    

```python
#open files
file1 = open("one.txt", "w")
file2 = open("two.txt", "w")

# accession list
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']

# bucle for y declaracion condicional if/else
for accession in accs:
    if accession.startswith('a'):
       file1.write(accession + "\n")  
    else:
       file2.write(accession + "\n")
```

<br>

elif statements
-----------------

¿Qué pasa si tenemos más de dos posibles opciones? Por ejemplo, digamos que queremos tres archivos de nombres de acceso: 

1. aquellos que comienzan con "a" 
1. aquellos que comienzan con "b" 
1. todos los demás. 

Python tiene la instrucción **elif**, que fusiona **else y if** y nos permite tener mas opciones de decision:

```python
file1 = open("one.txt", "w")
file2 = open("two.txt", "w")
file3 = open("three.txt", "w")
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for accession in accs:
    if accession.startswith('a'):
       file1.write(accession + "\n")
    elif accession.startswith('b'):
       file2.write(accession + "\n")
    else:
       file3.write(accession + "\n")
```       

Si se nos queda corto, podemos añadir muchas mas ramas de decisión sin necesidar de aumentar el nivel de identaciones:

```python
for accession in accs:
    if accession.startswith('a'):
       file1.write(accession + "\n")
    elif accession.startswith('b'):
       file2.write(accession + "\n")
    elif accession.startswith('c'):
       file3.write(accession + "\n")
    elif accession.startswith('d'):
       file4.write(accession + "\n")
    elif accession.startswith('e'):
       file5.write(accession + "\n")
    else:
       file6.write(accession + "\n")
```

<br>

Bucle While
--------------       

El bucle while nos permite realizar un bucle similar al for pero en este caso solo se ejecuta mientras se mantenga una determinada condición (mientras la condición sea True).Por ejemplo, aquí hay un fragmento de código que incrementa una variable de conteo en uno cada vez que se ejecuta el bucle, deteniéndose cuando la variable de conteo alcanza diez:

```python
count = 0
while count < 10:
    print(count)
    count = count + 1
```

Dado que los **bucles for** en Python son muy utiles, los bucles while se utilizan mucho menos frecuentemente que en otros lenguajes.



Operadores booleanos (and, or & not)
--------------------------------------

La utilizacion de operadores booleanos junto con paréntesis cuando sea necesario nor permite construir condiciones mas complejas pero con estructuras mas sencillas además de economizar el código .

Por ejemplo, ¿Qué pasaría si quisiéramos expresar una condición que estuviera compuesta por varias partes? Imagina que queremos recorrer nuestra lista de accesiones e imprimir solo aquellas que comienzan con "a" y terminan con "3". Podríamos usar dos instrucciones if anidadas:


```python
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for accession in accs:
    if accession.startswith('a'):
       if accession.endswith('3'):
          print(accession)
```
<br>

pero esto introduce un nivel de indentación adicional innecesario. Una mejor manera es unir las dos condiciones con `and` para formar una expresión compleja:

```python
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for accession in accs:
    if accession.startswith('a') and accession.endswith('3'):
       print(accession)
```
<br>

Incluso podemos unir condiciones complejas para hacer condiciones aun mas complejas. Aquí hay un ejemplo que imprime accessions si comienzan con "a" o "b" y terminan con "4" utilizando la instruccion `or`:

```python
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for acc in accs:
    if ((acc.startswith('a') or acc.startswith('b')) and acc.endswith('4'):
       print(acc)
```

<br>

Observa cómo tenemos que incluir paréntesis en el ejemplo anterior para evitar ambigüedad. Finalmente, podemos negar cualquier tipo de condición anteponiendo la palabra `not`. Este ejemplo imprimirá accessions que comiencen con "a" y no terminen con 6:


```python
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for acc in accs:
    if acc.startswith('a') and not acc.endswith('6'):
       print(acc)
```


<br>


# Ejercicios

El archivo `data.csv` contiene algunos datos inventados para varios genes. Cada línea contiene los siguientes campos para un solo gen en este orden: nombre de la especie, secuencia, nombre del gen, nivel de expresión. Los campos están separados por comas (de ahí el nombre del archivo: csv significa Comma Separated Values). Piensa en esto como una representación de una tabla en una hoja de cálculo: cada línea es una fila, y cada campo en una línea es una columna. Los ejercicios planteados a continuacion usan este archivo:


**Ejercicio 1. Imprime los nombres** de los genes para todos los genes que pertenezcan a *Drosophila melanogaster* o *Drosophila simulans*.

**Ejercicio 2. Rango de longitud.** Imprime los nombres de los genes para todos los genes que tengan entre 90 y 110 bases de longitud.

**Ejercicio 3. Contenido de AT.** Imprime los nombres de los genes para todos los genes cuyo contenido de AT sea menor que 0.5 y cuyo nivel de expresión sea mayor que 200.

**Ejercicio 4. Condición compleja.** Imprime los nombres de los genes para todos los genes cuyo nombre comience con "k" o "h", excepto aquellos que pertenezcan a Drosophila melanogaster.

**Ejercicio 5. Alto, bajo, medio.** Para cada gen, imprime un mensaje que dé el nombre del gen y diga si su contenido de AT es alto (mayor que 0.65), bajo (menor que 0.45) o medio (entre 0.45 y 0.65).






