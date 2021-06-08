k = 0
ab = input().split(' ')
a = int(ab[0])
b = int(ab[1])
while a <= b:
	a *= 3
	b *= 2
	k += 1
print(k)