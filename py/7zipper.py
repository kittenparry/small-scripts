import os
import subprocess
import sys

'''
    Usage in command line after navigating to the desired folder:
    >7zipper.py password
    Creates archives with all the folders/files in a folder
    Adds password protection, encrypted file names, no compression
    Archives are named after the hexadecimal value of the current directory
    Work in progress.............
    TODO:
        Del files afterwards
'''
def seven_zip(pword):
    path_7z = r"C:\Program Files\7-Zip\7z.exe"
    zname = os.getcwd().split('\\')[-1]
    zname_hex = str(zname).encode('utf-8').hex()
    cmd = r'"{}" a "{}" "{}" -p"{}" -mhe=on -mx0'.format(path_7z, zname_hex, ".", pword)
    subprocess.call(cmd, shell=True)

if __name__ == '__main__':
    app = seven_zip(sys.argv[1])
