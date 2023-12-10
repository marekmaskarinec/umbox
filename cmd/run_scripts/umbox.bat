@echo off
setlocal enabledelayedexpansion

set DIR=%~dp0

for /f "delims=" %%i in ('dir /b "%DIR%dat\umbox"') do (
	set "currentDir=%%i"
	set "PATH=!PATH!;%DIR%dat\umbox\!currentDir!"
)

"%DIR%dat\umbox\umka\windows\umka.exe" "%DIR%dat\umbox.um" %*
