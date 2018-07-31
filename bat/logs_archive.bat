REM copies myLogs.txt to Logs\ with dates
REM %d% is (yyyy-mm-dd) if %date% is eee dd/mm/yyyy

SET dl=F
SET lo=:\Google Drive\Other
SET d=(%date:~10,4%-%date:~4,2%-%date:~7,2%)

%dl%:
CD %dl%%lo%
COPY myLogs.txt Logs\myLogs%d%.txt
PAUSE
