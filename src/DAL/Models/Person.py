from src.DAL.DataContext.Database_Context import Database_Context
from src.DAL.Models.Model import Model

class Person(Model):

    def __init__(self, ctx : Database_Context) -> None:
        self.ctx = ctx
        self.__tablename__ = "Person"
        self.__rows__ = (
            "id",
            "name",
            "age"
        )
        self.__defenition__ = (
                "  `id` int(11) NOT NULL AUTO_INCREMENT,"
                "  `name` varchar(14) NOT NULL,"
                "  `age` int(3) NOT NULL,"
                "  PRIMARY KEY (`id`)"
            )

