s = 0
knw = input().split(' ')
for i in range(1, int(knw[2]) + 1):
	s += i * int(knw[0])
if s > int(knw[1]):
	print(s - int(knw[1]))
else:
	print(0)