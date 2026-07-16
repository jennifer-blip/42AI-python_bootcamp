import sys

if len(sys.argv) < 2 :
	print("USAGE : please enter an integer as argument")
	sys.exit(1)
if len(sys.argv) > 2 : 
	print ("ERROR : please enter only one integer as argument")
	sys.exit(1)
if not sys.argv[1].isdigit() :
	print ("ERROR : argument is not an integer")
	sys.exit(1)

number = int(sys.argv[1])
if number == 0 :
	print ("I'm Zero")
elif number % 2 == 0 :
	print ("I'm even")
else :
	print ("I'm Odd")