@echo off
setlocal enabledelayedexpansion

set DIR=%~dp0

for /d %%i in (%DIR%dat/pak\*) do (
	set "currentDir=%%i"
	set "PATH=!PATH!;!currentDir!"
)

where curl-ca-bundle.crt

%DIR%dat\pak\umka\windows\umka.exe %DIR%dat\pak.um %*
