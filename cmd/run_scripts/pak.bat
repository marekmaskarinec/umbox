@echo off
setlocal enabledelayedexpansion

set DIR=%~dp0

for /f "delims=" %%i in ('dir /b "%DIR%dat\pak"') do (
	set "currentDir=%%i"
	set "PATH=!PATH!;%DIR%dat\pak\!currentDir!"
)

"%DIR%dat\pak\umka\windows\umka.exe" "%DIR%dat\pak.um" %*
