import os
import subprocess

'''
    Creates archives with all the folders/files in a folder
    Adds password protection, encrypted file names, no compression
    Archives are named after the hexadecimal value of the current directory
    Work in progress.............
    TODO:
        Pword to cmd argument
        Del files afterwards
'''
def seven_zip(pword):
    path_7z = r"C:\Program Files\7-Zip\7z.exe"
    cwd = os.getcwd()
    zname = os.path.dirname(os.path.realpath(__file__)).split('\\')[-1]
    zname_hex = str(zname).encode('utf-8').hex()
    files1 = [f for f in os.listdir(os.curdir)]
    files2 = os.listdir(os.curdir)
    #print(os.listdir(os.curdir))
    #print(files)

    cmd = r'"{}" a "{}" "{}" -p"{}" -mhe=on -mx0'.format(path_7z, zname_hex, ".", pword)
    subprocess.call(cmd, shell=True)

#Swap below with "" for manual password entry
seven_zip(1)
