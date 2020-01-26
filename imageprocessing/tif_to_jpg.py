import os
import sys
from PIL import Image

def Usage():
    print('usage: %s <path> <filename>' % (sys.argv[0]))
    sys.exit(1)

if len(sys.argv) != 3:
    Usage()

path = sys.argv[1]
infile = os.path.join(path, sys.argv[2])
Image.MAX_IMAGE_PIXELS = None

f, e = os.path.splitext(infile)
outfile = f + ".jpg"

if infile != outfile:
        try:
            Image.open(infile).save(outfile,  quality=100)
        except IOError:
            print("cannot convert", infile)
