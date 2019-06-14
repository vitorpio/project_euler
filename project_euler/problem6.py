import math

sum_of_squares = sum([math.pow(n,2) for n in range(1,101)])
square_of_sum = math.pow(sum([n for n in range(1,101)]),2)

print(square_of_sum - sum_of_squares)
