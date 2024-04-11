def calcular_reversa_complementaria(secuencia):
	"""
	esta funcion toma como parametro una cadena de adn "string"
	y devuelve un string que contiene la reversa complementaria
	input = secuencia dna (no fasta)
	output = secuencia dna reversa complmentaria (no fasta)

	"""

	secuencia = secuencia.upper()
	replacement1 = secuencia.replace('A', 't')
	replacement2 = replacement1.replace('T', 'a')
	replacement3 = replacement2.replace('C', 'g')
	replacement4 = replacement3.replace('G', 'c')

	reverse_comp = replacement4[::-1]

	return reverse_comp





input_file = open("dnas.t","r")
for secuencia in input_file:
	reversa_complementaria = calcular_reversa_complementaria(secuencia.rstrip("\n"))
	print("esta es la secuencia de entrada: "+secuencia)
	print(reversa_complementaria)
