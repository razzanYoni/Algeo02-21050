@REM kalo mau cepet push ke github tapi manual lebih baik
@REM masih ERROR
echo off
git branch
echo "Apakah sudah ada di dalam branch[y/n]?"
set /p xyz =

if /i "%xyz%" == "y" goto branch
if /i "%xyz%"== "n" goto push
:branch
echo "Masukkan nama branch"
set /p brc =  
CALL git checkout -b "%brc%"
goto push
:push
git branch
set /p commit="Commit message: "
git add .
git commit -m "%commit%"
@REM git push
goto :end