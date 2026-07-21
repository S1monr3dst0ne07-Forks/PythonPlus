class NumberNode:

    def __init__(self, value):
        self.value = value


class StringNode:

    def __init__(self, value):
        self.value = value


class VariableNode:

    def __init__(self, name):
        self.name = name


class BinaryOperationNode:

    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right


class AssignmentNode:

    def __init__(self, name, value):
        self.name = name
        self.value = value


class PrintNode:

    def __init__(self, value):
        self.value = value
