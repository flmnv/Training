nk = input().split(' ')
n = int(nk[0])
for i in range(int(nk[1])):
	if n % 10 != 0:
		n -= 1
	else:
		n //= 10
print(n)