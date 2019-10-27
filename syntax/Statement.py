from lexical import Token
from syntax import InterpreterObject
from syntax.calls import FunctionCall
from syntax.keywords import *
from syntax.objects import new
from syntax.types import *
from syntax.calls.Variable import Variable
from syntax.math import Expression


class Statement(InterpreterObject):

    def __init__(self, parent: InterpreterObject):
        super().__init__(parent)
        token = self.token_stream.peek_next_token()
        if token.type == Token.Type.ID_OR_KEYWORD:
            if token.value.lower() == "constant":
                Constant(self)
            elif token.value.lower() == "algorithm":
                Algorithm(self)
            elif token.value.lower() == "function":
                Function(self)
            elif token.value.lower() == "conversion":
                Conversion(self)
            elif token.value.lower() == "for":
                For(self)
            elif token.value.lower() == "display":
                Display(self)
            elif token.value.lower() == "new":
                new(self)
            else:
                if self.token_stream.peek_next_token(1) is None:
                    Variable(self)
                elif self.token_stream.peek_next_token(1).type == Token.Type.OPEN_PAREN:
                    FunctionCall(self)
                elif self.token_stream.peek_next_token(1).type == Token.Type.OPERATION:
                    Expression(self)
                else:
                    Variable(self)
        elif token.type == Token.Type.STRING:
            String(self)
        elif token.type == Token.Type.NUMBER:
            Expression(self)
        else:
            self.token_stream.get_next_token()

    def get_value(self):
        return self.children[0].get_value()
