REM Zips SuicideGirls folders with appropriate names
REM and moves zips to the Google Drive folder
REM then moves folders to the parent directory

SET sgp="F:\Google Drive\Photos\Inappropriate\SuicideGirlsdotcom"
FOR /D %%d IN (*.*) DO "C:\Program Files\7-Zip\7z.exe" a -tzip "%%d.zip" ".\%%d\*"
MOVE *.zip %sgp%
FOR /d %%f IN (*.*) DO (
	IF NOT %%f==sg_archive.bat (
		CD %%f
		MD ..\..\%%f\
		FOR %%i IN (*.*) DO MOVE %%i ..\..\%%f\
		CD ..
		RMDIR /S /Q %%f
	)
)