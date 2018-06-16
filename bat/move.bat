REM Creates the folders for my downloads folder
REM and puts files to their places

REM Set folder names
SET t=f.torrent
SET i=f.img
SET w=f.webm
SET e=f.exe
SET c=f.comp
SET v=f.vid
SET o=f.oth

REM Set extensions
SET te=.torrent
SET ie=.jpg .png .gif .jpeg
SET we=.webm
SET ee=.exe .msi
SET ce=.rar .zip .7z .dmg
SET ve=.mp4 .avi .flv .ts .mov .vmw .mkv .3gp .m4v .mpg
SET oe=.pdf .mp3 .txt .iso .docx .rtf .svg .js .pptx .doc .m4a .html .css .ogg .xlsx .gz .azw3 .mobi .log .jar .scs .swf .ods .db .xml .ini .sh .php

MD %t% %i% %w% %e% %c% %v% %o%
FOR %%a IN (%te%) DO MOVE *%%a %t%
FOR %%a IN (%ie%) DO MOVE *%%a %i%
FOR %%a IN (%we%) DO MOVE *%%a %w%
FOR %%a IN (%ee%) DO MOVE *%%a %e%
FOR %%a IN (%ce%) DO MOVE *%%a %c%
FOR %%a IN (%ve%) DO MOVE *%%a %v%
FOR %%a IN (%oe%) DO MOVE *%%a %o%
