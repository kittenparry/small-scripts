REM Zips SuicideGirls folders with appropriate names
REM and moves them to the Google Drive folder

SET sgp="F:\Google Drive\Photos\Inappropriate\SuicideGirlsdotcom"
FOR /D %%d IN (*.*) DO "C:\Program Files\7-Zip\7z.exe" a -tzip "%%d.zip" ".\%%d\*"
MOVE *.zip %sgp%
REM MOVE folders to parent directory test below
REM XCOPY *.* .. /exclude:archive.bat
PAUSE