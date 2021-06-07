n = int(input())
mass = []
for i in range(n):
	mass.append(input().split(' '))
for i in range(3):
	temp = 0
	for j in range(n):
		temp += int(mass[j][i])
	if temp != 0:
		print('NO')
		raise SystemExit
print('YES')