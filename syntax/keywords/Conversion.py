from errors import TokenSyntaxError
from lexical import Token
from syntax import InterpreterObject


class Conversion(InterpreterObject):

    def __init__(self, parent: InterpreterObject):
        super().__init__(parent)
        self.token_stream.get_next_token()
        self.identifier = self.token_stream.get_next_token()

        assignment = self.token_stream.get_next_token()
        if assignment.type != Token.Type.ASSIGN:
            raise TokenSyntaxError("Conversion has missing assignment. Expected =", assignment)
        self.value = self.token_stream.get_next_token().value

    class AltConversion(InterpreterObject):
        def __init__(self,parent: InterpreterObject):
            super().__init__(parent)
