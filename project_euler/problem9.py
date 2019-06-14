import math	
from functools import reduce
from operator import mul

possibles = []

for c in range (3,1001):
	for b in range(2,c):
		a = 1000 - c - b
		if a < 1:
			break
		if (a + b + c == 1000) and (a < b and b < c):
			possibles.append([a,b,c])

response = list(filter(lambda p: (math.pow(p[0],2) + math.pow(p[1],2)) == math.pow(p[2],2), possibles))

print(reduce(mul, response[0], 1))
