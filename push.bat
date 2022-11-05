@REM kalo mau cepet push ke github tapi manual lebih baik
@REM masih ERROR
@REM echo off
@REM git branch
@REM echo "Apakah sudah ada di dalam branch[y/n]?"
@REM set /p xyz =

@REM if /i "%xyz%" == "y" goto branch
@REM if /i "%xyz%"== "n" goto push
@REM :branch
@REM echo "Masukkan nama branch"
@REM set /p brc =  
@REM CALL git checkout -b "%brc%"
@REM goto push
@REM :push
@REM git branch
@REM set /p commit="Commit message: "
@REM git add .
@REM git commit -m "%commit%"
@REM @REM git push
@REM goto :end