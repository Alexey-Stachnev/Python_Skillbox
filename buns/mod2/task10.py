inp = input()
word = ''
new_word = ''
for symb in inp:
    if symb == ' ':
        new_word += word[-1]
        word = ''
    word += symb
new_word += word[-1]
print(new_word)