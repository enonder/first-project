import random

numbs = list(range(1,53))
dict = { 'A' :[], 'B':[], 'C': [], 'D': []}

for i in range(int(len(numbs)/len(dict))):

    for j in dict:

        a= random.choice(numbs)
        dict [j] . append (a)
        b=numbs.index(a)
        del numbs[b]

print(dict)

