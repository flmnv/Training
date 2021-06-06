mass = []
for i in range(5):
	string = input().split(' ')
	mass.append(string)
for i in range(5):
	for j in range(5):
		if mass[i][j] == '1':
			print(abs(2 - i) + abs(2 - j))
			break