from PIL import Image
import os
import sys

def Usage():
    print('usage: %s <path> <filename> <tile_width>' % (sys.argv[0]))
    sys.exit(1)

if len(sys.argv) != 4:
    Usage()


path = sys.argv[1]
infile = os.path.join(path, sys.argv[2])
outputpath = os.path.join(path, sys.argv[2].split('.')[0])
Image.MAX_IMAGE_PIXELS = None

os.mkdir(os.path.join(path,sys.argv[2].split('.')[0]))

image = Image.open(infile)
tile_width = int(sys.argv[3])
tile_height = int(sys.argv[3])

if image.size[0] > tile_width and image.size[1] > tile_height:
    currentx = 0
    currenty = 0
    k = 1
    while currenty < image.size[1]:
        while currentx < image.size[0]:
            tile = image.crop((currentx,currenty,currentx + tile_width,currenty + tile_height))
            tile.save(os.path.join(outputpath, sys.argv[2].split('.')[0] + "_" + str(k) +  ".jpg"))
            currentx += tile_width
            k += 1
        currenty += tile_height
        currentx = 0
else:
    print("Error: your image does not fit neatly into",tile_width,"*",tile_height,"tiles")
