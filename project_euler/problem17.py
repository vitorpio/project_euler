# 1 - 19
numbers = [ '','one','two','three','four','five','six','seven','eight','nine','ten',
'eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']

decimals = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

# 20 - 99
for decimal in decimals:
	numbers.append(decimal)
	for n in range(1, 10):
		numbers.append(decimal + '-' + numbers[n])

# 100 - 999
for hundred in range(1, 10):
	numbers.append(numbers[hundred] + ' hundred')
	for number in range(1, 100):
		numbers.append(numbers[hundred] + ' hundred and ' + numbers[number])

# 1000
numbers.append('one thousand')


letters = 0
for number in numbers:
	number_clean = number.replace('-',' ').replace(' ','')
	letters += len(number_clean)

print(letters)
