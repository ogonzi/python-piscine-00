import sys

numArgs = len(sys.argv)
if numArgs == 1:
	print("Usage: python operations.py <number1> <number2>")
	print("Example:\n\t python operations.py 10 3")
else:
	assert numArgs == 3, "should provide 2 arguments"
	assert sys.argv[1].isdigit(), "first argument should be a digit"
	assert sys.argv[2].isdigit(), "second argument should be a digit"

	a = int(sys.argv[1])
	b = int(sys.argv[2])
	sum = a + b
	difference = a - b
	product = a * b
	if (b != 0):
		quotient = a / b
		remainder = a % b
	else:
		quotient = "ERROR (division by zero)"
		remainder = "ERROR (modulo by zero)"

	print(f'Sum:\t\t{sum}')
	print(f'Difference:\t{difference}')
	print(f'Product:\t{product}')
	print(f'Quotient:\t{quotient}')
	print(f'Remainder:\t{remainder}')