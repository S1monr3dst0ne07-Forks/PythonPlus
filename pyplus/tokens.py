from enum import Enum, auto


class TokenType(Enum):
    PRINT = auto()

    IDENTIFIER = auto()
    IF = auto()

    STRING = auto()
    NUMBER = auto()

    ASSIGN = auto()      # :=

    PLUS = auto()
    MINUS = auto()
    STAR = auto()
    SLASH = auto()

    TRUE = auto()
    FALSE = auto()
    
    LPAREN = auto()
    RPAREN = auto()
    COMMA = auto()

    FUNCTION = auto()
    END = auto()

    NEWLINE = auto()
    RETURN = auto()
    EOF = auto()

    EQUAL = auto()          # ==
    NOT_EQUAL = auto()      # !=

    LESS = auto()           # <
    LESS_EQUAL = auto()     # <=

    GREATER = auto()        # >
    GREATER_EQUAL = auto()  # >=


class Token:
    def __init__(self, token_type, value=None, line=1, column=1):
        self.type = token_type
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        return (
            f"{self.type.name}({self.value}) "
            f"[{self.line}:{self.column}]"
        )
