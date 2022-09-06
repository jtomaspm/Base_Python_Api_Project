import mysql.connector
from mysql.connector import errorcode
from contextlib import contextmanager


class Database_Context:

    def __init__(self, config):
        self.config = config

    @contextmanager
    def connection(self):
        cnx = None
        try:
            cnx = mysql.connector.connect(**self.config)
            yield cnx
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cnx.commit()
        finally:
            if cnx:
                cnx.close()

    @contextmanager
    def cursor(self):
        with self.connection() as cnx:
            try:
                cursor = cnx.cursor()
                yield (cnx, cursor)
            finally:
                cursor.close()

