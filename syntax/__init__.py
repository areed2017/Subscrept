from lexical import TokenStream
from syntax.InterpreterObject import InterpreterObject
from syntax.Statement import Statement


class Interpreter(InterpreterObject):

    def __init__(self, token_stream: TokenStream, flags):
        super().__init__(None, token_stream, flags)
        while not token_stream.is_empty():
            Statement(self)
