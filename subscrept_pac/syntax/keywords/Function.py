from subscrept_pac.errors import TokenSyntaxError
from subscrept_pac.lexical import Token
from subscrept_pac.syntax import InterpreterObject
from subscrept_pac.syntax.math import Expression


class Function(InterpreterObject):

    def __init__(self, parent: InterpreterObject):
        super().__init__(parent)
        self.token_stream.get_next_token()
        self.identifier = self.token_stream.get_next_token().value

        open_paren = self.token_stream.peek_next_token()
        if open_paren.type != Token.Type.OPEN_PAREN:
            raise TokenSyntaxError(" Missing arguments of function", self.token_stream.peek_next_token())

        self.token_stream.get_next_token()
        while True:
            Function.Variable(self, self.token_stream.get_next_token().value)

            if self.token_stream.peek_next_token().type == Token.Type.CLOSE_PAREN:
                break
            if self.token_stream.peek_next_token().type != Token.Type.COMMA:
                raise TokenSyntaxError("Missing comma to separate arguments", self.token_stream.peek_next_token())
            self.token_stream.get_next_token()
        self.token_stream.get_next_token()

        assignment = self.token_stream.get_next_token()
        if assignment.type != Token.Type.ASSIGN:
            raise TokenSyntaxError("Constant has missing assignment. Expected =", assignment)
        self.value = Expression(self)

    def get_value(self):
        return self.value.get_value()

    def run(self):
        if self.verbose:
            print("Defining Function " + str(self.identifier) + " With arguments ", end="")
            for child in self.children:
                if type(child) == Function.Variable:
                    print(str(child.identifier) + ", ", end="")
            print(" and the expression " + str(self.value))

    class Variable(InterpreterObject):

        def __init__(self, parent: InterpreterObject, name):
            super().__init__(parent)
            self.identifier = name
            self.value = None

        def get_value(self):
            return self.value
