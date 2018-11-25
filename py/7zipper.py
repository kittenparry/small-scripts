import os
import subprocess
import sys
import shutil

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
        Display the filesize for folders as well
'''
def seven_zip(pword, d):
    path_7z = r"C:\Program Files\7-Zip\7z.exe"
    zname = os.getcwd().split('\\')[-1].encode('utf-8').hex()
    temp_dir = os.getcwd().split(":\\")[0] + ":\\__7zipper_temp"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    zloc = temp_dir + "\\" + zname
    cmd = r'"{}" a "{}" "{}" -p"{}" -mhe=on -mx0'.format(path_7z, zloc, ".", pword)
    subprocess.call(cmd, shell=True)
    if d == "-d":
        try:
            shutil.rmtree(os.curdir)
        except:
            pass
        os.rename(zloc + ".7z", os.getcwd() + "\\" + zname + ".7z")
        os.rmdir(temp_dir)
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
def strings(s):
    str = {
        "f_size": "{} files, {}.",
        "err_d": "Usage: 7zipper.py -d password",
        "err_arg": "Only 2 arguments are allowed.\nUse quotes for special characters in the password.",
    }
    return str.get(s)

if __name__ == '__main__':
    if len(sys.argv) <= 3:
        try:
            arg2 = sys.argv[2]
        except IndexError:
            arg2 = None
        if sys.argv[1] == "-s": #only -s
            app = file_size()
        elif sys.argv[1] == "-d" and arg2 is None: #don't accept -d
            print(strings("err_d"))
        elif sys.argv[1] == "-d" and arg2 is not None: #-d password
            seven_zip(arg2, sys.argv[1])
        elif sys.argv[1] == sys.argv[-1]: #only password
            seven_zip(sys.argv[1], "")
    else:
        print(strings("err_arg"))
