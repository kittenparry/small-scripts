import os
import sys

def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0
'''
def file_size(file_path):
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)
'''
#file_path = r"J:\jdownloader7\6a646f776e6c6f6164657237.7z"
#print(file_size(file_path))
#files = os.listdir(os.curdir)
files = [f for f in os.listdir(os.curdir) if os.path.isfile(f)]
fsize = 0
for file in files:
    fsize += os.stat(file).st_size

print(files)
print(fsize)
print (convert_bytes(fsize))

#if __name__ == '__main__':
#    app = seven_zip(sys.argv[1])
