from subscrept_pac.lexical import TokenStream, Token


class InterpreterObject:
    def __init__(self, parent, token_stream: TokenStream = None, flags=None):
        self.parent = parent
        self.children = []
        self.value = None
        self.identifier = None

        if token_stream is not None:
            self.token_stream = token_stream
        else:
            self.token_stream = parent.token_stream
        if flags is not None:
            self.verbose = True if ('v' in flags) else False
            self.discrept = True if ('d' in flags) else False
        else:
            self.verbose = parent.verbose
            self.discrept = parent.discrept

        if parent is not None:
            self.parent.children.append(self)

    def run(self):
        for child in self.children:
            child.run()

    def get_identifier(self, identifier, visited=None):
        if visited is None:
            visited = []

        if self in visited:
            return None

        visited.append(self)
        if identifier == self.identifier:
            return self

        for child in self.children:
            if child in visited:
                continue
            if child.get_identifier(identifier, visited.copy()) is not None:
                return child.get_identifier(identifier, visited)

        if self.parent is None:
            return None

        return self.parent.get_identifier(identifier, visited)

    def get_value(self):
        return self.value

    @staticmethod
    def check_new_line(token_stream: TokenStream):
        token = token_stream.peek_next_token()
        if token is not None and token.type == Token.Type.NEW_LINE:
            token_stream.get_next_token()
            return True
        return False

    @staticmethod
    def check_indents(token_stream: TokenStream, number_of_indent: int):
        for i in range(number_of_indent):
            token = token_stream.peek_next_token(i)
            if token is None or token.type != Token.Type.INDENT:
                return False

        for i in range(number_of_indent):
            token_stream.get_next_token()
        return True