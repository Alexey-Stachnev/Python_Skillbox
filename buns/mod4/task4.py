str = input()
def palindrome(letters):
    counter = {}
    single = ''
    result = ''

    for ch in letters:
        if ch not in counter:
            counter[ch] = 1
        else:
            counter[ch] += 1
            if counter[ch] == 2:
                counter[ch] = 0
                result += ch

    for ch, count in counter.items():
        if count == 1:
            single = ch
            break

    return result + single + result[::-1]
def count_the_number_of_letters(str):
    dict = {}
    for i in str:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    return dict

def pal_possible(dict):
    oddNumberOfLetters = 0
    for j in dict.values():
        if oddNumberOfLetters == 2:
            break
        if j % 2 != 0:
            oddNumberOfLetters += 1
    return oddNumberOfLetters < 2

if str == str[::-1]:
    print(str)
elif pal_possible(count_the_number_of_letters(str)) == False:
    print(False)
else:
    print(palindrome(str))