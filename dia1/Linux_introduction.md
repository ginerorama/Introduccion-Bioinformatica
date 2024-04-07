# Bienvenidos al Curso de Introducción a la programacion Bioinformatica 



Profesor coordinador: Joaquín Giner Lamia <br>
Profesora: Francine Amaral Piubeli


## Tu equipo de trabajo

#### Sistema operativo
Linux Ubuntu 20.

#### Descripción General

<p align="center">
<img src="media/0.1.png" alt="drawing" width="400"/>
</p>



Linus Torvalds era un estudiante de la Universidad de Helsinki a quien le gustaba jugar con software y computadoras [pero parece que tiene problemas para entender las emociones de las personas y responder adecuadamente](https://www.newyorker.com/science/elements/after-years-of-abusive-e-mails-the-creator-of-linux-steps-aside). En 1991 anunció la creación de un nuevo sistema operativo al que llamó Linux: 

1. Linux está presenta hoy en dia el 94% de las supercomputadoras del mundo, la mayoría de los servidores que alimentan Internet y más de mil millones de dispositivos Android. 
2. El 97% de los encargados de contratación en empresas relacionadas con la gestión informática priorizarán la contratación de empleados competentes en Linux en relación con otras áreas de habilidades. 
3. Linux es particularmente adecuado para empresas con presupuestos pequeños (¡como laboratorios científicos!). 
4. Linux es gratuito para usar e instalar, y es extremadamente estable y confiable (¡sin pantalla azul de la muerte!).


[Linus es un personaje](https://www.pcmag.com/news/linuxs-linus-torvalds-sorry-for-being-a-jerk) 

<br>

### Linux Ubuntu 

Linux Ubuntu 20.0
A diferencia de Windows, hay muchas interfaces ("shells"), distribuciones y "sabores" o Flavours de Linux. Obviamente, la interfaz que está en tu teléfono Android es muy diferente de la que puedes usar con Ubuntu. ¡Ten en cuenta que también hay muchas interfaces diferentes para tu teléfono! Linux también estará incrustado en dispositivos como Raspberry PI, tu router WiFi, tu Smart TV, sistemas de entretenimiento en tu automóvil y en naves espaciales. Linux puede ser muy pequeño: ¡hay distribuciones de Linux que se ejecutarán con tan solo 3 MB de RAM! Debido 


<p align="center">
<img src="media/0.2.png" alt="drawing" width="400"/>
</p>


#### Por qué Linux en Bioinformatica

Linux es ampliamente utilizado en bioinformática por varias razones:

1. **código abierto:** Muchas herramientas y programas de bioinformática están disponibles como software de código abierto, lo que significa que **los usuarios pueden acceder al código fuente, modificarlo según sea necesario y compartir mejoras con la comunidad**. Linux proporciona un entorno ideal para ejecutar este tipo de software.

1. **Estabilidad y fiabilidad:** Linux es conocido por ser estable y fiable, lo que es fundamental para el procesamiento de grandes conjuntos de datos y ejecución de análisis complejos en bioinformática.

1. **Eficiencia y personalización:** Linux es altamente personalizable y se puede adaptar para satisfacer las necesidades específicas de la bioinformática. Los usuarios pueden **configurar su entorno de trabajo de acuerdo con sus requisitos y optimizar el sistema para ejecutar análisis de manera eficiente**.

1. **Recursos de línea de comandos:** Muchas herramientas de bioinformática se ejecutan desde la línea de comandos, y **Linux ofrece un entorno de línea de comandos robusto y poderoso que facilita la ejecución de estos programas y la automatización de tareas**.
 
1. **Escalabilidad:** Linux es altamente escalable y puede funcionar en una amplia gama de dispositivos, desde computadoras de escritorio hasta servidores de alto rendimiento. Esto lo hace adecuado para ejecutar análisis bioinformáticos en una variedad de entornos, desde laboratorios de investigación hasta centros de supercomputación.



#### Empezando con Linux


Una de las principales aplicaciones que necesitarás conocer durante los primeros días es el **Terminal**. El icono para abrir el Terminal se encuentra en la barra de iconos (en la parte inferior izquierda de tu pantalla) - es un icono de caja negra (esto en caso de que abramos la terminal en Ubuntu, en Windows se nos abre por defecto al abrir Ubuntu). 

<p align="center">
<img src="media/0.3.png" alt="drawing" width="200"/>
</p>



Ábrelo ahora. Lo primero que vemos es el **Prompt** o Simbolo del sistema, que es un indicador visual que generalmente aparece en la interfaz de línea de comandos de los sistemas operativos UNIX.

<p align="center">
<img src="media/0.5.png" alt="drawing" width="800"/>
</p>




Este prompt indica que el sistema está listo para recibir una entrada del usuario, como un comando o una consulta. Por lo general, el prompt muestra:

username <br>
computername <br>
localización en el sistema <br>
command prompt ('$') <br>


```
e.g. osboxes@osboxes ~/bioinformatic_course$
```

Escribe: "mkdir Course" ("mkdir" = "make directory") y presiona `Enter`. Acabas de crear un directorio llamado Course. <br>
Ahora escribe: "cd Course" ("cd" = "Change directory") y presiona `Enter`. Tu prompt debe cambiar a algo similar a:

```
osboxes@osboxes ~/Course $
```

El **autocompletado es "inteligente"** en el sentido de que seleccionará automáticamente ya sea una aplicación (en el contexto donde se necesita una aplicación) o un nombre de archivo (en el contexto donde se necesita un nombre de archivo). Puedes probar esto ahora:

```
osboxes@osboxes ~/Course $ cd ..            

osboxes@osboxes ~/Course $ cd Co            (now press Tab)

osboxes@osboxes ~/Course $ cd Course
```



¡Recuerda esto! ¡Es un truco muy útil que acelerará tu escritura!

Para ir "hacia arriba" un nivel en el directorio, escribe 'cd ..' (dos puntos).

Para regresar a tu directorio "home", desde cualquier lugar, escribe 'cd ~'.

```
osboxes@osboxes ~/Course $ cd ~
osboxes@osboxes ~$

```

Para repetir un comando previo, presiona la FLECHA HACIA ARRIBA hasta que veas ese comando en el prompt (la FLECHA HACIA ABAJO te lleva a través del historial de comandos en la dirección opuesta).

### atajos

`ctrl+A`te llava al comienzo del prompt
`ctrl+E`te lleva al final de la linea



# Recap

1. Prompt
1. `Tab`automcompletar
1. Historial de comandos con Cursor arriba o a cursor abajo
1. crtl+A y ctrl+E
