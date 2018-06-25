REM deletes unnecessary files from torrents in %l%:\Archive\porn
REM DEL /S /F *.nfo *.diz *.exe *.dat
SET x=:\Archive\porn\*.nfo *.diz *.exe *.dat
SET dl=D E F G H I J
FOR %%a IN (%dl%) DO DEL /S /F %%a%x%
PAUSE