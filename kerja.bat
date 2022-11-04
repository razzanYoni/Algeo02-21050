cd ..\
mkdir lokal
xcopy /s .\Algeo02-21050 .\lokal
cd .\lokal
py -m venv src
CALL .\src\Scripts\activate
pip install -r requirements.txt