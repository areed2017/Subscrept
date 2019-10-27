from errors import TokenSyntaxError
from lexical import Token
from syntax import InterpreterObject, Statement
from syntax.keywords import Function


class For(InterpreterObject):

    def __init__(self, parent: InterpreterObject):
        super().__init__(parent)
        self.token_stream.get_next_token()
        each = self.token_stream.get_next_token()
        if each.value.lower() != "each":
            raise TokenSyntaxError("missing each after for", each)
        self.index = For.Variable(self, self.token_stream.get_next_token().value)

        from_ = self.token_stream.get_next_token()
        if from_.value.lower() != "from":
            raise TokenSyntaxError("missing each after for", from_)

        self.lower_bound = float(self.token_stream.get_next_token().value)

        to_ = self.token_stream.get_next_token()
        if to_.value.lower() != "to":
            raise TokenSyntaxError("missing each after for", to_)

        self.upper_bound = float(self.token_stream.get_next_token().value)

        while self.token_stream.peek_next_token() is not None and \
                self.token_stream.peek_next_token().type == Token.Type.INDENT:
            self.token_stream.get_next_token()
            Statement.Statement(self)

    def run(self):
        for i in range(int(self.lower_bound), int(self.upper_bound) + 1, 1):
            self.children[0].value = i
            super().run()

    class Variable(InterpreterObject):

        def __init__(self, parent: InterpreterObject, name):
            super().__init__(parent)
            self.identifier = name
            self.value = None


