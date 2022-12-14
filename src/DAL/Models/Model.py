from src.DAL.DataContext.Database_Context import Database_Context
from src.DAL.Queries.Insert_Queries import insert_to_table
from src.DAL.Queries.Delete_Queries import delete
from src.DAL.Queries.Table_Creation_Queries import create_table


class Model:
    def __init__(self, ctx: Database_Context):
        self.ctx = ctx

    def create_table(self):
        create_table(self.__tablename__, self.__defenition__, self.ctx)

    def new(self, data : dict) -> dict:
        if all(row in self.__rows__ for row in data.keys()):
            insert_to_table(self.__tablename__, data, self.ctx)
            return {
                row : data[row] 
                if (row in data.keys()) 
                else '' 
                for row in self.__rows__  
                }
        else:
            return None

    def delete(self, condition : str) -> bool:
        return delete(self.__tablename__, condition, self.ctx)
