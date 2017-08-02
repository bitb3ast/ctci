#Fizz for multiples of 3 Buzz for multiples of 5 and FizzBuzz for multiples of both

for i in range(1,input('Enter Range: ')+1):
	output = ''
	if i % 3 == 0:
		output += 'fizz'
	if i % 5 == 0:
		output += 'buzz'
	if output == '':
		output = str(i)

	print(output)