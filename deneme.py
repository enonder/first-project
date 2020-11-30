import string

letters = list(string.ascii_lowercase)
numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
str_1 = 'kuzey'
list_1 = []
list_1[:] = str_1


def soru():
    x = 0
    for i in list_1:
        if letters[x] == list_1[i]:
            numbers[x] += 1

        else:
            x += 1
        return x

soru()
print(numbers)



