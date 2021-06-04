n = int(input())
s = 0
for i in range(n):
	string = input().split(' ')
	if int(string[0]) + int(string[1]) + int(string[2]) >= 2:
		s += 1
print(s)