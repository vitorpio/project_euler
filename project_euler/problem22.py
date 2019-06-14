from operator import add
from functools import reduce
import string

points = {}
for pos, l in enumerate(string.ascii_uppercase):
	points[l] = pos + 1

with open('names.txt','r') as f:
	names = f.read().splitlines()

names.sort()

score = 0
for pos, name in enumerate(names):
	letters_points = [points[letter] for letter in name]
	score += (pos + 1) * reduce(add, letters_points, 0)
print(score)
		

    	
