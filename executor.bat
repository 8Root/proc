@echo off
set cfgvar=%1
echo github.com/8root/proc
echo try out now: rootqit.dev/proc/test
echo Running in python.
py C:\proc\runtime\main.py -c %cfgvar%
pause
