REM backs up compressed files folder using ROBOCOPY

SET l=D E G H I J K
SET p=:\632d66696c6573\636469
SET lo=F%p%
FOR %%a IN (%l%) DO (
	%%a:
	MD %%a%p%
	ROBOCOPY "%lo%" "%%a%p%" /MIR /DCOPY:T
)
ROBOCOPY "%lo%" "F:\Google Drive\Other\Archived\Compressed\636469" /MIR /DCOPY:T
PAUSE
