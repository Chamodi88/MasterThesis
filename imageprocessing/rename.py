import os 
import sys

def Usage():
    print('usage: %s <path> ' % (sys.argv[0]))
    sys.exit(1)

if len(sys.argv) != 2:
    Usage()

path = sys.argv[1]
    
files = os.listdir(path)
i = 1

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, 'image' + str(i)+'.jpg'))
    i = i+1