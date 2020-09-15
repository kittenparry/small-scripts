@ECHO OFF
REM organise downloads directory using pddcat
REM https://github.com/kittenparry/pddcat
REM direct port of its bash counterpart:
REM https://github.com/kittenparry/dot-files/blob/master/.scripts/ordwn

SET pdd=D:\git\pddcat\pddcat.py
SET dwn=D:\dwnWin4
SET arch=D:\archxdwn\porn

CALL move.bat
python %pdd% -ts %dwn%\f.img -td %arch%\img
python %pdd% -ts %dwn%\f.vid -td %arch%\vid
