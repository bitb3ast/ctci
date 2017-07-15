#check if a string has unique characters

def isUnique(string):
	occurance = {}
	for char in string:
		occurance.setdefault(char,0)
		occurance[char] += 1
		if occurance[char] > 1:
			return 'Repeating Characters in String'

	return 'String has unique characters'


string = raw_input('Enter String ')
print(isUnique(string))
	
