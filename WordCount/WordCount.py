# Function to find number of words in string
def words(inputStr):
	ans = inputStr.split()
	finalcount = len(ans)
	return finalcount

# Print and run function
print(words(input('Paste your text... ' )))

# Exit or continue
while True:
	Count = input('Continue? y/n ' )
	if Count == ('y'):
		print(words(input('Paste your text... ' )))
	elif Count == ('n'):
		exit()
	else:
		print('invalid character')