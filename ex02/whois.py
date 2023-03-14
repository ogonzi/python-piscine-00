import sys

numArgs = len(sys.argv)
assert numArgs <= 2, "more than one argument are provided"
if (numArgs == 2):
	arg = sys.argv[1]
	assert arg.isdigit(), "argument is not an integer"
	if int(arg) == 0:
		print("I'm Zero.")
	elif int(arg) % 2 == 0:
		print("I'm Even.")
	else:
		print("I'm odd.")
