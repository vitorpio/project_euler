import string
import itertools

digits = string.digits
permuts = [''.join(p) for p in itertools.permutations(digits)]
print(permuts[999999])

