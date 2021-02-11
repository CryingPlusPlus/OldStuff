import random

unSorted = [random.randint(0,100) for i in range(100000)]
rawSorted = [[] for i in range(1 + max(unSorted) - min(unSorted))]

for num in unSorted:
    rawSorted[num - min(unSorted)] += [num]


sorted = []
for subList in rawSorted:
    sorted += subList

print(sorted)
