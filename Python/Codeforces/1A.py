from math import ceil

nma = input().split(' ')
result = ceil(int(nma[0]) / int(nma[2])) * ceil(int(nma[1]) / int(nma[2]))
print(result)