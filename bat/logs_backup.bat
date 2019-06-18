REM copies myLogs.txt and Logs\ to different partitions

SET dll=D E F G H I J K
SET lp=_logs\latest_logs\
SET lo=:\%lp%
SET gd=F
SET dl=:\Dropbox\
SET gl=:\Google Drive\Other\
SET ll=Logs\
SET n=myLogs.txt

REM Dropbox COPY below, needs cleaning up
%gd%:
CD %gd%%dl%
MD %gd%%dl%%lp%
MD %gd%%dl%%lp%%ll%
CD %gd%%gl%
COPY %n% %gd%%dl%%lp%%n%
COPY %ll%*.txt %gd%%dl%%lp%%ll%*.txt

REM different drives COPY below
FOR %%a IN (%dll%) DO (
	%%a:
	MD %%a%lo%
	MD %%a%lo%%ll%
	%gd%:
	CD %gd%%gl%
	COPY %n% %%a%lo%%n%
	COPY %ll%*.txt %%a%lo%%ll%*.txt
)

EXIT

REM IDEAS
REM zip instead of directly copying?
