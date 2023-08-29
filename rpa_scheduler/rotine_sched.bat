@echo off

rem Defina a pasta onde está o ambiente virtual (seu_script_env)
set "ENV_DIR=C:\Users\User\sites\control-tower-D\venv"

rem Ative o ambiente virtual
call "%ENV_DIR%\Scripts\activate"

rem Vá para a pasta onde está o script Python (sorting_in.py)
cd C:\Users\User\sites\control-tower-D

rem Execute o script Python
python run.py

rem Desative o ambiente virtual após a execução do script (opcional)
deactivate