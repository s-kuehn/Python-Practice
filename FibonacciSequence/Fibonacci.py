def prog(numItr):
	# Create dictionary
	fibcach = {}
	# Calculate Fibonacci Sequence
	def fib(n):
		if n in fibcach:
			return fibcach[n]
		if n == 0:
			val = 1
		elif n == 1:
			val = 1
		elif n >= 2:
			val = fib(n-1) + fib(n-2)
		fibcach[n] = val
		return val

	# Format Numbers When displayed
	for numItr in range(0,numItr+1):
		print(numItr, ':', fib(numItr))

# run function
prog(int(input('how many iteration would you like? ')))

# Continue Running Prompt
while True:
	cont = input('Continue? y/n ' )
	if cont == ('y'):
		prog(int(input('how many iteration would you like? ')))
	elif cont == ('n'):
		exit()
	else:
		print('invalid character')
