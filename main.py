import string

letters = list(string.ascii_lowercase)

zlist = []
for a in range(len(letters)):
    zlist = [0] * (a + 1)

def my_func(x, y):


    for j in x:
        for i in letters:
            if i == j:
                y[letters.index(i)] +=1
    return y

print(my_func("deneme", zlist ))



