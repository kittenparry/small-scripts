import shutil
import glob
import os

'''
Usage in command line:
>Python Move.py
Moves some or all contents of a folder with its subfolders
Moves folders from the current working directory
You can remove filetypes, related loop and string
if in need to move all the files
'''

class Move():
    def __init__(self):
        names = ([name for name in os.listdir(".") if os.path.isdir(name)])
        #add or remove filetypes as required
        filetypes = ['rar', 'zip']
        for name in names:
            #remove the loop below and...
            for type in filetypes:
                dst = 'D:/estination/folder/' + str(name) + '/'
                if not os.path.exists(dst):
                    os.makedirs(dst)
                #change '/*.' + str(type) into '/*.*' if need to move all the files
                for file in glob.glob(r'' + str(name) + '/*.' + str(type)):
                    print(file)
                    shutil.move(file, dst)

if __name__ == '__main__':
    app = Move()
