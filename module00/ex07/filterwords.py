import sys
import string

if len(sys.argv) != 3 :
	print ("USAGE : filterwords STRING INTEGER")
	sys.exit(1)

try :
	nb = int(sys.argv[2])
except :
	print ("ERROR : argument is not an integer", sys.argv[2])
	sys.exit(1)
result = [word for word in sys.argv[1].translate(sys.argv[1].maketrans("", "", string.punctuation)).split(' ') if len(word) >= nb]
print(result)
