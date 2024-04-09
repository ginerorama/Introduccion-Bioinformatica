my_dna = "ATGCAAATTGTGTGTGCATAATTTATATAGGCTAGAATAGAATCGCTA"
my_dna = my_dna.upper()
length = len(my_dna)
g_count = my_dna.count('G')
c_count = my_dna.count('C')
gc_content = ((g_count + c_count) / length)*100
print("GC content is " + str(gc_content))