from .tokens import Token, TokenType


class Lexer:

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


            # Numbers
            if char.isdigit():

                tokens.append(
                    self.read_number()
                )

                continue


            # Identifiers / keywords
            if char.isalpha():

                tokens.append(
                    self.read_identifier()
                )

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


            self.advance()


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


    def read_identifier(self):

        start = self.column
        word = ""

        while (
            self.position < len(self.source)
            and self.source[self.position].isalnum()
        ):

            word += self.source[self.position]
            self.advance()


        if word == "print":

            return Token(
                TokenType.PRINT,
                word,
                self.line,
                start
            )


        return Token(
            TokenType.IDENTIFIER,
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
