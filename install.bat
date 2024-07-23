@echo off
setlocal enabledelayedexpansion

set "REQUIRED_PYTHON_VERSION=3.11.8"

set "REQUIRED_PACKAGES=colorama requests tls_client holehe py-cord cryptography"

set "CMD=cmd.exe /c exit"

for /f "delims=" %%i in ('python --version 2^>^&1') do set "PYTHON_VERSION=%%i"

if "%PYTHON_VERSION%"=="" (
    echo Python is not installed.
    goto :INSTALL_PYTHON
)

for /f "tokens=2 delims= " %%i in ("%PYTHON_VERSION%") do set "PYTHON_VERSION=%%i"

if "%PYTHON_VERSION%"=="%REQUIRED_PYTHON_VERSION%" (
    echo Required Python version %REQUIRED_PYTHON_VERSION% is already installed.
    goto :CHECK_PIP
) else (
    echo Installed Python version is %PYTHON_VERSION%.
    echo Required Python version is %REQUIRED_PYTHON_VERSION%.
    goto :INSTALL_PYTHON
)

:INSTALL_PYTHON
echo Installing Python %REQUIRED_PYTHON_VERSION%...
curl -o python-installer.exe https://www.python.org/ftp/python/%REQUIRED_PYTHON_VERSION%/python-%REQUIRED_PYTHON_VERSION%-amd64.exe

start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1

del python-installer.exe

set "PATH=%ProgramFiles%\Python311\Scripts;%ProgramFiles%\Python311;%PATH%"

for /f "delims=" %%i in ('python --version 2^>^&1') do set "PYTHON_VERSION=%%i"
for /f "tokens=2 delims= " %%i in ("%PYTHON_VERSION%") do set "PYTHON_VERSION=%%i"

if not "%PYTHON_VERSION%"=="%REQUIRED_PYTHON_VERSION%" (
    echo Failed to install Python %REQUIRED_PYTHON_VERSION%.
    exit /b 1
)

:CHECK_PIP
python -m ensurepip --upgrade
python -m pip install --upgrade pip

:INSTALL_PACKAGES
for %%p in (%REQUIRED_PACKAGES%) do (
    echo Installing package %%p...
    python -m pip install %%p
)

echo Python and required packages setup completed.
exit /b 0

# dev by dx / https://github.com/eerieweb
