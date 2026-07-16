import sys
import string

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ' ' : '/'}

def encrypt(message) :
	result = ""
	for letter in message :
		result += MORSE_CODE_DICT[letter] + " "
	return (result)

if len(sys.argv) < 2 :
	print ("USAGE : sos 'ALPHANUMERIC TEXT TO TRANSLATE'")
	sys.exit (1)

if not all ((c.isalnum() or c.isspace()) for arg in sys.argv[1:] for c in arg) :
	print ("USAGE : sos 'ALPHANUMERIC TEXT TO TRANSLATE'")
	sys.exit(1)

args = [words.strip() for words in sys.argv[1:]]
text = " ".join(args).upper()

print (encrypt(text))


