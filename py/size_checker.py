import os

'''
    Usage in command line after navigating to the desired folder:
    >size_checker.py
        Prints out the number and total size of all files in a folder.
'''
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
    app = file_size()
