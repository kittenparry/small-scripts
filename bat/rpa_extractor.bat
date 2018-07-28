REM RPA Extractor command with a for loop to help the extraction of all files in a path
REM Usage rpa_extractor.bat path output_folder_name

SET rp="I:\Downloads.old3\f.folder\RPA Extractor for Windows"
SET rl=I
%rl%:
CD %rp%
FOR %%a IN (%1\*.rpa) DO rpaextractor -x %%a -o %2
