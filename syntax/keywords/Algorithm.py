from lexical import TokenStream, Token
from syntax import InterpreterObject


class Algorithm(InterpreterObject):

    def __init__(self, parent: InterpreterObject):
        super().__init__(parent)
        token = self.token_stream.get_next_token()
