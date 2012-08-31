import Image, ImageFont, ImageDraw
import tkFileDialog
import sys
import itertools
import math
import numpy

src = tkFileDialog.askopenfilename()

if not src.strip():
	print 'no file'
	sys.exit()

ranks = []

f = open('result.txt', 'r')
for l in f:
	a, b = l.split(',')
	ranks.append((int(a), float(b)))
print ranks

font = ImageFont.truetype('DejaVuSansMono.ttf', 32)

X_STEP = 1
Y_STEP = 2
W_FONT = 20
H_FONT = 40

try:
	i = Image.open(src)
	src_pix = i.load()
	src_x, src_y = i.size
	if src_x % X_STEP > 0: src_x -= src_x % X_STEP
	if src_y % Y_STEP > 0: src_y -= src_y % Y_STEP
	dest = Image.new('RGB', (src_x * W_FONT / X_STEP, src_y * H_FONT / Y_STEP), (255, 255, 255))
	dest_d = ImageDraw.Draw(dest)
	np_pix = numpy.array(srx_pix)
	for x in range(0, src_x, X_STEP):
		for y in range(0, src_y, Y_STEP):
			rgb = [0.0, 0.0, 0.0]
			for r in range(0, 3):
				for ii in range(x, x + X_STEP):
					for jj in range(y, y + Y_STEP):
						rgb[r] += src_pix[ii, jj][r]
			rgb = map(lambda a: a / X_STEP / Y_STEP, rgb)
			gray = math.pow((math.pow(rgb[0], 2.2) * 0.2973 + math.pow(rgb[1], 2.2) * 0.6274 + math.pow(rgb[2], 2.2) * 0.0753), 1 / 2.2)
			dst_x = x * W_FONT / X_STEP
			dst_y = y * H_FONT / Y_STEP
			rank = int(gray / 256 * len(ranks))
			s = str(chr(ranks[rank][0]))
			dest_d.text((dst_x, dst_y), s, font=font, fill='black')
	dest.save('result.jpg')

except IOError, e:
	print e