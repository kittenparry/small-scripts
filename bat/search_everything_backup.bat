REM copies Search Everything run and search history to dated folders in Google Drive
REM formatted date is yyyy-mm-dd if %date% is eee dd/mm/yyyy

SET sel=C
SET sep=:\Users\Edvin\AppData\Roaming\Everything
SET gdp=F:\Google Drive\Other\Backups\Search Everything\%date:~10,4%-%date:~4,2%-%date:~7,2%\

%sel%:
CD %sel%%sep%
MD "%gdp%"
COPY *.csv "%gdp%"
