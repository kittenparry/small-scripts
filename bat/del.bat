REM deletes unnecessary files from torrents in %dl%:\Archive\porn

SET x=:\Archive\porn\
SET dl=D E F G H I J K
FOR %%a IN (%dl%) DO (
	%%a:
	CD %%a%x%
	DEL /S /F *.nfo *.diz *.exe *.dat
)
PAUSE
