
manipulando archivos
---------------------------------

A la hora de manipular archivos en python usaremos dos funciones que son esenciales para llevar a cabo esta tarea. La función `open()` y la funcion `read()`.

imaginemos el siguiente archivo de texto denominado dna.fasta:
```
>seq1
atagatagatagat
```
si quisieramos abrir el archivo, guardar en una variable su contenido e imprimir dicha variable, podríamos hacer el siguiente script __read_file.py__:

```
#almacenamos en una variable tipo string el path del archivo
file = "dna.txt"

#ejecutamos la función open para abrir el archivo y almacenarlo en la variable open_file 
open_file = open(file,"r")

#ahora leemos el contenido del archivo y lo almacenamos en file_content
file_content = open_file.read()

#finalmente imprimimos el contenido del archivo en pantalla
print(file_content)
```

si ahora ejecutamos el script:

```
$ python read_file.py
>seq1
atagatagatagat
```

La función `open(archivo, opciones)`, vemos que tiene dos argumentos, el primero es el archivo sobre el que vamos a operar y el segundo argumento es la acción que vamos a hacer sobre el archivo. En nuestro caso hemos usar `r` read para leer un arhivo, pero mas adelante veremos que podemos usar la opción `w` write para crear y escribir un archivo. Esta función es el eje angular de Python para leer o escribir archivos. 

importante `read()` es un método, y como ya hemos comentado antes, los métodos son funciones específicas para cierto tipo de objetos. En este caso la función `read()` solo puede usarse con objetos que sean archivos. Si lo intentamos usar con un string obtendremos un error, veamoslo directamente en python (recuerda para entrar en python solo tienes que escribir __python__ en terminal y para salir escribir __exit()__:

```
>> my_dna = "atgc"
>> fna_content = my_dna.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'read'
```

<br />

archivo no encontrado
---------------------
imaginemos que intentamos arbir un archivo directamente en el prompt de python y nos ocurre lo siguiente:
```
>> my_file = open("archivo.txt","r")
IOError: [Errno 2] No such file or directory: 'archivo.txt'
```
Esto quiere decir que o bien no hemos escrito bien el archivo, o que no esta en la ubicación que hemos escrito. Si traducimos el mesaje pone __Input/Output Error: Error numero 2 No existe ese archivo o directory : archivo.txt__ . Como vemos los mensajes de Python son realmente informativos y útiles.

<br />

La función write() y la escritura de archivos
--------------------------------------------
Crear y almacenar datos en un archivo de texto es realmente facil en Python utilizando las funciones `open()` y el método `write()`. Utilizaremos `open()` para crear un archivo y permitir su escritura, para esta tarea `open()` puede tomar como segundo argumento dos opciones:

-`w` write para escribir un archivo. Crea un archivo nuevo y lo escribe.

-`a` append para añadir lineas o strings al final de un archivo existente

Recuerda que `r` lo usaremos para abrir y leer archivos
```
my_file = open("out.txt", "w") #creamos un archivo en modo escritura
my_file.write("Hello world") # utilizamos el metodo write() para escribir en un archivo
```
Luego utilizaremos el método `write()` que permite insertar o escribir texto en un archivo que haya sido creado con la función `open()` en modo w o a . Write funciona exactamente igual que print(), solo que en vez de imprimir el texto en terminal lo va a escribir en un archivo de texto. Eso si al usar `write()` trendremos que especificar cuando escribamos un string si queremos añadir un salto de linea o no `\n`. 

veamos un ejemplo para entender todo esto mejor con el script __write_python.py__ :
```
my_file = open("out.txt", "w") #creamos un archivo en modo escritura

# write "TTGC"
my_file.write("ATGC".replace('A', 'T'))

# write "atgc"
my_file.write("ATGC".lower())

seq1 = "atgc"
seq2 = "tgggc"
# write contents of my_variable
my_file.write(seq1+seq2)
```
veamos el archivo out.txt
```
~ cat out.txt
TTGCatgcatgctgggc
```
como podemos ver cada vez que hemos ejecuta `write()` en el archivo hemos concatenado, los strings. Esto ocurre porque no hemos separado cada string que ha entrado en el archivo con un new line `\n`. 
```
my_file = open("out.txt", "w") #creamos un archivo en modo escritura

# write "TTGC"
my_file.write("ATGC\n".replace('A', 'T')) # introducimos en el string el caracte new line

# write "atgc"
my_file.write("ATGC\n".lower()) # introducimos en el string el caracte new line

seq1 = "atgc"
seq2 = "tgggc"
# write contents of my_variable
my_file.write(seq1+seq2+"\n")
```
si ahora corremos el script:
```
~ cat out.txt
TTGC
atgc
atgctgggc
``` 

<br />

cerrando los archivos
----------------------
No vamos a entrar en detalle, pero en Python es importante cerrar los archivos una vez hemos terminado de manipularlos, es importante sobre todo por cuestiones de memoria. Para cerrar una archivo lo unico que tenemos que hacer es usar el metodo `close()`. Siguiendo con el ejemplo anterior solo tendríamos que añadir al final del script __write_python.py__:

```
my_file = open("out.txt", "w") #creamos un archivo en modo escritura

#write "TTGC"
my_file.write("ATGC".replace('A', 'T'))

#write "atgc"
my_file.write("ATGC".lower())

seq1 = "atgc"
seq2 = "tgggc"
#write contents of my_variable
my_file.write(seq1+seq2)

#close the file
my_file.close()
```



# Ejercicios 

### Ejercicio_1. División de ADN genómico

Usando el archivo llamado genomic_dna.txt; contiene el mismo fragmento de ADN genómico que estábamos utilizando en el ejercicio final del tema anterior. Escribe un programa que divida el ADN genómico en partes codificantes y no codificantes, y escriba estas secuencias en dos archivos separados.

<br>

### Ejercicio_2. Escribiendo un archivo FASTA

El formato de archivo FASTA es un formato comúnmente utilizado para secuencias de ADN y proteínas. Una secuencia única en formato FASTA se ve así:

```
 >sequence_name
 ATCGACTGATCGATCGTACGAT
```
Donde sequence_name es un encabezado que describe la secuencia (el símbolo mayor que indica el inicio de la línea de encabezado). A menudo, el encabezado contiene un número de acceso que se relaciona con el registro de la secuencia en una base de datos pública de secuencias. Un solo archivo FASTA puede contener múltiples secuencias, como esta:

```
>sequence_one
 ATCGATCGATCGATCGAT
 >sequence_two
 ACTAGCTAGCTAGCATCG
 >sequence_three
 ACTGCATCGATCGTACCT    
```

Escribe un programa que cree un archivo FASTA para las siguientes tres secuencias; asegúrate de que todas las secuencias estén en mayúsculas y solo contengan las bases A, T, G y C.

<br>

| Sequence header | DNA sequence                           |
|-----------------|----------------------------------------|
| ABC123          | ATCGTACGATCGATCGATCGCTAGACGTATCG      |
| DEF456          | ACTGATCGACGATCGATCGATCACGACT           |
| HIJ789          | ACTGAC-ACTGT--ACTGTA----CATGTG        |

<br>

### Ejercicio_3. Escribe múltiples archivos FASTA
Utiliza los datos del ejercicio anterior, pero en lugar de crear un solo archivo FASTA, crea tres nuevos archivos FASTA, uno por cada secuencia. Los nombres de los archivos FASTA deben ser iguales a los nombres de encabezado de las secuencias, con la extensión .fasta.

