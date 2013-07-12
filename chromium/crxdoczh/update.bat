@echo off
xcopy /s /e /y /exclude:exclude.txt ..\official\src\*.* .\src\
svn stat
