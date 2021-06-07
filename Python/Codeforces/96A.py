string = input()
lastChar = string[0]
count = 0
for i in string:
	if i == lastChar:
		count += 1
		if count >= 7:
			print('YES')
			raise SystemExit
	else:
		lastChar = i
		count = 1
print('NO')