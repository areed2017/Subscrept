from subscrept_pac.lexical import TokenStream, Token
from subscrept_pac.syntax import InterpreterObject


class Algorithm(InterpreterObject):

    def __init__(self, parent: InterpreterObject):
        super().__init__(parent)
        token = self.token_stream.get_next_token()
