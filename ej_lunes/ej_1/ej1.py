a = 1
b = 0
conj1 = set()

while a < 1000:
	if a % 3 == 0 or a % 5 == 0:
		conj1.add(a)
		b = b + a
	a = a + 1

print('Conjunto1:')
print(sum(conj1))

print('Esto es b:')
print(b)
