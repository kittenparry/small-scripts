REM backs up Google Drive folder using ROBOCOPY
REM /MIR (/E + /PURGE) copies subdirs and deletes elements that doesn't exist in source anymore
REM /DCOPY:T preserves timestamps on folders
REM /XD exclude folder
REM /XF exclude file

ROBOCOPY "F:\Google Drive" "J:\GoogleDriveb" /MIR /DCOPY:T /XD .tmp.drivedownload /XF desktop.ini
PAUSE
