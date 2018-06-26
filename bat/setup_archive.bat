REM Archive folder setup in different drives

SET dl=D E F G H I J
SET l=:\Archive\

SET g=games
SET m=music
SET p=porn
SET s=series

FOR %%a IN (%dl%) DO (
	%%a:
	MD %%a%l%
	CD %%a%l%
	CALL :mf
)
:mf
MD books documentaries %g% %g%\nsfw %g%\oth %g%\sfw images movies %m% %m%\live_footage %m%\to_check oth %p% %p%\animu %p%\jav %p%\mango %p%\pics %p%\unorganised %p%\vids programs %s% %s%\one %s%\many sports
EXIT /B 0