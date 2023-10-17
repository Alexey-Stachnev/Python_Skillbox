str = input()
whitespace1 = 0
whitespace2 = 0
for symb in range(len(str)):
    if str[symb] == ' ':
        if whitespace1 == 0:
             whitespace1 = symb
        else:
             whitespace2 = symb
first_num = int(str[:whitespace1])
second_num = int(str[whitespace1 + 1: whitespace2])
third_num = int(str[whitespace2 + 1:])

if (second_num > first_num and second_num < third_num) or (second_num > third_num and second_num < first_num):
    print(second_num)
elif (first_num > second_num and first_num < third_num) or (first_num > third_num and first_num < second_num):
    print(first_num)
else:
    print(third_num)