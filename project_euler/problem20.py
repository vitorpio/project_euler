import math
from operator import add
from functools import reduce

factorial = math.factorial(100)
digits = [int(d) for d in list(str(factorial))]
sum_digits = reduce(add, digits)

print(sum_digits)
