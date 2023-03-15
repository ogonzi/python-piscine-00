from random import randint

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!\n")

random_number = randint(1, 99)
guessed = False
guess = 0
attempts = 0
while guessed == False and guess != "exit":
	guess = input("What's your guess between 1 and 99?\n")
	if guess.isdigit():
		if (int(guess) == random_number):
			guessed = True
		elif (int(guess) > random_number):
			print("Too high!")
		elif (int(guess) < random_number):
			print("Too low!")
	elif (guess == "exit"):
		print("Goodbye!")
		continue
	else:
		print("That's not a number.")
	attempts += 1
if guessed == True:
	if (random_number == 42):
		print("The answer to the ultimate question of life, the universe and everythin is 42.")
	if (attempts == 1):
		print("Congratulations! You got it on the first try!")
	else:
		print("Congratulations, you've got it!")
		print(f'You won in {attempts} attempts!')