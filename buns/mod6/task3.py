def armstrong_generator():
    num = 100
    while True:
        digits = [int(i) for i in str(num)]
        sum_of_powers = sum([i ** len(digits) for i in digits])
        if sum_of_powers == num:
            yield num
        num += 1

generator = armstrong_generator()

def get_armstrong_numbers():
    return next(generator)

for i in range(8):
    print(get_armstrong_numbers(), end=' ')