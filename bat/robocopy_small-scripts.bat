REM backs up small-scripts folder using ROBOCOPY

ROBOCOPY "D:\git\small-scripts" "F:\Google Drive\Programs\small-scripts" /MIR /DCOPY:T /XD .git
PAUSE
