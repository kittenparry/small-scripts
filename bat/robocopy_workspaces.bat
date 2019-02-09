REM backs up workspaces using ROBOCOPY

SET g=F:\Google Drive\Workspaces\
SET a=/MIR /DCOPY:T
SET r=ROBOCOPY

%r% "D:\androidstudio" "%g%androidstudio" %a%
%r% "D:\codeblocksworkspace" "%g%codeblocks" %a%
%r% "D:\eclipseworkspace" "%g%eclipse" %a%
%r% "D:\git" "%g%git" %a%
%r% "D:\intelliJworkspace" "%g%intelliJ" %a%
%r% "D:\photoshopworkspace" "%g%photoshop" %a%
%r% "D:\pycharmworkspace" "%g%pycharm" %a%
%r% "D:\renpyworkspace" "%g%renpy" %a%
%r% "D:\visualcodestudioworkspace" "%g%vscode" %a%
%r% "D:\webstormworkspace" "%g%webstorm" %a%
PAUSE
