import math
from operator import add
from functools import reduce

def is_prime(n):
	for v in range(3,int(math.sqrt(n)+1),2):		
		if n % v == 0:
			return False
	return True

limit = 2000000

primes = [2] + list(filter(is_prime, range(3, limit + 1, 2)))

print(reduce(add,primes))
