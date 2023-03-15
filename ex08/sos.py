import sys
CHARS_TO_MORSE_CODE_MAPPING = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----'
}

num_args = len(sys.argv)

if num_args > 1:
	str = " ".join(sys.argv[1:])
	if all(x.isalnum() or x.isspace() for x in str):
		morse_code = ''
		for char in str:
			if char == ' ':
				morse_code += '/ '
			else:
				morse_code += CHARS_TO_MORSE_CODE_MAPPING[char.upper()] + ' '
		print(morse_code)
	else:
		print("ERROR")