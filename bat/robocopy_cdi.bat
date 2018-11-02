REM backs up compressed files folder using ROBOCOPY

SET l=D E G H I J K
SET p=:\Archive\oth\cdi
SET lo=F%p%
FOR %%a IN (%l%) DO (
	%%a:
	MD %%a%p%
	ROBOCOPY "%lo%" "%%a%p%" /MIR /DCOPY:T
)
ROBOCOPY "%lo%" "F:\Google Drive\Other\Archived\Compressed\cdi" /MIR /DCOPY:T

PAUSE
