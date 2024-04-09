my_dna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
replacement1 = my_dna.replace('A', 'T')

replacement2 = replacement1.replace('T', 'A')

replacement3 = replacement2.replace('C', 'G')

replacement4 = replacement3.replace('G', 'C')


print(my_dna)
print(replacement4)