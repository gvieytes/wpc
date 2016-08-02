a = 1
b = 2
c = 0
lista = [a,b]

while True:
	c = a+b
	if c >= 4000000:
		break
	a = b
	b = c
	lista.append(c)

print(lista)
