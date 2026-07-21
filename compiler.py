class Compiler:

    def compile(self, code):

        output = []

        for line in code.splitlines():

            line = line.strip()

            if line.startswith("print "):

                text = line[6:]

                output.append(f"print({text})")

            else:

                output.append(line)

        return "\n".join(output)
