print('Limit?')
n = int(input()) + 1
a = []
prim = []

for i in range(n):
    a.append(i)

for p in range(2, n):
    if a[p] == p:
        prim.append(p)
        for i in range(p, n, p):
            a[i] = p


for i in prim:
    print(i)
