from .Token import Token
from .TokenStream import TokenStream


def parse(data) -> TokenStream:
    token_stream = TokenStream(data)
    parse_data = data.replace('    ', '\t')
    parse_data = parse_data.replace('\r', '')
    parse_data = parse_data.replace('(', ' (')
    parse_data = parse_data.replace(')', ' )')
    reserved = ['(', ')', ',', '\n', '\t']

    i = 0
    while i < len(parse_data):
        token = ""
        c = parse_data[i]
        if c == '\t':
            token_stream + Token("Tab", Token.Type.INDENT)
        elif c == '(':
            token_stream + Token(c, Token.Type.OPEN_PAREN)
        elif c == ')':
            token_stream + Token(c, Token.Type.CLOSE_PAREN)
        elif c == ',':
            token_stream + Token(c, Token.Type.COMMA)
        elif c in ['+', '-', '/', '*']:
            token_stream + Token(c, Token.Type.OPERATION)
        elif c == '"':
            i += 1
            c = parse_data[i]
            while c != '"':
                token += c
                i += 1
                if i >= len(parse_data):
                    break
                c = parse_data[i]
            token = token.replace(' (', '(')
            token = token.replace(' )', ')')
            token_stream + Token(token, Token.Type.STRING)
        elif c == '=':
            token_stream + Token(c, Token.Type.ASSIGN)
        elif c.isdigit():
            while c.isdigit() or c == '.':
                token += c
                i += 1
                if i >= len(parse_data):
                    break
                c = parse_data[i]
            if len(token) > 0:
                token_stream + Token(token, Token.Type.NUMBER)
        else:
            while c != ' ' and c not in reserved:
                token += c
                i += 1
                if i >= len(parse_data):
                    break
                c = parse_data[i]
                if c in reserved:
                    i -= 1
            if len(token) > 0:
                token_stream + Token(token, Token.Type.ID_OR_KEYWORD)

        i += 1

    return token_stream
