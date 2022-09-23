

def fact(x):
	if x == 0:
		return 1
	else:
		return x * fact(x - 1)

for i in range(0, 10):
	print("Hallo:", i)

print(fact(0))
print(fact(1))
print(fact(2))
print(fact(5))
print(fact(10))

# Her er en kommentar!!!
