from src.DAL.DataContext.Database_Context import Database_Context
from src.DAL.Models.Model import Model


class Repository:
    def __init__(self, ctx : Database_Context) -> None:
        self.ctx = ctx
        self.model = Model(self.ctx)
        self.query_history = []
        self.staged = []

    def add(self, data : dict) -> dict:
        pass

    def remove(id : int) -> bool:
        pass

    def get(id : int) -> dict:
        pass

    def find(predicate : dict = None) -> list(dict):
        pass
