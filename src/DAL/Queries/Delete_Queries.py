from src.DAL.DataContext.Database_Context import Database_Context

def delete(tablename : str, condition : str, ctx : Database_Context) -> bool:
    query = (
        "DELETE FROM {} WHERE ({})"
    ).format(tablename, condition)
    print(query)
    with ctx.cursor() as (_, cursor):
        try:
            cursor.execute(query)
            return True
        except:
            return False