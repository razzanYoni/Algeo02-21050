@REM kalo mau cepet push ke github tapi manual lebih baik
@REM masih ERROR
@REM @echo off
@REM git branch
@REM set /p xyz = "apakah sudah di branch? 0/1? "
@REM if %xyz%==0 goto branch
@REM if %xyz%==1 goto push
@REM :branch
@REM set /p "branch = masukkan nama branch:  "
@REM git checkout -b %branch%
@REM goto push
@REM :push
@REM set /p "commit=Commit message: "
@REM git add .
@REM git commit -m "%commit%"
@REM git push
@REM goto end
@REM :end