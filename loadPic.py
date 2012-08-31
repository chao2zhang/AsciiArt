import Image
import ImageFont, ImageDraw

data_file = open('result.txt', 'w')

arr = []

for o in range(32, 128):
    c = str(chr(o))
    f = ImageFont.truetype('DejaVuSansMono.ttf', 32)
    i = Image.new('RGBA', (20, 40), (255, 255, 255, 255))
    d = ImageDraw.Draw(i)
    d.text((0, 0), c, font=f, fill='black')
    #print c
    #i.save('font/%i.png' % o)
    pix = i.load()
    maxx, maxy = i.size
    sumrgba = (float(0), float(0), float(0), float(0))
    for x in range(0, maxx):
        for y in range(0, maxy):
            sumrgba = map(lambda x,y: x + y, sumrgba, pix[x, y])
    sumrgba = map(lambda x: x / (maxx * maxy), sumrgba)
    print chr(o), sumrgba
    data_file.write('%i:%s\r\n' % (o, sumrgba))
    arr.append((c, sumrgba[0] + sumrgba[1] + sumrgba[2]))

data_file.write('Sorted:\r\n')
arr.sort(lambda x, y: int(x[1] - y[1]))
for d in map(lambda x: '%s:%f' % (x[0], x[1]), arr):
    data_file.write('%s\r\n' % d)

data_file.write('\r\nJust ascii value:\r\n')
arr = map(lambda x: ord(x[0]), arr)
data_file.write(str(arr))

data_file.close()
