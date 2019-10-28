from subscrept_pac.syntax import InterpreterObject
from subscrept_pac.syntax.objects.Line import Line


def new(parent: InterpreterObject):
    parent.token_stream.get_next_token()
    if parent.token_stream.peek_next_token().value.lower() == "line":
        return Line(parent)
    return InterpreterObject(None)
    # raise TokenSyntaxError("Missing class after new keyword", token_stream.peek_next_token())