from errors import TokenSyntaxError
from lexical import Token
from syntax import InterpreterObject
from syntax.math import Term


class Factor(InterpreterObject):

    def __init__(self, parent: InterpreterObject):
        super().__init__(parent)
        self.value = self.token_stream.get_next_token()
        if self.value.type == Token.Type.OPERATION:
            Term(self)

    def get_value(self):
        if len(self.children) == 0:
            if self.value.type == Token.Type.NUMBER:
                return float(self.value.value)
            return self.get_identifier(self.value.value).get_value()
        else:
            if self.value == "-":
                return -1 * self.children[0].get_value()
            if self.value == "+":
                return 1 * self.children[0].get_value()
            raise TokenSyntaxError("Cannot apply math operator without leading term", self.value)

    def __str__(self):
        return "(" + str(self.value.value) + ")"
