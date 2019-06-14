import math

def is_prime(n):
	if (n < 2) or (n % 2 == 0 and n != 2):
		return False
	for v in range(3,int(math.sqrt(n)+1),2):		
		if n % v == 0:
			return False
	return True

def prime_pos(pos):
	primes = [2,3]
	n = 5
	while len(primes) < pos:
		if is_prime(n):			
			primes.append(n)
		n += 2
	return primes[-1]

print(prime_pos(10001))
