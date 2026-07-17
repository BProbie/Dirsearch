#!/bin/bash

cd /d ..

rm -rf dist
rm -rf build
rm -rf scripts/main.spec

python -m PyInstaller -F ^
--collect-all fake_useragent ^
--add-data "src/webfuzz/data;data" ^
src/dirsearch/main.py

mv main.spec scripts

read -p "..."