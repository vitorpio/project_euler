import math

def digits_sum(n):

	num = int(math.pow(2, n))
	num_digits_sum = 0

	for digit in str(num):
		num_digits_sum += int(digit)
	return num_digits_sum

print(digits_sum(1000))
