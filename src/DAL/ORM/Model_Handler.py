
from ctypes import Structure
from dataclasses import dataclass
from typing import List
from src.DAL.ORM.Orm import database_model

class Field(Structure):
    name : str 
    options : List[str]

class ORM_Object(Structure):
    tablename : str
    fields : List[Field]
    required_fields : List[Field]
    primary_key : str
    


def ORM_Object_Factory(model : database_model) -> ORM_Object | None:
    fields = list(model.__dataclass_fields__.keys())

    pass