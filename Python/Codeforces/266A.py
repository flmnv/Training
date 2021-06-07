input()
string = input()
result = string[0]
lastChar = string[0]

for i in range(len(string)):
	if string[i] != lastChar:
		result += string[i]
		lastChar = string[i]

print(len(string) - len(result))