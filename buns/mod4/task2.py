def exponentiation(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return exponentiation(a**2, n/2)
    else:
        return a * exponentiation(a, n-1)

print(exponentiation(10,2))