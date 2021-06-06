ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
t = int(input())
allResult = ''
for k in range(t):
	input()
	string = input()
	result = 'a'
	while string.find(result) != -1:
		if result[len(result) - 1] != 'z':
			result = result[:-1] + ALPHABET[ord(result[-1]) - 96]
		else:
			if result[0] == ALPHABET[25]:
				temp = ''
				for i in range(len(result) + 1):
					temp += ALPHABET[0]
				result = temp
			else:
				result = result[:-1] + ALPHABET[0]
				for i in range(len(result) - 2, -1, -1):
					if result[i + 1] == 'a':
						result = result[:i] + ALPHABET[(ord(result[i]) - 96) % 26] + result[i + 1:]
					else:
						break
	allResult += result
	if k < t - 1:
		allResult += '\n'
print(allResult)