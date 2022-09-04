import mysql.connector
from mysql.connector import errorcode
from src.DAL.DataContext.Database_Context import Database_Context
from src.Core.Utilities.string_formaters import key_list_to_string

def insert_to_table(tablename : str, data : dict, ctx : Database_Context):
    rows, values = tuple(data.keys()), tuple(data.values())
    rows_str = key_list_to_string(rows)
    values_str = "(" + ("%s,"*len(values))[:-1] + ")"
    query = "INSERT INTO {} {} VALUES {}".format(tablename, rows_str, values_str)
    print(query)
    with ctx.cursor() as (cnx, cursor):
        cursor.execute(query, values)
        cnx.commit()