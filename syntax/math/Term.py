from errors import TokenSyntaxError
from lexical import Token
from syntax import InterpreterObject
from syntax.math.Factor import Factor


class Term(InterpreterObject):

    def __init__(self, parent: InterpreterObject):
        super().__init__(parent)
        self.factor_1 = Factor(self)

        self.op = self.token_stream.peek_next_token()
        if self.op is None:
            self.op = Token('', Token.Type.NEW_LINE)
        if self.op.value in ['*', '/']:
            self.op = self.token_stream.get_next_token()
            self.factor_2 = Term(self)

    def get_value(self):
        if self.op.value not in ['*', '/']:
            return self.factor_1.get_value()

        val1 = float(self.factor_1.get_value())
        val2 = float(self.factor_2.get_value())

        if self.op.value == "*":
            return val1 * val2
        if self.op.value == "/":
            return val1 / val2

    def __str__(self):
        if self.op.value not in ['*', '/']:
            return str(self.factor_1)
        return "(" + str(self.factor_1) + " " + self.op.value + " " + str(self.factor_2) + ")"