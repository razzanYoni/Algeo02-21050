echo off &&
python3 -m venv src &&
CALL ./src/Scripts/activate &&
pip install -r requirements.txt &&
python3 ./src/program/apps.py