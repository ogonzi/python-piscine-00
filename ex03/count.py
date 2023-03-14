import string

def text_analyzer(text):
	'''Takes in a string, counts and prints the number of uppercase, lowercase
	punctuation and space characters'''
	if text == None:
		print("Please introduce a string")
		return
	if isinstance(text, str) == False:
		print("Error: Text is not a string")
		return
	if len(text) == 0:
		print("Please introduce a string")
		return
	countUppercase = sum(1 for c in text if c.isupper())
	countLowercase = sum(1 for c in text if c.islower())
	countPunctuationMark = sum(1 for c in text if c in string.punctuation )
	countSpace = sum(1 for c in text if c.isspace())
	print(f'The text contains {len(text)} character(s):')
	print(f'- {countUppercase} upper letter(s)')
	print(f'- {countLowercase} lower letter(s)')
	print(f'- {countPunctuationMark} punctuation mark(s)')
	print(f'- {countSpace} space(s)')
