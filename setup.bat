@echo off
CLS
color 0A
echo "creating virtual environment!! wait for few seconds !!  " 
CD %USERPROFILE%
python -m venv selenium-temp
echo "now installing selenium wait!"
CD %USERPROFILE%\selenium-temp\Scripts
activate.bat & pip install selenium & exit

 
