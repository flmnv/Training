s = 0
n = int(input())
for i in range(n):
	string = input()
	if string == 'X++' or string == '++X':
		s += 1
	else:
		s -= 1
print(s)