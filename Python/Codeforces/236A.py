string = input()
result = ''
for i in range(len(string)):
	if result.find(string[i]) == -1:
		result += string[i]
		
if len(result) % 2 == 0:
	print('CHAT WITH HER!')
else:
	print('IGNORE HIM!')