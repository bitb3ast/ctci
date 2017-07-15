#check if a string has unique characters

occurance = {}

for char in input():
	occurance.setdefault(char,0)
	occurance[char] += 1
	if occurance[char] > 1:
		print('Repeating Characters in String')
	else:
		print('Unique Characters in String')
