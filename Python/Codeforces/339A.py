result = ''
string = input().split('+')
for i in range(len(string) - 1):
	for j in range(i + 1, len(string)):
		if int(string[i]) > int(string[j]):
			temp = string[i]
			string[i] = string[j]
			string[j] = temp
for i in range(len(string)):
	result += string[i]
	if i != len(string) - 1:
		result += '+'
print(result)