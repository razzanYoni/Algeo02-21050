echo off
python3 -m venv src
CALL .\src\Scripts\activate
pip install -r requirements.txt
python .\src\program\apps.py