#hamming distance is the number of bits that are different in the binary rep. of numbers
from __future__ import print_function

def hammingDistace(x,y):
	assert len(x) == len(y)
	count = 0
	for ch1,ch2 in zip(x,y):
		if ch1 != ch2:
			count += 1
	return count

if __name__ == '__main__':
	print('The number of bits should be equal \n')
	a = raw_input('Enter the number: ')
	b = raw_input('Enter the second number: ')
	print('No. of bits that are different =',hammingDistace(a,b))