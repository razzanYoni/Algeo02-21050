echo off &&
python3 -m venv src &&
source ./src/bin/activate &&
pip install -r requirements.txt &&
python3 ./src/program/apps.py
