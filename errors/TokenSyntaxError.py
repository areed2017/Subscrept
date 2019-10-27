from lexical import Token


class TokenSyntaxError(Exception):
    
    def __init__(self, message: str, token: Token):
        super(TokenSyntaxError, self).__init__("Syntax Eror; " + message + " at "\
                                               + str(token))