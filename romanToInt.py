#convert a roman number to integer

from __future__ import print_function

def value(elem):
	roman = {'M':1000,'D':500,'C': 100,'L':50,'X':10,'V':5,'I':1}
	return roman[elem]

if __name__ == '__main__':

	number = list(raw_input('Enter the number '))
	result = 0
	i = 0	
	
	while(i<len(number)):
		s1 = value(number[i])
		if i+1 < len(number):
			s2 = value(number[i+1])
			if s1 >= s2:
				result = result + s1
				i += 1
			else:
				result = result + s2 - s1
				i += 2
		else:
			result = result + s1 
			i += 1


	print('The sum of the number is ',result)

