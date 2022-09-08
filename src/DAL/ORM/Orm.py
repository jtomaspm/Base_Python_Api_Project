
from ctypes import Structure
from dataclasses import dataclass

class database_model(Structure):
    tablename : str
    primary_key : str

class Orm:
    def __init__(self, data_class : database_model) -> None:
        pass