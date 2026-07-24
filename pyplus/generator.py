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
)


class Generator:

    def generate(self, node):

        if isinstance(node, ProgramNode):

            output = []

            for statement in node.statements:

                output.append(
                    self.generate(statement)
                )

            return "\n".join(output)


        if isinstance(node, NumberNode):

            return str(node.value)


        if isinstance(node, StringNode):

            return f'"{node.value}"'


        if isinstance(node, VariableNode):

            return node.name


        if isinstance(node, BinaryOperationNode):

            left = self.generate(node.left)

            right = self.generate(node.right)

            return (
                f"{left} {node.operator} {right}"
            )


        if isinstance(node, AssignmentNode):

            value = self.generate(node.value)

            return (
                f"{node.name} = {value}"
            )


        if isinstance(node, PrintNode):

            value = self.generate(node.value)

            return (
                f"print({value})"
            )

        elif isinstance(node, GroupNode):

            return "(" + self.generate(node.expression) + ")"

        elif isinstance(node, FunctionCallNode):

            arguments = ", ".join(
                self.generate(argument)
                for argument in node.arguments
            )

            return f"{node.name}({arguments})"


        raise Exception(
            f"Unknown node: {node}"
        )
