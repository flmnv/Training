result = ''
string = input()
string = string.lower()
for i in range(len(string)):
	if (string[i] != 'a' and string[i] != 'o' and
		string[i] != 'y' and string[i] != 'e' and
		string[i] != 'u' and string[i] != 'i'):
		result += '.' + string[i]
print(result)