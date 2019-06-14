fibs = [0,1,1]

def fibonacci(pos):
	if pos < len(fibs):
		return fibs[pos]
	else:
		fibs.append(fibonacci(pos - 1) + fibonacci(pos - 2))
		return fibs[pos]

count = 1

while len(str(fibonacci(count))) < 1000:
	count += 1

print(count)
