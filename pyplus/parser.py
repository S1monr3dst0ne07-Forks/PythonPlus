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
    FunctionCallNode,
    FunctionDefinitionNode,
    ReturnNode,
    BooleanNode,
    IfNode,
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

            value = self.parse_primary()

            return PrintNode(value)

        if token.type == TokenType.RETURN:

                self.advance()

                value = self.parse_expression()

                return ReturnNode(value)

        if token.type == TokenType.IF:

            self.advance()

            condition = self.parse_expression()


            while self.current().type == TokenType.NEWLINE:
                self.advance()


            body = []


            while self.current().type != TokenType.END:

                body.append(
                    self.parse_statement()
                )

                while self.current().type == TokenType.NEWLINE:
                    self.advance()


            self.advance()  # consume END


            return IfNode(
                condition,
                body
            )
            

        if token.type == TokenType.FUNCTION:

            self.advance()

            name = self.current().value

            self.advance()

            parameters = []

            if self.current().type != TokenType.LPAREN:
                raise Exception("Expected '(' after function name")

            self.advance()

            while self.current().type != TokenType.RPAREN:


                if self.current().type != TokenType.IDENTIFIER:
                    raise Exception(
                        "Expected parameter name"
                    )

                parameters.append(
                    self.current().value
                )

                self.advance()


                if self.current().type == TokenType.COMMA:

                    self.advance()

                else:

                    break


            if self.current().type != TokenType.RPAREN:
                raise Exception(
                    "Expected ')'"
                )

            self.advance()


            # Skip new lines after function header
            while self.current().type == TokenType.NEWLINE:
                self.advance()


            body = []

            while self.current().type != TokenType.END:

                body.append(
                    self.parse_statement()
                )

                while self.current().type == TokenType.NEWLINE:
                    self.advance()


            self.advance()  # consume END


            return FunctionDefinitionNode(
                name,
                parameters,
                body
            )

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


            if self.current().type == TokenType.LPAREN:

                self.position -= 1

                return self.parse_primary()

        raise Exception(
            f"Unknown statement: {token}"
        )

    def parse_function(self):

        self.advance()   # Skip 'function'

        if self.current().type != TokenType.IDENTIFIER:
            raise Exception("Expected function name")

        name = self.current().value
        self.advance()

        if self.current().type != TokenType.LPAREN:
            raise Exception("Expected '('")

        self.advance()

        parameters = []

        while self.current().type != TokenType.RPAREN:

            if self.current().type != TokenType.IDENTIFIER:
                raise Exception("Expected parameter")

            parameters.append(
                self.current().value
            )

            self.advance()

            if self.current().type == TokenType.COMMA:
                self.advance()
            else:
                break

        if self.current().type != TokenType.RPAREN:
            raise Exception("Expected ')'")

        self.advance()

        while self.current().type == TokenType.NEWLINE:
            self.advance()

        body = []

        while self.current().type != TokenType.END:

            if self.current().type == TokenType.NEWLINE:
                self.advance()
                continue

            body.append(
                self.parse_statement()
            )

        self.advance()   # Skip END

        return FunctionDefinitionNode(
            name,
            parameters,
            body
        )


    def parse_expression(self):

        return self.parse_comparison()

    def parse_comparison(self):

        left = self.parse_addition()

        while self.current().type in (
            TokenType.EQUAL,
            TokenType.NOT_EQUAL,
            TokenType.LESS,
            TokenType.LESS_EQUAL,
            TokenType.GREATER,
            TokenType.GREATER_EQUAL,
        ):

            operator = self.current()

            self.advance()

            right = self.parse_addition()

            left = BinaryOperationNode(
                left,
                operator.value,
                right
            )

        return left

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

            return StringNode(token.value)


        if token.type == TokenType.NUMBER:

            self.advance()

            return NumberNode(token.value)

        if token.type == TokenType.TRUE:

            self.advance()

            return BooleanNode(True)


        if token.type == TokenType.FALSE:

            self.advance()

            return BooleanNode(False)


        if token.type == TokenType.IDENTIFIER:

            self.advance()

            if self.current().type == TokenType.LPAREN:

                self.advance()

                arguments = []

                while self.current().type != TokenType.RPAREN:

                    arguments.append(
                        self.parse_expression()
                    )

                    if self.current().type == TokenType.COMMA:
                        self.advance()
                    else:
                        break

                if self.current().type != TokenType.RPAREN:
                    raise Exception(
                        "Expected ')'"
                    )

                self.advance()

                return FunctionCallNode(
                    token.value,
                    arguments
                )


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
