@echo off

cd /d ..

if exist dist rmdir /s /q dist
if exist build rmdir /s /q build
if exist scripts\main.spec del /f /q scripts\main.spec

python -m PyInstaller -F ^
--collect-all fake_useragent ^
--specpath scripts ^
src/dirsearch/main.py

pause