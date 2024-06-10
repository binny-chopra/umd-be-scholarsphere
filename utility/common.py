import mysql.connector
from constants import app_constants


class common:
    def conn_setup(self):
        try:
            self.conn = mysql.connector.connect(
                host=app_constants.DB_HOST,
                user=app_constants.DB_USER,
                password=app_constants.DB_PASSWORD,
                database=app_constants.DB_NAME,
            )
            self.conn.autocommit = True
            self.cursor = self.conn.cursor(dictionary=True)
            print(app_constants.CONN_SUCCESSFUL)
        except:
            print(app_constants.CONN_FAILED)
