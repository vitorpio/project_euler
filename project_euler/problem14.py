def collatz(n):
	if n % 2 == 0:	
		return n / 2
	else:
		return (3 * n) + 1


collatz_sequences = {1:1, 2:2}

for count in range(3, 1000001):
	n = count
	sequence = []
	while True:
		if n in collatz_sequences:
			collatz_sequences[count] = len(sequence) +  collatz_sequences[n]
			break
		else:
			sequence.append(n)
			n = collatz(n)

print(max(collatz_sequences, key=collatz_sequences.get))
