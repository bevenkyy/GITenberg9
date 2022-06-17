@ECHO OFF

SET batFileDir=%cd%
SET pythonExeFilePath=iPyGIRS\python-3.7.5-embed-amd64\python.exe
SET MainWindowFilePath=iPyGIRS\appUI\MainWindow.py
SET pythonExeAbsFilePath=%batFileDir%%pythonExeFilePath%
SET MainWindowAbsFilePath=%batFileDir%%MainWindowFilePath%
SET "spaceChar= "
SET RunCommand=%pythonExeAbsFilePath%%spaceChar%%MainWindowAbsFilePath%

ECHO. 

ECHO iPyGIRS-V0.2.0 application is starting, please wait a moment...

ECHO. 

%RunCommand%

PAUSE