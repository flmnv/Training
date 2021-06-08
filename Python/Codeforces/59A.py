big = 0
small = 0
string = input()
for i in string:
	if i != i.lower():
		big += 1
	else:
		small += 1
if small >= big:
	print(string.lower())
else:
	print(string.upper())