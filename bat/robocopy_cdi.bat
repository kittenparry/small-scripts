REM backs up compressed files folder using ROBOCOPY

SET l=D E F G H I J K
SET p=:\_bup2\c
FOR %%a IN (%l%) DO (
	%%a:
	MD %%a%p%
	ROBOCOPY "F:\_temp\c" "%%a%p%" /MIR /DCOPY:T
)
ROBOCOPY "F:\_temp\c" "F:\Google Drive\Other\Archived\Compressed\c" /MIR /DCOPY:T

PAUSE
