# Analisis metagenomico de distribución bacteriana abundantes en sedimentos costeros

**¿Sabes en que consiste la metagenómica?** <br>
Te recomiendo este [video del EMBL](https://www.youtube.com/watch?v=RcYXTpNS_XU)

En este ejercicio tenemos que calcular la abundancia de especies bacterianas en una muestra de secuenciación 16S obtenida sedimentos costeros. 
Nuestra libreria de fragmentos de dna ribosomico 16S se encuentra en el archivo `bacterias.csv` y comprende 6 generos: pseudomonas, acidobacteria, rhizobium, bacillus, streptomices y Mycobacterium. 

| Especie         | Secuencia   |
|-----------------|-------------|
| Pseudomonas     | ATCGATCG    |
| Bacillus        | CGATCGAT    |
| Streptomyces    | TATATATA    |
| Rhizobium       | GCGCGCGC    |
| Mycobacterium   | AGAGAGAG    |
| Acidobacterium  | CTCTCTCT    |




Tendremos que generar un diccionario a partir de dicha tabla y analizar los reads secuenciados del archivo `multifasta.fasta`:


```bash
>AKG0001
TTCGGCGACGTCAAAGGAATTACTGTTTTCCCATTGTACGGCGAATAACACATTCACGGTCCACTCGAAGTGCGACAAACCCGTGGTCCATCTTTACCGGATGGTGGTGAAATTGGTATCCGGCCTCTCTCTCGTTGTTTGGGAGCCAGC
>AKG0002
AATCACTTTCCACCTCCAGTAACGTTTCTTCACCCAAGGCAAAGACTAACTGTATAAGAATAAACGTACACTTGAGAGGATCGTTCTCTAGACACTCATCGATCGGTCTTTGTGCAAATCCCGGCAGGAACCGGGGATAAGGGTGTCTAA
>AKG0003
AATCAATCTATGTGGCTGGTAGTTGGATCGTCTTTCACGGACGGGTGTAGGAATGGATAGGGGTGTGAAATCTTTTCTGCCGCACCTACTGTAGGTTGTCAAGGTTATACAACGCGCGCGCCACCCCAGAGCGCACATTTTCTAAGCTCG
```

para obtener el conteo de cada genero bacteriano con una salida de resultados similar a esta:


```python
$ python calcular_abundacia_bacterias.py
Total de secuencias para Pseudomonas: 203
Total de secuencias para Bacillus: 180
Total de secuencias para Streptomyces: 163
Total de secuencias para Rhizobium: 161
Total de secuencias para Mycobacterium: 167
Total de secuencias para acidobacterium: 186
```

**Quieres ir mas alla?**
1. Puedes obtener los porcentajes de cada especie respecto al total de secuencias fasta analizadas?
1. Que te parece explorar los paquetes numpy y matplotlib y plotear los resultados en un histograma de frecuencias?



