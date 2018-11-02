REM My attempt on moving folders from Downloads to Archive folders.

@ECHO OFF
REM categories like a, j, m, p, u, v
ECHO %0
ECHO %~dp0

REM Goal:
REM E:\downloads\porn\jeff_milton E:\archive\porn\pics\jeff_milton

REM archive_downloads.bat E:\downloads\porn\jeff_milton
ECHO %~dp1
REM E:\downloads\porn\
ECHO %~f1
REM E:\downloads\porn\jeff_milton
ECHO %~d1
REM E:
ECHO %~p1
REM \downloads\porn\
ECHO %~nx1
REM jeff_milton
SET t=%~p1
ECHO %t:~10%
REM \porn\
SET tc=%t:~10%

SET ar=\Archive
SET loc=%~d1%ar%%tc%
ECHO %loc%
REM E:\Archive\porn\

REM SET additional folders
SET a=animu
SET j=jav
SET m=mango
SET p=pics
SET u=unorganised
SET v=vids
SET pl=

REM 2nd arg into additional folder
ECHO %2
IF "%2"=="a" SET pl=%a%\
IF "%2"=="j" SET pl=%j%\
IF "%2"=="m" SET pl=%m%\
IF "%2"=="p" SET pl=%p%\
IF "%2"=="u" SET pl=%u%\
IF "%2"=="v" SET pl=%v%\
REM append to end, before the foldername
SET loc=%loc%%pl%%~nx1
ECHO %loc%
REM E:\Archive\porn\pics\jeff_milton with p
REM uncomment below
REM ROBOCOPY %1 %loc% /MOVE /DCOPY:T
PAUSE
