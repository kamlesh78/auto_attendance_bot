@echo off
CLS
color 0A
echo "wait opening web browser"
CD %USERPROFILE%\selenium-temp\Scripts
activate.bat & CD %USERPROFILE%\Desktop & python autoattendance.py 


 
