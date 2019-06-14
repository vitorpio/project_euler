def fib(limit):
	fib_seq = [1,2]
	while True:
		next_value = fib_seq[-1] + fib_seq[-2]
		if next_value > limit:
			return fib_seq
		fib_seq.append(next_value)
	
fibs = fib(4000000)
even_fibs = list(filter(lambda value: value % 2 == 0, fibs))

print(sum(even_fibs))


