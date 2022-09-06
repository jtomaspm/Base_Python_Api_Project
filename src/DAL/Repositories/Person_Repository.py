from src.DAL.Repositories.Repository import Repository
from src.DAL.DataContext.Database_Context import Database_Context
from src.DAL.Models.Person import Person

class Person_Repository(Repository):
    def __init__(self, ctx: Database_Context) -> None:
        super().__init__(ctx)
        self.model = Person(ctx)