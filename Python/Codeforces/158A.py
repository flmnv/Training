s = 0
nk = input().split(' ')
a = input().split(' ')
for i in range(int(nk[0])):
	if int(a[i]) >= int(a[int(nk[1]) - 1]) and int(a[i]) > 0:
		s += 1
print(s)