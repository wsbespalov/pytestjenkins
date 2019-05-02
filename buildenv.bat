cd c:\projects\pytestjenkins\
venv\Scripts\activate.bat
mkdir -p reports
pip install -r requirements.txt
pytest tests\test_api.py