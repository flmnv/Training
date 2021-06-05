first = input().lower()
second = input().lower()
for i in range(len(first)):
	if first[i] != second[i]:
		if ord(first[i]) < ord(second[i]):
			print(-1)
			raise SystemExit
		else:
			print(1)
			raise SystemExit
print(0)