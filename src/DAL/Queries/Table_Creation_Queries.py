import mysql.connector
from mysql.connector import errorcode
from src.DAL.DataContext.Database_Context import Database_Context

def create_table(table_name: str, table_description : str, ctx : Database_Context):


    query = (
        "CREATE TABLE `{}` ("
        "{}"
        ") ENGINE=InnoDB"
    ).format(table_name, table_description)
    print(query)
    with ctx.cursor() as (_, cursor):
        try:
            print("Creating table {}: ".format(table_name), end='')
            cursor.execute(query)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")