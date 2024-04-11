# open the input file
file = open("input.txt")

# open the output file
output = open("trimmed.txt", "w")

count = 1


# go through the input file one line at a time
for dna in file:

    # get the substring from the 15th character to the end
    trimmed_dna = dna[14:]

    # get the length of the trimmed sequence
    trimmed_length = len(trimmed_dna.rstrip())


    # print out the trimmed sequence
    output.write(">secuencia_"+ str(count) +"\n" + trimmed_dna)

    # print out the length to the screen
    print("processed sequence with length " + str(trimmed_length))

    count = count + 1