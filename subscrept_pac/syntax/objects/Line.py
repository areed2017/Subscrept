from subscrept_pac.syntax import InterpreterObject


class Line(InterpreterObject):

    def __init__(self, parent: InterpreterObject):
        super().__init__(parent)
        self.token_stream.get_next_token()
        if self.discrept:
            self.value = "<br />"
        else:
            self.value = "\n"
