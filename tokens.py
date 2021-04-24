from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
    NUM = 0
    ADD = 1
    SUB = 2
    MUL = 3
    DIVIDE = 4
    LPAREN = 5
    RPAREN = 6

@dataclass
class Token:
    type: TokenType
    value: any = None

    def __repr__(self):
        return self.type.name + (f":{self.value}" if self.value != None else "")