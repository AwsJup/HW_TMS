
# Даны три слова. Выяснить, является ли хоть одно из них палиндромом
# ("перевертышем"), т. е. таким, которое читается одинаково слева направо и
# справа налево. (Определить функцию, позволяющую распознавать слова
# палиндромы.)


str = input('word: ')

def palindromes(str):
    length = len(str)
    first = 0
    last = length -1
    status = 1
    while (first<last):
           if (str[first] == str[last]):
               first = first+1
               last = last-1
           else:
               status = 0
               break
    return int(status)


status = palindromes(str)
if(status):
    print(True)
else:
    print(False)