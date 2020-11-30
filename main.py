import string

letters = list(string.ascii_lowercase)
name = 'kuuuzey'

zlist = []
for a in range(len(letters)):
    zlist = [0] * (a + 1)

def bok(x, y):
    # zlist = []
    # for a in range(len(letters)):
    #     zlist = [0] * (a + 1)

    for j in x:
        for i in letters:
            if i == j:
                y[letters.index(i)] +=1
    return y

print(bok("bokasdgfhjkldAsdfghjnhgfdsdfvgbn", zlist ))



