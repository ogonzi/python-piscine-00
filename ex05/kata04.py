from decimal import Decimal

kata = (0, 4, 132.42222, 1000, 12345.67)
copyKata = list(kata)
copyKata[0] = str(copyKata[0])
copyKata[1] = str(copyKata[1])
copyKata[2] = round(copyKata[2], 2)
if (len(copyKata[0]) == 1):
	copyKata[0] = '0' + copyKata[0]
if (len(copyKata[1]) == 1):
	copyKata[1] = '0' + copyKata[1]

print(f'module_{copyKata[0]}, ex_{copyKata[1]} : {copyKata[2]}, ' + '{:.2e}'.format(copyKata[3]) + ', {:.2e}'.format(copyKata[4]))