import sys

n = len(sys.argv)
if (n > 1):
	str = ' '.join(sys.argv[1:])
	str = str[::-1] 
	print(str.swapcase())