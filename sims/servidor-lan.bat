@echo off
REM Doble click para levantar el servidor del aula en Windows.
cd /d "%~dp0"
python servidor-lan.py 8080 || py servidor-lan.py 8080
pause
