inp = input()
flag = True
try:
    number = int(inp)
except ValueError:
    flag = False
    print("Неверный ввод")

def convert_to_binary(number):
    remains = ''
    while number != 0:
        remains += str(number % 2)
        number //= 2
    return(remains[::-1])

def convert_to_octal(number):
    remains = ''
    while number != 0:
        remains += str(number % 8)
        number //= 8
    return(remains[::-1])

def number_to_letter(number):
    if number == 10:
        return 'A'
    if number == 11:
        return 'B'
    if number == 12:
        return 'C'
    if number == 13:
        return 'D'
    if number == 14:
        return 'E'
    if number == 15:
        return 'F'
    return 'Неверное число'

def convert_to_hexadecimal(number):
    remains = ''
    a=''
    while number != 0:
        a = number % 16
        if a > 9:
            remains += number_to_letter(a)
        remains += str(a)
        number //= 16
    return(remains[::-1])
if flag:
    a = convert_to_binary(number)
    b = convert_to_octal(number)
    c = convert_to_hexadecimal(number)
    print(a, b, c)