py -m venv src
CALL .\src\Scripts\activate
pip install -r requirements.txt
pyinstaller --onefile .\src\apps.py -w
.\dist\apps.exe