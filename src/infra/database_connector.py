import mysql.connector as mysql

class DatabaseConnection:

    connection = None

    @classmethod
    def connect(cls):
        db_connection = mysql.connect(
            host = "localhost",
            port = 3306,
            database = "pipeline_db",
            user = "root",
            passwd = "onepiece1998Yan"
        )
        cls.connection = db_connection
