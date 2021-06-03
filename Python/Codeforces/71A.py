count = int(input())
strings = []
for i in range(count):
	strings.append(input())
	if len(strings[i]) > 10:
		strings[i] = strings[i][0] + str(len(strings[i]) - 2) + strings[i][-1]
for i in range(count):
	print(strings[i])