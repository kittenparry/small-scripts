import os
import io
import sys


'''
Usage in command line:
>Python Reader.py manifest.txt
Creates a list of files in the current dir and subdirs to 'manifest.txt'
which will be placed to the current directory
Needs the absolute location of Reader.py if it's in a different location
You can remove sys.argv[1] and get rid of file variable for a static filename
'''
class Reader():
    def __init__(self, file):
        archive = ''
        for dirname, dirnames, filenames in os.walk(os.getcwd()):
            print('.', end='')
            #print path to all subdirectories first
            for subdirname in dirnames:
                archive += os.path.join(dirname, subdirname) + '\n'
            #print path to all filenames
            for filename in filenames:
                archive += os.path.join(dirname, filename) + '\n'
        try:
            with io.open(str(file), 'w', encoding='utf8') as f:
                f.write(archive)
        except IOError:
            print('error')

if __name__ == '__main__':
    app = Reader(sys.argv[1])
