@echo off
@title=Python-Calcutator-Lite Setup
:m
cls
echo Python-Calcutator-Lite Setup
echo Which Version Do You Want To Install?
echo 1.Python-Calcutator-Lite-TR
echo 2.Python-Calcutator-Lite-EN
echo Choose:
set input=nothing
set/p input=Choose:
if %input%==1 goto one
if %input%==2 goto two
goto m
:one
echo Python-Calcutator-Lite-TR Version will be downloaded.
pause
copy INSTALL/TR/calc C:\Users\%users%\
pause
exit
goto m
:two
echo Python-Calcutator-Lite-EN Version will be downloaded.
pause
copy INSTALL/EN/calc C:\Users\%users%\
pause
exit