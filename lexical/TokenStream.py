from lexical import Token


class TokenStream:

    def __init__(self, data):
        self.tokens = list()
        self.index = 0
        self.data = data

    def __add__(self, token: Token) -> None:
        self.tokens.append(token)

    def get_next_token(self) -> Token:
        if self.index >= len(self.tokens):
            return None
        token = self.tokens[self.index]
        self.index += 1
        return token

    def peek_next_token(self, index=0) -> Token:
        if self.index + index >= len(self.tokens):
            return None
        token = self.tokens[self.index + index]
        return token

    def is_empty(self):
        return self.index + 1 >= len(self.tokens)