REM deletes unnecessary files from torrents in %dl%:\Archive\porn
REM DEL /S /F *.nfo *.diz *.exe *.dat

SET x=:\Archive\porn\
SET dl=D E F G H I J
FOR %%a IN (%dl%) DO (
	%%a:
	CD %%a%x%
	DEL /S /F *.nfo *.diz *.exe *.dat
)
PAUSE
