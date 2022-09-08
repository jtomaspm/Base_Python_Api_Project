from dataclasses import dataclass, field


@dataclass
class Person():
    _id : int
    name : str = field(metadata={'max_length' : 55})
    age : int = field(metadata={'max_length': 3})