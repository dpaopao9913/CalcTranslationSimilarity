@echo off
pushd %~dp0
setlocal enabledelayedexpansion

setlocal
set INPUT_FILENAME=sentences.csv
set OUTPUT_FILENAME=sentences_out.csv

rem Anaconda§ŒÅ¢œÎ≠hæ≥£®base£©§Œåg––
call "D:\anaconda\Scripts\activate.bat"

python calcTranslationSimilarity.py %INPUT_FILENAME% %OUTPUT_FILENAME%

pause