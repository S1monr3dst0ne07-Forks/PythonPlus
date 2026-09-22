from .lexer import Lexer
from .tokens import TokenType
from .parser import Parser
from .generator import Generator

class Compiler:
    def compile(self, code):
        tokens = Lexer(code).tokenize()

        for token in tokens:
            print(token)

        tree = Parser(tokens).parse()
        python_code = Generator().generate(tree)

        header = "import sys; sys.setrecursionlimit(10000)\n"
        return header + python_code
    

    def dead():
        output = []

        i = 0
        while i < len(tokens):
            token = tokens[i]
            i += 1

            match token.type:
                case TokenType.NEWLINE: pass

                # Variable assignment
                case TokenType.IDENTIFIER:
                    if i == len(tokens):                   continue
                    if tokens[i].type != TokenType.ASSIGN: continue
                    i += 1

                    value = tokens[i]
                    i += 1

                    if value.type == TokenType.STRING:
                        line = f'{token.value} = "{value.value}"'

                    elif value.type == TokenType.NUMBER:
                        line = f'{token.value} = {value.value}'

                    output.append(line)
                    
                case TokenType.PRINT:
                    value = tokens[i]
                    i += 1

                    if value.type == TokenType.STRING:
                        line = f'print("{value.value}")'

                    elif value.type == TokenType.IDENTIFIER:
                        line = f'print({value.value})'

                    output.append(line)


        return "\n".join(output)
