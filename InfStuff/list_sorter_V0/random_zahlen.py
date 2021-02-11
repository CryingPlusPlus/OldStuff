from random import *

fh = open('unsorted.txt', 'w')

nums = []
n = 1000000
i = 0
while i <= n:
    nums.append(10000*random())
    i += 1

for x in nums:
    fh.write(str(x))
    fh.write(';')
fh.write('0')
fh.close()