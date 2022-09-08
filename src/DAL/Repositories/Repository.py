from abc import ABC, abstractmethod
from src.DAL.DataContext.Database_Context import Database_Context
from src.DAL.Models.Model import Model


class Repository(ABC):
    def __init__(self, ctx : Database_Context) -> None:
        self.ctx = ctx
        self.model = Model(self.ctx)
        self.query_history = []
        self.staged = []

    @abstractmethod
    def add(self, data : dict) -> dict:
        pass

    @abstractmethod
    def remove(self, id : int) -> bool:
        pass

    @abstractmethod
    def get(self, id : int) -> dict:
        pass

    @abstractmethod
    def find(self, predicate : dict = {}) -> list:
        pass
