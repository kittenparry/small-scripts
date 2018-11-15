REM Creates the folders for my downloads folder
REM and puts files to their places

REM SET and CD to the downloads folder
SET dh=I
SET dl=:\Downloads.old3
%dh%:
CD %dh%%dl%

REM SET folder names
SET t=f.torrent
SET i=f.img
SET w=f.webm
SET e=f.exe
SET c=f.comp
SET v=f.vid
SET o=f.oth

REM SET extensions
SET te=.torrent
SET ie=.jpg .png .gif .jpeg .bmp .webp
SET we=.webm
SET ee=.exe .msi
SET ce=.rar .zip .7z .dmg
SET ve=.mp4 .avi .flv .ts .mov .wmv .mkv .3gp .m4v .mpg
SET oe=.pdf .mp3 .txt .iso .docx .rtf .svg .js .pptx .doc
SET oe2=.m4a .html .css .ogg .xlsx .gz .azw3 .mobi .log .jar
SET oe3=.scs .swf .ods .db .xml .ini .sh .php .ogx .save
SET oe4=.htmlz .h .class .rpa .rpy .sav .package .ttf .bk2 .csv

MD %t% %i% %w% %e% %c% %v% %o%
FOR %%a IN (%te%) DO MOVE *%%a %t%
FOR %%a IN (%ie%) DO MOVE *%%a %i%
FOR %%a IN (%we%) DO MOVE *%%a %w%
FOR %%a IN (%ee%) DO MOVE *%%a %e%
FOR %%a IN (%ce%) DO MOVE *%%a %c%
FOR %%a IN (%ve%) DO MOVE *%%a %v%
FOR %%a IN (%oe%, %oe2%, %oe3%, %oe4%) DO MOVE *%%a %o%
