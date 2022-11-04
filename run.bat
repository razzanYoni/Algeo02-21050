@REM buat nanti belum tau yang mana bakal jadi appsnya
@REM pastiin udah jadi venvnya
pip install virtualenv
py -m venv src
CALL .\src\Scripts\activate
pip install -r requirements.txt
pyinstaller --onefile .\src\program\apps.py -w
.\dist\apps.exe