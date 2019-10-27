import sys

from lexical import parse
from syntax import Interpreter

VERBOSE = True

if __name__ == '__main__':
    flags = dict()
    file = None
    for arg in sys.argv:
        if '-' in arg:
            flags[arg[1:]] = True
        else:
            file = sys.argv[1]

    if file is None:
        quit()

    with open(file) as file:
            token_stream = parse(file.read())
            interpreter = Interpreter(token_stream, flags=flags)
            interpreter.run()
