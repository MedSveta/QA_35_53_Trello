
from dataclasses import dataclass

@dataclass
class User:
    email: str|None = None
    password: str|None = None
