kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

kataKeys = list(kata.keys())
kataValues = list(kata.values())
for i in range(3):
	print(f'{kataKeys[i]} was created by {kataValues[i]}')