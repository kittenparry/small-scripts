REM backs up scripts folders using ROBOCOPY
REM TODO: remove repetition

ROBOCOPY "D:\git\small-scripts" "F:\Google Drive\Programs\small-scripts" /MIR /DCOPY:T /XD .git
ROBOCOPY "D:\git\userscripts" "F:\Google Drive\Programs\userscripts" /MIR /DCOPY:T /XD .git
ROBOCOPY "D:\git\userscripts-private" "F:\Google Drive\Programs\userscripts-private" /MIR /DCOPY:T /XD .git
PAUSE
