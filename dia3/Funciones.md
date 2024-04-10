# Creando Funciones

¿Por qué queremos escribir nuestras propias funciones? Echemos un vistazo al primer ejercicio ejercicio que hemos hecho en este curso de Python donde tuvimos que escribir un programa para calcular el contenido de AT de una secuencia de ADN. Recordemos el código:

```python
my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
length = len(my_dna)
a_count = my_dna.count('A')
t_count = my_dna.count('T')
at_content = (a_count + t_count) / length
print("El contenido de AT es " + str(at_content))
```

Si descartamos la primera línea (cuya función es almacenar la secuencia de entrada) y la última línea (cuya función es imprimir el resultado), podemos ver que se necesitan cuatro líneas de código para calcular el contenido de AT. Esto significa que en cada lugar de nuestro código donde queramos calcular el contenido de AT de una secuencia, necesitamos estas mismas cuatro líneas, y tenemos que asegurarnos de copiarlas exactamente, sin cometer errores. Sería mucho más sencillo si Python tuviese una función integrada (llamémosla `get_at_content`) para calcular el contenido de AT. Si ese fuera el caso, podríamos simplemente ejecutar `get_at_content` de la misma manera que ejecutamos `print`, `len` o `open`. Aunque, lamentablemente, Python no tiene una función integrada como esa, tiene algo muy parecido: una forma para que nosotros creemos nuestras propias funciones. Crear nuestra propia función para llevar a cabo una tarea en particular tiene muchos beneficios. Nos permite reutilizar el mismo código muchas veces dentro de un programa sin tener que copiarlo cada vez. Además, si descubrimos que tenemos que hacer un cambio en el código, solo tenemos que hacerlo en un solo lugar. Dividir nuestro código en funciones también nos permite abordar problemas más grandes, ya que podemos trabajar en diferentes partes del código de manera independiente. También podemos reutilizar el código en varios programas. 

**Definir una función.**  

Vamos a crear nuestra función get_at_content. Antes de comenzar a escribir, necesitamos averiguar cuáles serán las entradas (el número y tipos de argumentos de la función) y las salidas (el tipo del valor de retorno). Para esta función, eso parece bastante obvio: la entrada va a ser una única secuencia de ADN, y la salida va a ser un número decimal. Para traducir esto a términos de Python: la función tomará un solo argumento de tipo cadena, y devolverá un valor de tipo número. Aquí está el código:

```python
def get_at_content(dna):
    length = len(dna)
    a_count = dna.count('A')
    t_count = dna.count('T')
    at_content = (a_count + t_count) / length
    return at_content
```

Recordatorio: si estás utilizando Python 2 en lugar de Python 3, incluye esta línea al principio de tu programa:

```python
from __future__ import division
```
La primera línea de la definición de la función contiene varios elementos diferentes. Comenzamos con la palabra def, que es la abreviatura de define (escribir una función se llama definirla). Después de eso, escribimos el nombre de la función, seguido de los nombres de las variables de argumento entre paréntesis. Tal como vimos antes con variables normales, el nombre de la función y los nombres de los argumentos son arbitrarios; podemos usar lo que queramos. 
La primera línea termina con dos puntos, al igual que la primera línea de los bucles que vimos en el capítulo anterior. Y al igual que los bucles, esta línea es seguida por un bloque de líneas indentadas, el cuerpo de la función. El cuerpo de la función puede tener tantas líneas de código como queramos, siempre y cuando todas tengan la misma indentación. Dentro del cuerpo de la función, podemos hacer referencia a los argumentos usando los nombres de las variables de la primera línea. En este caso, la variable `dna` se refiere a la secuencia que se pasó como argumento a la función. 
La última línea de la función hace que devuelva el contenido de AT que se calculó en el cuerpo de la función. Para devolver una función, simplemente escribimos `return` seguido del valor que la función debería producir. 
Hay un par de cosas importantes que tener en cuenta al escribir funciones. En primer lugar, necesitamos hacer una clara distinción entre definir una función y ejecutarla (nos referimos a ejecutar una función como llamarla). El código que hemos escrito anteriormente no hará que suceda nada cuando lo ejecutemos, porque en realidad no le hemos pedido a Python que ejecute la función `get_at_content`(); simplemente hemos definido qué es. El código en la función no se ejecutará hasta que llamemos a la función de esta manera:

```python
get_at_content("ATGACTGGACCA")
```

Sin embargo, si simplemente llamamos a la función de esa manera, entonces el contenido de AT desaparecerá una vez que se haya calculado. Para usar la función para hacer algo útil, debemos almacenar el resultado en una variable: 

```python
at_content = get_at_content("ATGACTGGACCA")
```
 O usarlo directamente:
 
```python
print("AT content is " + str(get_at_content("ATGACTGGACCA")))
```
Segundo, es importante entender que la variable de argumento dna no tiene ningún valor particular cuando se define la función. En cambio, su trabajo es contener cualquier valor que se le dé como argumento cuando se llama a la función. De esta manera, es análogo a las variables de bucle que vimos en el capítulo anterior: las variables de bucle contienen un valor diferente cada vez que se ejecuta el bucle, y las variables de argumento de función contienen un valor diferente cada vez que se llama a la función. Finalmente, ten en cuenta que las mismas reglas de alcance que se aplicaron a los bucles también se aplican a las funciones; cualquier variable que creemos como parte de la función solo existe dentro de la función y no se puede acceder desde fuera. Si intentamos usar una variable que se crea dentro de la función desde afuera:

```python
Copy code
def get_at_content(dna):
    length = len(dna)
    a_count = dna.count('A')
    t_count = dna.count('T')
    at_content = (a_count + t_count) / length
    return at_content

print(a_count)
```

Obtendremos un error: 
```python
NameError: name 'a_count' is not defined
```

**Llamando y mejorando nuestra función.**

Escribamos un pequeño programa que utilice nuestra nueva función para ver cómo funciona. Probaremos tanto almacenar el resultado en una variable antes de imprimirlo (líneas 8 y 9) como imprimirlo directamente (líneas 10 y 11):

```python
Copy code
def get_at_content(dna):
    length = len(dna)
    a_count = dna.count('A')
    t_count = dna.count('T')
    at_content = (a_count + t_count) / length
    return at_content

my_at_content = get_at_content("ATGCGCGATCGATCGAATCG")
print(str(my_at_content))
print(get_at_content("ATGCATGCAACTGTAGC"))
print(get_at_content("aactgtagctagctagcagcgta"))

```

Al observar la salida, podemos ver que la primera llamada a la función funciona bien: el contenido de AT se calcula como 0.45, se almacena en la variable my_at_content y luego se imprime. Sin embargo, la salida para las siguientes dos llamadas no es tan buena. La llamada en la línea 10 produce un número con demasiadas cifras después del punto decimal, y la llamada en la línea 11, con la secuencia de entrada en minúsculas, da un resultado de 0.0, que definitivamente no es correcto:

```
0.45
0.5294117647058824
0.0
```

Arreglaremos estos problemas haciendo un par de cambios en la función `get_at_content`. Podemos agregar un paso de redondeo para limitar el número de cifras significativas en el resultado. Python tiene una función de redondeo integrada que toma dos argumentos: el número que queremos redondear y el número de cifras significativas. Llamaremos a la función `round()` en el resultado antes de devolverlo.Y podemos solucionar el problema de las minúsculas convirtiendo la secuencia de entrada a mayúsculas antes de comenzar el cálculo. Aquí está la nueva versión de la función, con las mismas tres llamadas a la función:"


"Corregiremos estos problemas haciendo un par de cambios en la función get_at_content. Podemos agregar un paso de redondeo para limitar el número de cifras significativas en el resultado. Python tiene una función integrada llamada round que toma dos argumentos: el número que queremos redondear y el número de cifras significativas. Llamaremos a la función round en el resultado antes de devolverlo. Y podemos solucionar el problema de las minúsculas convirtiendo la secuencia de entrada a mayúsculas antes de comenzar el cálculo. Aquí está la nueva versión de la función, con las mismas tres llamadas a la función:"

```python
def get_at_content(dna):
    length = len(dna)
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    at_content = (a_count + t_count) / length
    return round(at_content, 2)

my_at_content = get_at_content("ATGCGCGATCGATCGAATCG")
print(str(my_at_content))
print(get_at_content("ATGCATGCAACTGTAGC"))
print(get_at_content("aactgtagctagctagcagcgta"))
```

Y ahora la salida es justo como queremos: 

```
0.45 
0.53 
0.52 
```

Sin embargo, podemos mejorar aún más la función: ¿por qué no permitir que se llame con el número de cifras significativas como argumento? En el código anterior, hemos elegido dos cifras significativas, pero puede haber situaciones donde queramos ver más. Agregar el segundo argumento es fácil; simplemente lo añadimos a la lista de variables de argumento en la primera línea de la definición de la función, y luego usamos la nueva variable de argumento en la llamada a `round()`. Añadiremos algunas llamadas a la nueva versión de la función con diferentes argumentos para comprobar que funciona:

```python
def get_at_content(dna, sig_figs):
    length = len(dna)
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    at_content = (a_count + t_count) / length
    return round(at_content, sig_figs)

test_dna = "ATGCATGCAACTGTAGC"
print(get_at_content(test_dna, 1))
print(get_at_content(test_dna, 2))
print(get_at_content(test_dna, 3))
```

La salida confirma que el redondeo funciona como se pretendía:

```
0.5
0.53
0.529
```

**Encapsulación con funciones**

Detengámonos por un momento y consideremos lo que sucedió en la sección anterior. Escribimos una función y luego escribimos algún código que usaba esa función. En el proceso de escribir el código que usaba la función, descubrimos un par de problemas con nuestra definición original de la función. **Luego pudimos volver atrás y cambiar la definición de la función, sin tener que hacer ningún cambio en el código que usaba la función.**
He escrito esa última frase en negrita, porque es increíblemente importante. No es una exageración decir que entender las implicaciones de esa oración es la clave para poder escribir programas más grandes y útiles. La razón por la que es tan importante es que describe un fenómeno de programación que llamamos *encapsulación*.
<br>

La encapsulación simplemente significa dividir un programa complejo en pequeñas partes en las que podemos trabajar independientemente. En el ejemplo anterior, el código se divide en dos partes: la parte que define la función `get_at_content` y la parte que la usa, y podemos hacer cambios en una parte sin preocuparnos por los efectos en la otra parte.
Esta es una idea muy poderosa, porque sin ella, el tamaño de los programas que podemos escribir está limitado al número de líneas de código que podemos retener en nuestra cabeza en un momento dado. Algunos de los ejemplos de código en las soluciones a ejercicios en el tema anterior ya estaban rozando este límite, incluso para problemas relativamente simples. Por el contrario, el uso de funciones nos permite construir un programa complejo a partir de pequeños bloques de construcción, cada uno de los cuales es lo suficientemente pequeño como para entenderlo en su totalidad. Debido a que el uso de funciones es tan importante, las futuras soluciones a ejercicios las usarán cuando sea apropiado, incluso cuando no se mencione explícitamente en el texto del problema. Te animo a que te acostumbres a usar funciones en tus soluciones también. 

**Las funciones no siempre tienen que tomar un argumento.**

No hay nada en las reglas de Python que diga que tu función debe tomar un argumento. Es perfectamente posible definir una función sin argumentos:

```python
def get_a_number():
    return 42
```
    
Pero tales funciones tienden a no ser muy útiles. Por ejemplo, podemos escribir una versión de `get_at_content()` que no requiera argumentos estableciendo el valor de la variable `dna` dentro de la función:

```python
def get_at_content():
    dna = "ACTGATGCTAGCTA"
    length = len(dna)
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    at_content = (a_count + t_count) / length
    return round(at_content, 2)
```

Pero eso obviamente no es muy útil. Ocasionalmente, puedes tener la tentación de escribir una función sin argumentos que funcione así:

```python
def get_at_content():
    length = len(dna)
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    at_content = (a_count + t_count) / length
    return round(at_content, 2)

dna = "ACTGATCGATCG"
print(get_at_content())
```
Al principio, esto parece ser una buena idea: funciona porque la función obtiene el valor de la variable `dna` que se establece en la línea 8. Sin embargo, esto rompe la encapsulación que tanto nos costó lograr. La función ahora solo funciona si hay una variable llamada `dna` establecida en la parte del código donde se llama a la función, por lo que las dos piezas de código ya no son independientes. Si te encuentras escribiendo código de esta manera, generalmente es una buena idea identificar qué variables externas a la función se están utilizando dentro de ella y convertirlas en argumentos.

**Las funciones no siempre tienen que devolver un valor.**

Considera esta variación de nuestra función: en lugar de **devolver** el contenido de AT, esta función lo **imprime** en la pantalla:

```python
def print_at_content(dna):
    length = len(dna)
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    at_content = (a_count + t_count) / length
    print(str(round(at_content, 2)))
```
 
Cuando comienzas a escribir funciones, es muy tentador hacer este tipo de cosas. 

Piensas: 
*"OK, necesito calcular e imprimir el contenido de AT, escribiré una función que haga ambas cosas".* 

El problema con este enfoque es que resulta en una función menos flexible. En este momento quieres imprimir el contenido de AT en la pantalla, pero ¿qué pasa si más tarde descubres que quieres escribirlo en un archivo o usarlo como parte de algún otro cálculo? Tendrás que escribir más funciones para llevar a cabo estas tareas.

La clave para diseñar funciones flexibles es reconocer que el trabajo de calcular e imprimir el contenido de AT en realidad son dos trabajos separados: calcular el contenido de AT y imprimirlo. Trata de escribir tus funciones de tal manera que solo realicen un trabajo. Luego puedes escribir fácilmente código para llevar a cabo trabajos más complicados utilizando tus funciones simples como bloques de construcción.

**Las funciones pueden ser llamadas con argumentos nombrados.**

 ¿Qué necesitamos saber sobre una función para poder usarla? Necesitamos saber cuál es el valor de retorno y su tipo, y necesitamos conocer el número y tipo de los argumentos. Para los ejemplos que hemos visto hasta ahora en este curso, también necesitamos saber el orden de los argumentos. Por ejemplo, para usar la función `open`, necesitamos saber que el nombre del archivo va primero, seguido del modo del archivo. 
<br> 
Por ejemplo, para usar la función `open`, necesitamos saber que el nombre del archivo viene primero, seguido por el modo del archivo. Y para usar nuestra versión de dos argumentos de `get_at_content` como se describe anteriormente, necesitamos saber que la secuencia de ADN viene primero, seguida por el número de cifras significativas. 
<br>
Hay una característica en Python llamada **argumentos de palabras clave** que nos permite llamar a funciones de una manera ligeramente diferente. En lugar de dar una lista de argumentos entre paréntesis:

```python
get_at_content("ATCGTGACTCG", 2)
```

podemos suministrar una lista de nombres de variables de argumento y valores unidos por signos de igual:

```python
get_at_content(dna="ATCGTGACTCG", sig_figs=2). 
```

Este estilo de llamar a funciones tiene varias ventajas. No depende del orden de los argumentos, por lo que podemos usar el orden que prefiramos. Estas dos declaraciones se comportan de manera idéntica: 

```python
get_at_content(dna="ATCGTGACTCG", sig_figs=2) 
get_at_content(sig_figs=2, dna="ATCGTGACTCG")
```

También es más claro entender lo que está sucediendo cuando los nombres de los argumentos se dan explícitamente. Incluso podemos mezclar y combinar los dos estilos de llamadas: las siguientes son todas idénticas: 

```python
get_at_content("ATCGTGACTCG", 2)
get_at_content(dna="ATCGTGACTCG", sig_figs=2)
get_at_content("ATCGTGACTCG", sig_figs=2).
```

Aunque no se nos permite comenzar con argumentos de palabras clave y luego volver a la forma normal, esto causará un error.

```python
get_at_content(dna="ATCGTGACTCG", 2)
```

Los argumentos de palabras clave pueden ser particularmente útiles para funciones y métodos que tienen muchos argumentos, y los usaremos cuando sea apropiado en los ejemplos y soluciones de ejercicios en el resto de este libro.

**Los argumentos de funciones pueden tener valores predeterminados.**

Hemos encontrado argumentos de funciones con valores predeterminados antes, cuando estábamos discutiendo la apertura de archivos. Recuerda que la función open toma dos argumentos: un nombre de archivo y una cadena de modo, pero que si la llamamos con solo un nombre de archivo, utiliza un valor predeterminado para la cadena de modo. Podemos aprovechar fácilmente esta característica en nuestras propias funciones, simplemente especificamos el valor predeterminado en la primera línea de la definición de la función. Aquí hay una versión de nuestra función get_at_content donde el número predeterminado de cifras significativas es dos:

```python
def get_at_content(dna, sig_figs=2):
    length = len(dna)
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    at_content = (a_count + t_count) / length
    return round(at_content, sig_figs)
```

Ahora tenemos lo mejor de ambos mundos. Si la función se llama con dos argumentos, usará el número de cifras significativas especificado; si se llama con un solo argumento, usará el valor predeterminado de dos cifras significativas. Veamos algunos ejemplos:

```python
get_at_content("ATCGTGACTCG")
get_at_content("ATCGTGACTCG", 3)
get_at_content("ATCGTGACTCG", sig_figs=4)
```

La función se encarga de completar el valor predeterminado para `sig_figs` para la primera llamada de función donde no se suministra ninguno:

```
0.45
0.455
0.4545
```

Los valores predeterminados de los argumentos de función nos permiten escribir funciones muy flexibles que pueden tener un número variable de argumentos. Solo tiene sentido usarlos para argumentos donde se pueda elegir un valor predeterminado sensato; no tiene sentido especificar un valor predeterminado para el argumento `dna` en nuestro ejemplo. Son particularmente útiles para funciones donde algunas de las opciones solo se van a usar raramente.

**Pruebas de funciones**

Al escribir código de cualquier tipo, es importante verificar periódicamente que tu código haga lo que pretende hacer. Si observas las soluciones a los ejercicios de los temas anteriores, verás que generalmente probamos nuestro código en cada paso imprimiendo algo de salida en la pantalla y comprobando que se vea bien. Por ejemplo, en el tema del dia 2 cadenas de texto, cuando estábamos calculando por primera vez el contenido de AT, usamos una secuencia de prueba muy corta para verificar que nuestro código funcionara antes de ejecutarlo en la entrada real. 

La razón por la que usamos una secuencia de prueba fue que, como era tan corta, podíamos calcular fácilmente la respuesta a simple vista y compararla con la respuesta dada por nuestro código. Esta idea: ejecutar código en una entrada de prueba y comparar el resultado con una respuesta *que sabemos que es correcta*, es tan útil que Python tiene una herramienta integrada para expresarla: `assert`. Una afirmación consta de la palabra `assert`, seguida de una llamada a nuestra función, luego *dos* signos iguales, y luego el resultado que esperamos.


Por ejemplo, sabemos que si ejecutamos nuestra función `get_at_content` en la secuencia de ADN "ATGC", deberíamos obtener una respuesta de 0.5. Esta afirmación probará si ese es el caso:

```python
assert get_at_content("ATGC") == 0.5. 
```

Observa los dos signos iguales: aprenderemos la razón de eso en el próximo capítulo. La forma en que funcionan las afirmaciones es muy simple; si una afirmación resulta ser falsa (es decir, si Python ejecuta nuestra función en la entrada "ATGC" y la respuesta *no es* 0.5), entonces el programa se detendrá y obtendremos un `AssertionError`.

Las afirmaciones son útiles de varias maneras. Proporcionan un medio para verificar si nuestras funciones están funcionando como se pretende y, por lo tanto, nos ayudan a rastrear errores en nuestros programas. Si obtenemos alguna salida inesperada de un programa que utiliza una función particular, y todas las pruebas de afirmación para esa función pasan, entonces podemos estar seguros de que el error no radica en la función sino en el código que la llama. 

También nos permiten modificar una función y verificar que no hayamos introducido ningún error. Si tenemos una función que pasa una serie de pruebas de afirmación, y hacemos algunos cambios en ella, podemos volver a ejecutar las pruebas de afirmación y, suponiendo que todas pasen, estar seguros de que no hemos roto la función.

Las afirmaciones también son útiles como una forma de documentación. Al incluir una colección de pruebas de afirmación junto con una función, podemos mostrar exactamente qué salida se espera de una entrada determinada. 

Finalmente, podemos usar afirmaciones para probar el comportamiento de nuestra función ante entradas inusuales. Por ejemplo, ¿cuál es el comportamiento esperado de `get_at_content` cuando se le proporciona una secuencia de ADN que incluye bases desconocidas (generalmente representadas como *N*)? Una manera sensata de manejar las bases desconocidas sería excluirlas del cálculo del contenido de AT; en otras palabras, el contenido de AT para una secuencia dada no debería verse afectado al agregar un montón de bases desconocidas. Podemos escribir una afirmación que exprese esto:

```python
assert get_at_content("ATGCNNNNNNNNNN") == 0.5.
```

Esta afirmación falla para la versión actual de `get_at_content()`. Sin embargo, podemos modificar fácilmente la función para eliminar todos los caracteres N antes de realizar el cálculo:

```python
def get_at_content(dna, sig_figs=2):
    dna = dna.replace('N', '')
    length = len(dna)
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    at_content = (a_count + t_count) / length
    return round(at_content, sig_figs)
```
    
Y ahora la afirmación pasa. Es común agrupar una colección de afirmaciones para una función particular para probar el comportamiento correcto en diferentes tipos de entradas. Aquí hay un ejemplo para get_at_content que muestra una variedad de tipos de comportamiento:

```python
assert get_at_content("A") == 1
assert get_at_content("G") == 0
assert get_at_content("ATGC") == 0.5
assert get_at_content("AGG") == 0.33
assert get_at_content("AGG", 1) == 0.3
assert get_at_content("AGG", 5) == 0.33333
```

# Resumen:

En este tema, hemos visto cómo empaquetar código en funciones nos ayuda a manejar la complejidad de programas grandes y promover la reutilización de código. Aprendimos cómo para definir y llamar nuestras propias funciones junto con varias formas nuevas de proporcionar argumentos a las funciones.

También examinamos un par de cosas que son posibles en Python, pero rara vez recomendables, como escribir funciones sin argumentos o valores de retorno.

Finalmente, exploramos el uso de afirmaciones para probar nuestras funciones y discutimos cómo podemos usarlas para detectar errores antes de que se conviertan en un problema. 

Los capítulos restantes de este libro utilizarán funciones tanto en los ejemplos como en las soluciones de ejercicios, así que asegúrate de sentirte cómodo con las nuevas ideas de este capítulo antes de avanzar.


# Ejercicios

1. Escribe una funcion que obtenga la hebra reversa complementaria de una cadena de ADN


1. Escribe una función que tome dos argumentos: una secuencia de proteínas y un código de residuo de aminoácido, y devuelva el porcentaje de la proteína que representa el aminoácido. Utiliza las siguientes afirmaciones para probar tu función:

```
assert my_function("MSRSLLLRFLLFLLLLPPLP", "M") == 5
assert my_function("MSRSLLLRFLLFLLLLPPLP", "r") == 10
assert my_function("MSRSLLLRFLLFLLLLPPLP", "L") == 50
assert my_function("MSRSLLLRFLLFLLLLPPLP", "Y") == 0

```




