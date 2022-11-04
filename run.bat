@REM buat nanti belum tau yang mana bakal jadi appsnya
CALL .\src\Scripts\activate
pyinstaller --onefile .\src\program\apps.py -w
.\dist\apps.exe