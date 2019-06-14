def factors(n):
	factors = []
	for i in range(1, int(n ** 0.5 + 1)):
		if n % i == 0:
			if (i != n/i):
				factors.append(i)
				factors.append(n / i)
			else:
				factors.append(i)
	return factors

count = 1
triangle_number = 0
divisors = 500

while True:
	triangle_number += count
	print(f'{triangle_number} -> {len(factors(triangle_number))}')
	if len(factors(triangle_number)) > divisors:
		break
	count += 1
