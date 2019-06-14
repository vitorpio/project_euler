import math

def is_prime(n):
	if (n < 2) or (n % 2 == 0 and n != 2):
		return False
	for v in range(3,int(math.sqrt(n)+1),2):		
		if n % v == 0:
			return False
	return True

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

f = factors(600851475143)

for n in f[::-1]:
	if is_prime(n):
		print(n)
		break
