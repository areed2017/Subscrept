from subscrept_pac.syntax import InterpreterObject


class String(InterpreterObject):

    def __init__(self, parent: InterpreterObject):
        super().__init__(parent)
        self.value = self.token_stream.get_next_token().value
