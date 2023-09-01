import os
from datetime import datetime
from src.drivers.slack_report import log_error_and_notify_slack


class ErrorLog(Exception):
    def __init__(self, message: str,func:str) -> None:
        super().__init__(message)
        self.message = message

        current_path = os.path.abspath(__file__)
        arquive_name = os.path.basename(current_path)
        mensagem_de_erro = (
            f"Arquivo: {arquive_name} \n\n "
            f"Hora atual: {datetime.now()} \n\n"
            f"Função: '{func}',\n\n "
            f"Erro: {message}"
        )

        log_error_and_notify_slack(mensagem_de_erro)
