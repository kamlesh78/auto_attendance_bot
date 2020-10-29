# auto_attendance_bot
browser automation to mark attendance using python bot


setup.bat :  
This is just a setup file to automate all configuration needed for auto_attendace_bot to run.
This batch script will create python virtual environment in the root directory i.e `%USERPROFILE%`.
It will also install `selenium` lib by activating the virtual environment


run.bat :                                                                                                                                                                
This batch script will automate all the process of activating virtual environment and running the python scrip from your Desktop.


autoattendance.py : python script to mark your attendace in gehu moddle.

Note: You need to download webdriver for the web browser you are using and copy the web driver to `C:\driver\` directory(create directory driver in C:\ driver if not exist already).


          * Download Firefox webdriver from https://github.com/mozilla/geckodriver/releases 
          
          * Download Chrome webdriver from https://chromedriver.chromium.org/downloads
          
          *** similarly you can download webdriver for your web browser supprorted by selenium***
          
         
   IMP: if you are using Chrome web browser replace webdriver.Firefox with webdriver.Chrome in line 5 of autoattendance.py. 
        Similary if you are using any other browser replace Firefox with name of that browser.
 
