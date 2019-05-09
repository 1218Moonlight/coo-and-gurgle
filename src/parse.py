class AST(object):
    pass


class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right


class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value


class Exit(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value


class Main(object):
    def __init__(self, lexer, opcode):
        self.__lexer = lexer
        self.__currentToken = self.__lexer.getNextToken()
        self.__op = opcode

    def __error(self):
        raise Exception('Invalid syntax')

    def __eat(self, tokenType):
        if self.__currentToken.type == tokenType:
            self.__currentToken = self.__lexer.getNextToken()
        else:
            self.__error()

    def __factor(self):
        token = self.__currentToken
        if token.type == self.__op.hexToString(self.__op.정수):
            self.__eat(self.__op.hexToString(self.__op.정수))
            return Num(token)
        elif token.type == self.__op.hexToString(self.__op.나가기):
            self.__eat(self.__op.hexToString(self.__op.나가기))
            return Exit(token)

    def __term(self):
        node = self.__factor()
        while self.__currentToken.type in (self.__op.hexToString(self.__op.곱하기), self.__op.hexToString(self.__op.나누기)):
            token = self.__currentToken
            if token.type == self.__op.hexToString(self.__op.곱하기):
                self.__eat(self.__op.hexToString(self.__op.곱하기))
            elif token.type == self.__op.hexToString(self.__op.나누기):
                self.__eat(self.__op.hexToString(self.__op.나누기))

            node = BinOp(left=node, op=token, right=self.__factor())

        return node

    def __expr(self):
        node = self.__term()

        while self.__currentToken.type in (self.__op.hexToString(self.__op.더하기), self.__op.hexToString(self.__op.빼기)):
            token = self.__currentToken
            if token.type == self.__op.hexToString(self.__op.더하기):
                self.__eat(self.__op.hexToString(self.__op.더하기))
            elif token.type == self.__op.hexToString(self.__op.빼기):
                self.__eat(self.__op.hexToString(self.__op.빼기))

            node = BinOp(left=node, op=token, right=self.__term())

        return node

    def run(self):
        return self.__expr()
