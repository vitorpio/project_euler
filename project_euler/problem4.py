def palindrome_prod():
    prods = []
    for n1 in range(999, 100, -1):
        for n2 in range(999, 100, -1):
            prod = n1 * n2
            if str(prod) == str(prod)[::-1]:
                prods.append(prod)
    return prods


print(max(palindrome_prod()))
