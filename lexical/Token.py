from enum import Enum


class Token:
    class Type(Enum):
        INDENT = 1
        STRING = 2
        NEW_LINE = 3
        ID_OR_KEYWORD = 4
        ASSIGN = 5
        NUMBER = 6
        OPEN_PAREN = 7
        CLOSE_PAREN = 8
        COMMA = 9
        OPERATION = 10

    def __init__(self, value, type):
        self.value = value
        while self.value[-1:] == '\n':
            self.value = self.value[0:-1]
        self.type = type

    def __str__(self):
        return self.value + " " + str(self.type)
