import sys
import string

numArgs = len(sys.argv)
if numArgs != 3:
	print("ERROR")
elif type(sys.argv[1]) != str or sys.argv[2].isdigit() == False:
	print("ERROR")
else:
	lst = sys.argv[1].split()
	for word in lst:
		lst[lst.index(word)] = word.translate(str.maketrans('', '', string.punctuation))
	lst = [word for word in lst if len(word) > int(sys.argv[2])]
	print(lst)
