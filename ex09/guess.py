from random import randint

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!\n")

random_number = randint(1, 99)
print(random_number)
guessed = False
guess = 0
attempts = 0
while guessed == False and guess != "exit":
	guess = input("What's your guess between 1 and 99?\n")
	if guess.isdigit():
		if (int(guess) == random_number):
			guessed = True
			print("Congratulations, you've got it!")
		elif (int(guess) > random_number):
			print("Too high!")
		elif (int(guess) < random_number):
			print("Too low!")
	elif (guess == "exit"):
		continue
	else:
		print("That's not a number.")
	attempts += 1
if guessed == True:
	print(f'You won in {attempts} attempts!')