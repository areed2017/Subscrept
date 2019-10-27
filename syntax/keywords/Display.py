from syntax import InterpreterObject, Statement


class Display(InterpreterObject):

    def __init__(self, parent: InterpreterObject):
        super().__init__(parent)
        self.token_stream.get_next_token()
        self.value = Statement.Statement(self)

    def run(self):
        string_value = self.value.get_value()
        if type(string_value) == float:
            print(string_value, end="")
            return
        if type(string_value) == int:
            print(float(string_value), end ="")
            return
        split_val = string_value.split("@")
        for i in range(len(split_val)):
            if i % 2 == 0:
                print(split_val[i], end="")
            else:
                temp = self.get_identifier(split_val[i].split(" ")[0])
                if temp is not None:
                    print(str(temp.get_value()) + " ", end="")
                    if len(split_val[i].split(" ")) > 1:
                        print(" ".join(split_val[i].split(" ")[1:]), end="")
                else:
                    print("@" + split_val[i], end="")

