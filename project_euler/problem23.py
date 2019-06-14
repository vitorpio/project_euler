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

limit = 28123

abundant_numbers = set()

for n in range(1, limit + 1):
	if sum_factors(n) > n:
		abundant_numbers.add(n)

abundant_numbers_sum = set()

for n1 in abundant_numbers:
	for n2 in abundant_numbers:
		s = n1 + n2		
		if s <= limit:
			abundant_numbers_sum.add(s)
		else:
			break

nums = set()
for n in range(1, limit + 1):
	if n not in abundant_numbers_sum:
		nums.add(n)
print(reduce(add, nums, 0))

		
