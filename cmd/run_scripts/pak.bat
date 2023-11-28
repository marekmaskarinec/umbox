@echo off
setlocal enabledelayedexpansion

set DIR=%~dp0

for /d %%i in (%DIR%dat/pak\*) do (
	set "currentDir=%%i"
	set "PATH=!PATH!;!currentDir!"
)

"%DIR%dat\pak\umka\windows\umka.exe" "%DIR%dat\pak.um" %*
