import sys

if len(sys.argv) != 3 :
	print("USAGE : operations.py int1 int2")
	sys.exit(1)
# if not (arg.isnumeric() for arg in sys.argv[1:]) :
# 	print("ERROR : arguments are not integers")
# 	sys.exit(1)
try:
   a = int(sys.argv[1])
   b = int(sys.argv[2])
except:
   print ("ERROR : argument is not integer", sys.argv[1:])
   sys.exit(1)
print("Sum: ", a+b)
print("Difference: ", a-b)
print("Product: ", a*b)
if b == 0 :
	print("Quotient : Error - Division by 0 is impossible")
	print("Remainder : Error - Division by 0 is impossible")
else :
	print("Quotient: ", a/b)
	print("Remainder: ", a%b)