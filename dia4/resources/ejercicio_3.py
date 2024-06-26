# our function to get AT content
def get_at_content(dna):
    length = len(dna)
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    at_content = (a_count + t_count) / length
    return at_content


data = open("data.csv")
for line in data:
    columns = line.rstrip("\n").split(",")
    species = columns[0]
    sequence = columns[1]
    name = columns[2]
    expression = int(columns[3])
    at_content = get_at_content(sequence)
    if at_content < 0.5 and expression > 200:
        print(name,str(round(at_content,2)),str(expression))

