import string
import sys

def text_analyzer(text=None) :
	"""This function counts the number of upper letters, lower letters, punctuation marks and spaces in the text argument."""
	if text is None :
		text = input("please enter a text to analyze : ")

	if not isinstance(text, str) :
		print("ERROR : the argument is not a string")
		return
	up = 0
	low = 0
	punc = 0
	spa = 0
	pri = 0
	for char in text :
		if char in string.punctuation :
			punc += 1
		elif char in string.ascii_uppercase :
			up += 1
		elif char in string.ascii_lowercase :
			low += 1
		elif char in string.whitespace :
			spa += 1
		if char in string.printable :
			pri += 1
	print(f"""the text contains : 
	- {pri} printable characters,
	- {up} upper letter(s),
	- {low} lower letter(s),
	- {punc} punctuation mark(s),
	- {spa}  space(s))""")

if len(sys.argv) > 2 :
	print ("Please enter only one argument")
	sys.exit(1)
if len(sys.argv) < 2 :
	text_analyzer()
else :
	text_analyzer(sys.argv[1])