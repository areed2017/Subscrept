from subscrept_pac.errors import TokenSyntaxError
from subscrept_pac.lexical import Token
from subscrept_pac.syntax import InterpreterObject, Statement


class Variable(InterpreterObject):

    def __init__(self, parent: InterpreterObject):
        super().__init__(parent)
        self.variable_name = self.token_stream.get_next_token().value
        self.reassignment = False
        if self.token_stream.peek_next_token(1) is None:
            return
        if self.token_stream.peek_next_token(1).type == Token.Type.ASSIGN:
            self.reassignment = True
            self.token_stream.get_next_token()
            self.variable_value = Statement.Statement(self)

    def run(self):
        if self.reassignment:
            variable = self.get_identifier(self.variable_name)
            variable.value = str(self.variable_value.get_value())
            if self.verbose:
                print("Variable " + str(self.variable_name) + " reassigned to " +
                      str(self.variable_value.get_value()))
        super().run()

    def get_value(self):
        identifier = self.get_identifier(self.variable_name)
        if identifier == None:
            raise TokenSyntaxError("No such identifier", self.variable_name)
        return identifier.get_value()
