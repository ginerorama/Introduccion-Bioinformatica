my_dna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
replacement1 = my_dna.replace('A', 't')

replacement2 = replacement1.replace('T', 'a')

replacement3 = replacement2.replace('C', 'g')

replacement4 = replacement3.replace('G', 'c')


print(my_dna)
print(replacement4)
print(replacement4.upper()[::-1])