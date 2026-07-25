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


class Generator:

    def generate(self, node, indent=0):

        indentation = "    " * indent

        # ----------------------------
        # Whole program
        # ----------------------------

        if isinstance(node, ProgramNode):

            output = []

            for statement in node.statements:
                output.append(
                    self.generate(statement, indent)
                )

            return "\n".join(output)

        if isinstance(node, BooleanNode):

            return str(node.value)

        # ----------------------------
        # Literals
        # ----------------------------

        if isinstance(node, NumberNode):
            return str(node.value)

        if isinstance(node, StringNode):
            return f'"{node.value}"'

        if isinstance(node, VariableNode):
            return node.name

        # ----------------------------
        # Expressions
        # ----------------------------

        if isinstance(node, GroupNode):
            return f"({self.generate(node.expression)})"

        if isinstance(node, BinaryOperationNode):

            left = self.generate(node.left)

            right = self.generate(node.right)

            return f"{left} {node.operator} {right}"

        if isinstance(node, FunctionCallNode):

            arguments = ", ".join(
                self.generate(argument)
                for argument in node.arguments
            )

            return (
                ("    " * indent)
                + f"{node.name}({arguments})"
            )

        # ----------------------------
        # Statements
        # ----------------------------

        if isinstance(node, AssignmentNode):

            value = self.generate(node.value)

            return (
                ("    " * indent)
                + f"{node.name} = {value}"
            )

        if isinstance(node, PrintNode):

            value = self.generate(node.value)

            return (
                ("    " * indent)
                + f"print({value})"
            )

        if isinstance(node, FunctionCallNode):

            arguments = ", ".join(
                self.generate(argument)
                for argument in node.arguments
            )

            return (
                ("    " * indent)
                + f"{node.name}({arguments})"
            )

        if isinstance(node, ReturnNode):

            value = self.generate(node.value)

            return f"{indentation}return {value}"

        # ----------------------------
        # Function definitions
        # ----------------------------

        if isinstance(node, IfNode):

            indentation = "    " * indent

            lines = [
                f"{indentation}if {self.generate(node.condition)}:"
            ]

            for statement in node.body:

                lines.append(
                    self.generate(statement, indent + 1)
                )

            return "\n".join(lines)

        if isinstance(node, FunctionDefinitionNode):

            parameters = ", ".join(node.parameters)

            lines = [
                f"{indentation}def {node.name}({parameters}):"
            ]

            if len(node.body) == 0:

                lines.append(
                    f"{indentation}    pass"
                )

            else:

                for statement in node.body:

                    generated = self.generate(
                        statement,
                        indent + 1
                    )


                    lines.append(generated)

            return "\n".join(lines)

        raise Exception(
            f"Unknown node: {node}"
        )
