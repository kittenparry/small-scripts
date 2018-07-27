REM Zips SuicideGirls folders with appropriate names
REM and moves zips to the Google Drive folder
REM then moves folders to the parent directory

SET sgp="F:\Google Drive\fromPC\SuicideGirls.com"
SET sgd=F
SET sgl=:\_suicidegirls\__n\
%sgd%:
CD %sgd%%sgl%
FOR /D %%d IN (*.*) DO "C:\Program Files\7-Zip\7z.exe" a -tzip "%%d.zip" ".\%%d\*"
MOVE *.zip %sgp%
FOR /D %%f IN (*.*) DO (
	CD %%f
	MD ..\..\%%f\
	FOR %%i IN (*.*) DO MOVE %%i ..\..\%%f\
	CD ..
	RMDIR /S /Q %%f
)
