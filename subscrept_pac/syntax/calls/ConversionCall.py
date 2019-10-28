from subscrept_pac.errors import TokenSyntaxError
from subscrept_pac.lexical import TokenStream, Token
from subscrept_pac.syntax import InterpreterObject
from subscrept_pac.syntax.keywords import Function


class FunctionCall(InterpreterObject):

    def __init__(self, parent: InterpreterObject):
        super().__init__(parent)
        self.function_identifier = self.token_stream.get_next_token()
        self.args = []

        open_paren = self.token_stream.peek_next_token()
        if open_paren.type != Token.Type.OPEN_PAREN:
            raise TokenSyntaxError(" Missing arguments of function", self.token_stream.peek_next_token())

        self.token_stream.get_next_token()
        while True:
            self.args.append(self.token_stream.get_next_token().value)
            if self.token_stream.peek_next_token().type == Token.Type.CLOSE_PAREN:
                break
            if self.token_stream.peek_next_token().type != Token.Type.COMMA:
                raise TokenSyntaxError("Missing comma to separate arguments", self.token_stream.peek_next_token())
            self.token_stream.get_next_token()
        self.token_stream.get_next_token()

    def get_value(self):
        if self.verbose:
            print("Calling function " + str(self.function_identifier.value) + " with arguments " + str(self.args))

        func = self.get_identifier(self.function_identifier.value)
        old = dict()
        for child in func.children:
            if type(child) is type(Function.Variable):
                old[child.variable_name] = child.value

        for i in range(0, len(self.args), 1):
            if self.get_identifier(self.args[i]):
                func.children[i].value = self.get_identifier(self.args[i]).get_value()
            else:
                func.children[i].value = self.args[i]

        self.value = func.get_value()
        for child in func.children:
            if type(child) == type(Function.Variable):
                self.get_identifier(child.variable_name).value = old[child.variable_name]

        return self.value

