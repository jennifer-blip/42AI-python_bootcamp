import sys
import random

nb = random.randint(1, 99)
count = 0

print(nb)
sys.exit(0)
while True :
	guess = input ("What's your guess between 1 and 99\n")
	try :
		guess = int (guess)
	except ValueError:
		if guess == 'q' :
			print ("Goodbye!")
			sys.exit(0)
		print ("ERROR : enter a integer")
		continue
	if guess not in range (1, 100):
		print ("the number is out of range")
		continue
	count += 1
	if guess > nb :
		print ("too high")
		continue
	if guess < nb :
		print ("too low")
		continue
	attempt = "attempt" if count == 1 else "attempts"
	print(f"Congratulations! You've got it!\nYou won in {count} {attempt}!")
	if nb == 42 :
		print("The answer to the ultimate question of life, the universe and everything is 42.")
	if count == 1 :
		print("Congratulations! You got it on your first try!")
	break