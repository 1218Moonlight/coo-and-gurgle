class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()


class Main:
    def __init__(self, code):
        self.__code = code

        self.__pos = 0
        self.__current_char = self.__code[self.__pos]

    def __skipWhitespace(self):
        while self.__current_char is not None and self.__current_char.isspace():
            self.__advance()

    def __advance(self):
        self.__pos += 1
        if self.__pos > len(self.__code) - 1:
            self.__current_char = None
        else:
            self.__current_char = self.__code[self.__pos]

    def __integer(self):
        result = ''
        while self.__current_char is not None and self.__current_char.isdigit():
            result += self.__current_char
            self.__advance()
        return int(result)

    def getNextToken(self):
        while self.__current_char is not None:
            if self.__current_char.isspace():
                self.__skipWhitespace()
                continue
            elif self.__current_char.isdigit():
                return Token('정수', self.__integer())

            elif self.__current_char == '더하기':
                self.__advance()
                return Token('더하기', None)

            elif self.__current_char == '곱하기':
                self.__advance()
                return Token('곱하기', None)

            elif self.__current_char == '빼기':
                self.__advance()
                return Token('빼기', None)

            elif self.__current_char == '나누기':
                self.__advance()
                return Token('나누기', None)

            elif self.__current_char == '나가기':
                self.__advance()
                return Token('나가기', 0)
            else:
                raise RuntimeError("Unknown token : '%s'" % self.__current_char)

        return Token('EOF', None)
