
inicio = 'Step'
fin = 'Loop'

with open('log.melt-berendsen','r') as archivo:
	while True:
		linea = archivo.readline()
		if linea == '':
			break
		if inicio in linea:
			with open ('salida.txt', 'w') as output:
				while True:
					linea = archivo.readline()
					if fin in linea or linea == '':
						break
					output.write(linea)
