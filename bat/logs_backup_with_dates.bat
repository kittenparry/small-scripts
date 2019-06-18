REM copies myLogs.txt and Logs\ to different partitions with dates
REM %d% is yyyy-mm-dd if %date% is eee dd/mm/yyyy

SET d=%date:~10,4%-%date:~4,2%-%date:~7,2%
SET dl=D E F G H I J K
SET lo=:\_logs\archived_logs\%d%\
SET gd=F
SET gl=:\Google Drive\Other\
SET ll=Logs\
SET n=myLogs.txt

FOR %%a IN (%dl%) DO (
	%%a:
	MD %%a%lo%
	MD %%a%lo%%ll%
	%gd%:
	CD %gd%%gl%
	COPY %n% %%a%lo%%n%
	COPY %ll%*.txt %%a%lo%%ll%*.txt
)

EXIT
