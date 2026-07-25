class NumberNode:

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Number({self.value})"


class StringNode:

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"String({self.value})"

class FunctionCallNode:

    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments

    def __repr__(self):
        return f"Call({self.name}, {self.arguments})"

class FunctionDefinitionNode:

    def __init__(self, name, parameters, body):
        self.name = name
        self.parameters = parameters
        self.body = body

    def __repr__(self):
        return (
            f"Function({self.name})"
        )

class VariableNode:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Variable({self.name})"


class BinaryOperationNode:

    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self):
        return (
            f"BinaryOperation("
            f"{self.left} {self.operator} {self.right}"
            f")"
        )

class GroupNode:

    def __init__(self, expression):
        self.expression = expression

    def __repr__(self):
        return f"Group({self.expression})"

class AssignmentNode:

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return (
            f"Assignment("
            f"{self.name} = {self.value}"
            f")"
        )

class IfNode:

    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def __repr__(self):
        return f"If({self.condition})"

class BooleanNode:

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Boolean({self.value})"

class ReturnNode:

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Return({self.value})"


class PrintNode:

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Print({self.value})"

class ProgramNode:

    def __init__(self, statements):
        self.statements = statements

    def __repr__(self):
        return (
            f"Program({self.statements})"
        )
