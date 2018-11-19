import os
import subprocess
import sys

'''
    Usage in command line after navigating to the desired folder:
    >7zipper.py password
    Creates an archive with all the data in a folder
    Adds password protection, encrypted file names, no compression
    Archives are named after the hexadecimal value of the current directory
    Work in progress.............
    >7zipper.py -s
    Displays the number of files and their total size in a folder
    TODO:
        Del files afterwards (as an argumental option (don't del if blank?))
            "7zipper.py p d" vs "7zipper.py p" for example?
        Display the filesize for folders as well
'''
def seven_zip(pword):
    path_7z = r"C:\Program Files\7-Zip\7z.exe"
    zname = os.getcwd().split('\\')[-1].encode('utf-8').hex()
    cmd = r'"{}" a "{}" "{}" -p"{}" -mhe=on -mx0'.format(path_7z, zname, ".", pword)
    subprocess.call(cmd, shell=True)
def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0
def file_size():
    files = [f for f in os.listdir(os.curdir) if os.path.isfile(f)]
    fsize = 0
    for file in files:
        fsize += os.stat(file).st_size
    print("{} files, {}.".format(len(files), convert_bytes(fsize)))

if __name__ == '__main__':
    if sys.argv[1] == "-s":
        app = file_size()
    else:
        app = seven_zip(sys.argv[1])
