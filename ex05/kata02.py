kata = (2019, 9, 25, 3, 30)
copyKata = list(kata)
for i in range(5):
	copyKata[i] = str(copyKata[i])
	if (len(copyKata[i]) == 1):
		copyKata[i] = '0' + copyKata[i]
print(f'{copyKata[1]}/{copyKata[2]}/{copyKata[0]} {copyKata[3]}:{copyKata[4]}')
