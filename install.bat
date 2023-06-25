@echo off

cd C:\
mkdir procx && cd procx
echo The Folders have been created. Cloning with git now.
git clone -b raw https://github.com/8root/proc .

rem Close all open Registry Editor windows
taskkill /f /im regedit.exe >nul 2>&1

rem Wait for Registry Editor to close
timeout /t 2 >nul

rem Open Registry Editor
start regedit

rem Wait for Registry Editor to open
timeout /t 2 >nul

rem Collapse all folders in Registry Editor
reg.exe ADD HKCU\Software\Microsoft\Windows\CurrentVersion\Applets\Regedit /v LastKey /t REG_SZ /d "5c 00 00 00" /f >nul 2>&1

rem Create vStart key under HKEY_CLASSES_ROOT
reg.exe ADD HKEY_CLASSES_ROOT\vStart /f >nul 2>&1

rem Create URL Protocol string value under vStart key
reg.exe ADD HKEY_CLASSES_ROOT\vStart /v "URL Protocol" /t REG_SZ /d "" /f >nul 2>&1

rem Create shell key under vStart key
reg.exe ADD HKEY_CLASSES_ROOT\vStart\shell /f >nul 2>&1

rem Create open key under shell key
reg.exe ADD HKEY_CLASSES_ROOT\vStart\shell\open /f >nul 2>&1

rem Create command key under open key
reg.exe ADD HKEY_CLASSES_ROOT\vStart\shell\open\command /f >nul 2>&1

rem Set the value of the REG_SZ key under command key
reg.exe ADD HKEY_CLASSES_ROOT\vStart\shell\open\command /v "" /t REG_SZ /d "c:\proc\menu.bat" "%%1" /f >nul 2>&1

echo All registry changes have been applied successfully.
echo You can exit now.
color 5
pause