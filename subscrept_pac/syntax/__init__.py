from subscrept_pac.lexical import TokenStream
from subscrept_pac.syntax.InterpreterObject import InterpreterObject
from subscrept_pac.syntax.Statement import Statement


class Interpreter(InterpreterObject):

    def __init__(self, token_stream: TokenStream, flags):
        super().__init__(None, token_stream, flags)
        while not token_stream.is_empty():
            Statement(self)
