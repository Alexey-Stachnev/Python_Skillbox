inp = input()
consonants = 0
vowel = 0
for symb in inp:
    if symb in 'бвгджзйклмнпрстуфхцчшщ':
        consonants += 1
    if symb in 'аеёиоуыэюя':
        vowel += 1
print(vowel, consonants)