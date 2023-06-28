if not exist venv ( 
py -m venv venv )
call venv\scripts\activate
py -m pip install -r requirements.txt