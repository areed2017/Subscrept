from errors import TokenSyntaxError
from lexical import TokenStream, Token
from syntax import InterpreterObject


class Constant(InterpreterObject):

    def __init__(self, parent: InterpreterObject):
        super().__init__(parent)
        self.token_stream.get_next_token()
        self.identifier = self.token_stream.get_next_token().value
        assignment = self.token_stream.get_next_token()
        if assignment.type != Token.Type.ASSIGN:
            raise TokenSyntaxError("Constant has missing assignment. Expected =", assignment)
        self.value = self.token_stream.get_next_token().value

    def run(self):
        if self.verbose:
            print("Constant " + str(self.identifier) + " assigned to " +
                  str(self.value))
        super().run()
