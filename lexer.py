from tokens import *

class Lexer:

    def __init__(self, text):
        self.text = text
        self.pos = 0

    def current(self):
        if self.pos >= len(self.text):
            return None
        return self.text[self.pos]

    def advance(self):
        self.pos += 1

    def tokenize(self):

        tokens = []

        while self.current() is not None:

            c = self.current()

            if c.isspace():
                self.advance()

            elif c.isdigit():

                number = ""

                while self.current() and self.current().isdigit():
                    number += self.current()
                    self.advance()

                tokens.append(Token(TokenType.NUMBER, int(number)))

            elif c.isalpha():

                word = ""

                while self.current() and self.current().isalnum():
                    word += self.current()
                    self.advance()

                if word == "print":
                    tokens.append(Token(TokenType.PRINT, word))
                else:
                    tokens.append(Token(TokenType.IDENTIFIER, word))

            elif c == "+":
                tokens.append(Token(TokenType.PLUS, "+"))
                self.advance()

            elif c == "=":
                tokens.append(Token(TokenType.EQUALS, "="))
                self.advance()

            else:
                raise Exception(f"Unknown character {c}")

        tokens.append(Token(TokenType.EOF, ""))

        return tokens
