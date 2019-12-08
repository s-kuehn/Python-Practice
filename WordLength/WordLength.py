import re

# Function to find length of characters in a word.
def Num(inputWord):
	re.sub(r'[\W_]+', '',inputWord)
	ans = len(inputWord.replace(" ",""))
	return(f'Length is {ans}')

# Print and run function
print(Num(input('Type a word. ' )))

# Exit or continue
while True:
	Cont = input('Continue? y/n ' )
	if Cont == ('y'):
		print(Num(input('Type a word. ' )))
	elif Cont == ('n'):
		exit()
	else:
		print('invalid character')
