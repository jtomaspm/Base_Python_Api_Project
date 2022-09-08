import mysql.connector
from mysql.connector import errorcode
from src.DAL.DataContext.Database_Context import Database_Context



def create_database(ctx : Database_Context):
    DB_NAME = ctx.config.pop('database')

    def create_database_int(cursor, DB_NAME):
        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
    
    with ctx.cursor() as (cnx, cursor):
        try:
            cursor.execute("USE {}".format(DB_NAME))
        except mysql.connector.Error as err:
            print("Database {} does not exists.".format(DB_NAME))
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                create_database_int(cursor, DB_NAME)
                print("Database {} created successfully.".format(DB_NAME))
                cnx.database = DB_NAME
                ctx.config['database'] = DB_NAME
            else:
                print(err)
    
    ctx.config['database'] = DB_NAME