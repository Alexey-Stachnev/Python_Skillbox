inp = input()
arr = inp.split()

def number_of_identical_numbers(list):
    num = 1
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] == list[j]:
                num += 1
                break
    return num

result = number_of_identical_numbers(arr)
if result == len(arr):
    print("Все числа равны")
elif result == 1:
    print("Все числа разные")
else:
    print("Есть равные и неравные числа")