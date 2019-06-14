step = 20
n = 20

while True:
    print(n)
    if all([n % x == 0 for x in range(1, 21)]):
        break
    n += 20
