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
            "7zipper.py p -d" vs "7zipper.py p" for example?
        Display the filesize for folders as well
        Maybe place another safeguard to prevent more than 2 arguments
'''
def seven_zip(pword, d):
    path_7z = r"C:\Program Files\7-Zip\7z.exe"
    zname = os.getcwd().split('\\')[-1].encode('utf-8').hex()
    #files = [os.listdir(os.curdir)]
    files = [f for f in os.listdir(os.curdir)]
    cmd = r'"{}" a "{}" "{}" -p"{}" -mhe=on -mx0'.format(path_7z, zname, ".", pword)
    subprocess.call(cmd, shell=True)
    if d == "-d":
        print("-d")
        #recursive folder/file removal below
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
    print(strings("f_size").format(len(files), convert_bytes(fsize)))
def del_files():
    print("del files")
def strings(s):
    str = {
        "f_size": "{} files, {}.",
        "err_d": "Usage: 7zipper.py -d password",
    }
    return str.get(s)

if __name__ == '__main__':
    try:
        arg2 = sys.argv[2]
    except:
        arg2 = None
    if sys.argv[1] == "-s": #only -s
        app = file_size()
    elif sys.argv[1] == "-d" and arg2 is None: #don't accept -d
        print(strings("err_d"))
    elif sys.argv[1] == "-d" and arg2 is not None: #-d password
        seven_zip(arg2, sys.argv[1])
    elif sys.argv[1] == sys.argv[-1]: #only password
        seven_zip(sys.argv[1], "")
