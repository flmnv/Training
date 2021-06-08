k = 0
x = int(input())
while x != 0:
	if x > 5:
		x -= 5
	else:
		x = 0
	k += 1
print(k)