def gcd(num1, num2):
    if num1 == 0:
        return num2
    return gcd(num2 % num1, num1)