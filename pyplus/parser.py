from .tokens import TokenType
from .ast_nodes import (
    NumberNode,
    StringNode,
    VariableNode,
    BinaryOperationNode,
    AssignmentNode,
    PrintNode,
    ProgramNode,
    GroupNode,
)


class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0


    def parse(self):

        statements = []

        while self.current().type != TokenType.EOF:

            if self.current().type == TokenType.NEWLINE:
                self.advance()
                continue

            statements.append(
                self.parse_statement()
            )

        return ProgramNode(statements)


    def parse_statement(self):

        token = self.current()

        if token.type == TokenType.PRINT:

            self.advance()

            value = self.parse_expression()

            return PrintNode(value)

        if token.type == TokenType.IDENTIFIER:

            name = token.value

            self.advance()

            if self.current().type == TokenType.ASSIGN:

                self.advance()

                value = self.parse_expression()

                return AssignmentNode(
                    name,
                    value
                )


        raise Exception(
            f"Unknown statement: {token}"
        )


    def parse_expression(self):


        return self.parse_addition()

    def parse_addition(self):

        left = self.parse_multiplication()

        while self.current().type in (
            TokenType.PLUS,
            TokenType.MINUS,
        ):

            operator = self.current()

            self.advance()

            right = self.parse_multiplication()

            left = BinaryOperationNode(
                left,
                operator.value,
                right
            )

        return left


    def parse_multiplication(self):

        left = self.parse_primary()

        while self.current().type in (
            TokenType.STAR,
            TokenType.SLASH,
        ):

            operator = self.current()

            self.advance()

            right = self.parse_primary()

            left = BinaryOperationNode(
                left,
                operator.value,
                right
            )

        return left


    def parse_primary(self):

        token = self.current()

        if token.type == TokenType.LPAREN:

            self.advance()

            expression = self.parse_expression()

            if self.current().type != TokenType.RPAREN:
                raise Exception(
                    "Expected ')'"
                )

            self.advance()

            return GroupNode(expression)

        if token.type == TokenType.STRING:

            self.advance()

            return StringNode(
                token.value
            )

        if token.type == TokenType.NUMBER:

            self.advance()

            return NumberNode(
                token.value
            )


        if token.type == TokenType.IDENTIFIER:

            self.advance()

            return VariableNode(
                token.value
            )


        raise Exception(
            f"Unexpected token: {token}"
        )


    def current(self):

        return self.tokens[self.position]


    def advance(self):

        self.position += 1
