from enum import Enum
from dataclasses import dataclass


# all the tokens
class TokenType(Enum):
    NUMBER = 0
    PLUS = 1
    MINUS = 2
    MULTIPLY = 3
    DIVIDE = 4
    LPAREN = 5
    RPAREN = 6
    VARIABLE = 7
    ASSIGN = 8
    IF = 9
    ELSE = 10
    WHILE = 11
    GREATER = 12
    LESS = 13
    EQUAL = 14
    LBARCK = 15
    RBRACK = 16
    LINE = 17
    EOF = 18  # End of file


@dataclass
class Token:
    type: TokenType
    value: any = None

    def __repr__(self):
        return self.type.name + (f":{self.value}" if self.value is not None else "")
