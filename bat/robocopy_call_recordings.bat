REM backs up callrecordings folder using ROBOCOPY

ROBOCOPY "G:\fromNewPhone\callrecordings" "F:\Google Drive\fromPC\callrecordings" /MIR /DCOPY:T /XF .nomedia
PAUSE
