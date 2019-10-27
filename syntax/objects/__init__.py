from errors import TokenSyntaxError
from lexical import TokenStream
from syntax import InterpreterObject
from syntax.objects.Line import Line


def new(parent: InterpreterObject):
    parent.token_stream.get_next_token()
    if parent.token_stream.peek_next_token().value.lower() == "line":
        return Line(parent)
    return InterpreterObject(None)
    # raise TokenSyntaxError("Missing class after new keyword", token_stream.peek_next_token())