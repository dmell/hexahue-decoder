#!/usr/bin/python3
from sys import argv
from PIL import Image

def usage():
	print(f"Usage: python3 {argv[0]} IMAGE [ PADDING (in pixels) ]")

# init colors, to init dictionary more easily
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blu = (0, 0, 255)
yellow = (255, 255, 0)
light_blue = (0, 255, 255)
magenta = (255, 0, 255)
gray = (128, 128, 128)

# init dict
# keys are tuples of tuples of the six colors, values are the decoded values
hexahue = {}
hexahue[(magenta, red, green, yellow, blu, light_blue)] = 'a'
hexahue[(red, magenta, green, yellow, blu, light_blue)] = 'b'
hexahue[(red, green, magenta, yellow, blu, light_blue)] = 'c'
hexahue[(red, green, yellow, magenta, blu, light_blue)] = 'd'
hexahue[(red, green, yellow, blu, magenta, light_blue)] = 'e'
hexahue[(red, green, yellow, blu, light_blue, magenta)] = 'f'
hexahue[(green, red, yellow, blu, light_blue, magenta)] = 'g'
hexahue[(green, yellow, red, blu, light_blue, magenta)] = 'h'
hexahue[(green, yellow, blu, red, light_blue, magenta)] = 'i'
hexahue[(green, yellow, blu, light_blue, red, magenta)] = 'j'
hexahue[(green, yellow, blu, light_blue, magenta, red)] = 'k'
hexahue[(yellow, green, blu, light_blue, magenta, red)] = 'l'
hexahue[(yellow, blu, green, light_blue, magenta, red)] = 'm'
hexahue[(yellow, blu, light_blue, green, magenta, red)] = 'n'
hexahue[(yellow, blu, light_blue, magenta, green, red)] = 'o'
hexahue[(yellow, blu, light_blue, magenta, red, green)] = 'p'
hexahue[(blu, yellow, light_blue, magenta, red, green)] = 'q'
hexahue[(blu, light_blue, yellow, magenta, red, green)] = 'r'
hexahue[(blu, light_blue, magenta, yellow, red, green)] = 's'
hexahue[(blu, light_blue, magenta, red, yellow, green)] = 't'
hexahue[(blu, light_blue, magenta, red, green, yellow)] = 'u'
hexahue[(light_blue, blu, magenta, red, green, yellow)] = 'v'
hexahue[(light_blue, magenta, blu, red, green, yellow)] = 'w'
hexahue[(light_blue, magenta, red, blu, green, yellow)] = 'x'
hexahue[(light_blue, magenta, red, green, blu, yellow)] = 'y'
hexahue[(light_blue, magenta, red, green, yellow, blu)] = 'z'
hexahue[(black, white, white, black, black, white)] = '.'
hexahue[(white, black, black, white, white, black)] = ','
hexahue[(white, white, white, white, white, white)] = ' '
hexahue[(black, black, black, black, black, black)] = ' '
hexahue[(black, gray, white, black, gray, white)] = '0'
hexahue[(gray, black, white, black, gray, white)] = '1'
hexahue[(gray, white, black, black, gray, white)] = '2'
hexahue[(gray, white, black, gray, black, white)] = '3'
hexahue[(gray, white, black, gray, white, black)] = '4'
hexahue[(white, gray, black, gray, white, black)] = '5'
hexahue[(white, black, gray, gray, white, black)] = '6'
hexahue[(white, black, gray, white, gray, black)] = '7'
hexahue[(white, black, gray, white, black, gray)] = '8'
hexahue[(black, white, gray, white, black, gray)] = '9'

if len(argv) < 2 or len(argv) > 3:
	usage()
	exit(1)

filename = argv[1]
padding = int(argv[2]) if len(argv) == 3 else 0

im = Image.open(filename)
width, height = im.size
x = padding
y = padding
plaintext = ""
while y < height-padding:
	current_letter = []
	for j in range(y, y+3):
		for i in range(x, x+2):
			current_letter.append(tuple(im.getpixel((i,j))))
	try:
		plaintext += hexahue[tuple(current_letter)]
	except KeyError:
		print(f"I broke trying to read {tuple(current_letter)}")
		print(f"Flag so far: {plaintext}")
		exit(0)
	x += 2
	# we reached the end of the row of boxes
	if x == width - padding:
		x = padding
		y += 3
	
print(plaintext)