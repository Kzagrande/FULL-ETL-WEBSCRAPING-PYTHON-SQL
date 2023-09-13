import pymysql
import sshtunnel
import logging
from src.errors.error_log import ErrorLog


class DatabaseConnection:
    connection = None

    @classmethod
    def connect(cls):
        try:
            logging.basicConfig(
                level=logging.DEBUG
            )  # Configurar o nível de log desejado

            # Configuração do túnel SSH
            tunnel = sshtunnel.SSHTunnelForwarder(
                ssh_address_or_host=(
                    "62.72.11.208",
                    22,
                ),  # Configurar o endereço e a porta do servidor SSH
                ssh_username="root",
                ssh_password="onepiece1998Yan",
                remote_bind_address=("127.0.0.1", 3306),
            )

            tunnel.start()  # Iniciar o túnel SSH

            db_connection = pymysql.connect(
                host="127.0.0.1",
                port=tunnel.local_bind_port,  # Usar a porta local do túnel SSH
                database="ware_ods_shein",
                user="ware_admin",
                passwd="onepiece9960",
            )

            cls.connection = db_connection
        except Exception as exception:
            raise ErrorLog(str(exception), func="connect()",error_code=9) from exception
