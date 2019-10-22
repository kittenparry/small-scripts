REM RPA Extractor command with a for loop to help the extraction of all files in a path
REM Usage rpa_extractor.bat path output_folder_name

F:
CD "F:\_rpaextractor"
FOR %%a IN (%1\*.rpa) DO rpaextractor -v -x "%%a" -o out\%2
