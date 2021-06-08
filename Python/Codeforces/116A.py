s = 0
maxS = 0
n = int(input())
for i in range(n):
	ab = input().split(' ')
	s += int(ab[1]) - int(ab[0])
	if s > maxS:
		maxS = s
print(maxS)