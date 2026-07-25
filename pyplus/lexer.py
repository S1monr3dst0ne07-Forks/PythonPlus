from .tokens import Token, TokenType


class Lexer:

    KEYWORDS = {
        "function": TokenType.FUNCTION,
        "end": TokenType.END,
        "return": TokenType.RETURN,
        "if": TokenType.IF,
        "True": TokenType.TRUE,
        "False": TokenType.FALSE,
    }

    def __init__(self, source):
        self.source = source
        self.position = 0
        self.line = 1
        self.column = 1


    def tokenize(self):

        tokens = []

        while self.position < len(self.source):

            char = self.source[self.position]

            # Spaces
            if char in " \t":
                self.advance()
                continue

            # New lines
            if char == "\n":

                tokens.append(
                    Token(
                        TokenType.NEWLINE,
                        None,
                        self.line,
                        self.column
                    )
                )

                self.advance()
                self.line += 1
                self.column = 1
                continue

            # Strings
            if char == '"':

                tokens.append(
                    self.read_string()
                )
                continue

            # Numbers
            if char.isdigit():

                tokens.append(
                    self.read_number()
                )
                continue

            # Identifiers / keywords
            if char.isalpha() or char == "_":

                tokens.append(
                    self.read_identifier()
                )
                continue

            # ==
            if char == "=" and self.peek() == "=":

                tokens.append(
                    Token(
                        TokenType.EQUAL,
                        "==",
                        self.line,
                        self.column
                    )
                )

                self.advance()
                self.advance()
                continue

            # !=
            if char == "!" and self.peek() == "=":

                tokens.append(
                    Token(
                        TokenType.NOT_EQUAL,
                        "!=",
                        self.line,
                        self.column
                    )
                )

                self.advance()
                self.advance()
                continue

            # Assignment :=
            if char == ":" and self.peek() == "=":

                tokens.append(
                    Token(
                        TokenType.ASSIGN,
                        ":=",
                        self.line,
                        self.column
                    )
                )

                self.advance()
                self.advance()
                continue

            # <=
            if char == "<" and self.peek() == "=":

                tokens.append(
                    Token(
                        TokenType.LESS_EQUAL,
                        "<=",
                        self.line,
                        self.column
                    )
                )

                self.advance()
                self.advance()
                continue

            # >=
            if char == ">" and self.peek() == "=":

                tokens.append(
                    Token(
                        TokenType.GREATER_EQUAL,
                        ">=",
                        self.line,
                        self.column
                    )
                )

                self.advance()
                self.advance()
                continue

            # <
            if char == "<":
                
                tokens.append(
                    Token(
                        TokenType.LESS,
                        "<",
                        self.line,
                        self.column
                    )
                )


                self.advance()
                continue

            # >
            if char == ">":

                tokens.append(
                    Token(
                        TokenType.GREATER,
                        ">",
                        self.line,
                        self.column
                        )
                    )

                self.advance()
                continue


            # Operators
            if char == "+":

                tokens.append(
                    Token(
                        TokenType.PLUS,
                        "+",
                        self.line,
                        self.column
                    )
                )

                self.advance()
                continue

            if char == "-":

                tokens.append(
                    Token(
                        TokenType.MINUS,
                        "-",
                        self.line,
                        self.column
                    )
                )

                self.advance()
                continue

            if char == "*":

                tokens.append(
                    Token(
                        TokenType.STAR,
                        "*",
                        self.line,
                        self.column
                    )
                )

                self.advance()
                continue

            if char == "/":

                tokens.append(
                    Token(
                        TokenType.SLASH,
                        "/",
                        self.line,
                        self.column
                    )
                )

                self.advance()
                continue

            # Parentheses
            if char == "(":

                tokens.append(
                    Token(
                        TokenType.LPAREN,
                        "(",
                        self.line,
                        self.column
                    )
                )

                self.advance()
                continue

            if char == ")":

                tokens.append(
                    Token(
                        TokenType.RPAREN,
                        ")",
                        self.line,
                        self.column
                    )
                )

                self.advance()
                continue

            # Comma
            if char == ",":

                tokens.append(
                    Token(
                        TokenType.COMMA,
                        ",",
                        self.line,
                        self.column
                    )
                )

                self.advance()
                continue

            raise Exception(
                f"Unexpected character '{char}' at {self.line}:{self.column}"
            )

        tokens.append(
            Token(TokenType.EOF)
        )

        return tokens


    def read_number(self):

        start = self.column
        number = ""

        while (
            self.position < len(self.source)
            and self.source[self.position].isdigit()
        ):

            number += self.source[self.position]
            self.advance()

        return Token(
            TokenType.NUMBER,
            int(number),
            self.line,
            start
        )


    def read_string(self):

        start = self.column

        self.advance()   # Skip opening quote

        text = ""

        while (
            self.position < len(self.source)
            and self.source[self.position] != '"'
        ):

            text += self.source[self.position]
            self.advance()

        self.advance()   # Skip closing quote

        return Token(
            TokenType.STRING,
            text,
            self.line,
            start
        )


    def read_identifier(self):

        start = self.column
        word = ""

        while (
            self.position < len(self.source)
            and (
                self.source[self.position].isalnum()
                or self.source[self.position] == "_"
            )
        ):

            word += self.source[self.position]
            self.advance()

        token_type = self.KEYWORDS.get(
            word,
            TokenType.IDENTIFIER
        )

        return Token(
            token_type,
            word,
            self.line,
            start
        )


    def peek(self):

        if self.position + 1 < len(self.source):
            return self.source[self.position + 1]

        return ""


    def advance(self):

        self.position += 1
        self.column += 1
