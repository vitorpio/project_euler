from operator import add
from functools import reduce

def sum_factors(n):
	factors = []
	for i in range(1, int(n ** 0.5 + 1)):
		if n % i == 0:
			if (i != n/i):
				factors.append(i)
				factors.append(n / i)
			else:
				factors.append(i)
	factors.remove(n)
	return reduce(add, factors, 0)

amicables = []

for n in range(2, 10001):
	sum_factors_n = int(sum_factors(n))
	if n == sum_factors(sum_factors_n):
		if n not in amicables and n != sum_factors_n:				
			amicables.append(n)
			amicables.append(sum_factors_n)

print(sum(amicables))
