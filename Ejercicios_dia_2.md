Ejercicio_2. Porcentaje GC
----------------------------
Escribe un script de python que calcule el contenido GC en porcentaje de la siguiente secuencia de ADN:
```
ATGCAAATTGTGTGTGCATAATTTATATAGGCTAGAATAGAATCGCTA
```


Ejercicio_3. Fragmentos de Restriccion
--------------------------------------
Dada la siguiente secuencia de ADN_
```
ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT
```

Esta secuencia contiene un sitio de restricción reconocido por la enzima __EcorRI__, la cual corta el motivo  `G*AATTC` ( el asterisco indica el sitio exacto del corte). 
Escribe un script que calcule el tamaño de los dos fragmentos que se produciran en las secuencia de ADN tras ser digerida con __EcoRI__

Ejercicio_4. Splicing de intrones
----------------------------------
Consideremos la siguiente secuencia de ADN eucariota en la que estamos interesados

```
ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT
```

Esta secuencia contiene 2 exones (region codificante) y un intron (region no codificante). El primer exon comienza al desde la posicion cero de la secuencia hasta la `posición 63`. El segundo exon hace lo propio desde la `base 91` hasta el final de la secuencia.


__Cuestiones:__

__a)__ Escribe un script que imprima en pantalla solo la región codificante,

__b)__ que calcule el porcentaje de DNA que supone esa secuencia codificante sobre el total del dicho gen,

__c)__ que escriba al final la secuencia de ADN indicando en minúscula el intron y mayúscula los exones dentro de la misma secuencia

__d)__ el script debe generar dos archivos uno con las dos secuencias en formato fasta conteniendo los exones y otro archivo conteniendo en formato fasta el intron tal y como sigue:

exones.fasta

>exon1
agcta...
>exon2
agtcgatca
intrones.fasta

>intron
atgctacg....
