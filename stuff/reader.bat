REM Creates a list of files in the current dir and subdirs to a text file
REM which will be placed to the current directory
REM Doesn't output in Unicode, unlike Reader.py

REM With files (Same with Reader.py, but sorted)
dir /s /b | sort > manifest_dirs_files.txt

REM Without files
dir /a:d /s /b | sort > manifest_dirs.txt
