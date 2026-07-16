import sys

def test():
	if len(sys.argv) < 2 :
		print ("Please enter an argument")
		sys.exit(1)

	# if __name__ == "__main__":
		# for arg in reversed(sys.argv[1:]) : 
		# 	print(arg[::-1].swapcase(), end=' ')
	# print('')
	print(" ".join(arg[::-1].swapcase() for arg in reversed(sys.argv[1:])))