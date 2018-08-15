REM copies myLogs.txt and Logs\ to different partitions

SET dl=D E F G H I J K
SET lo=:\_logs\latest_logs\
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
