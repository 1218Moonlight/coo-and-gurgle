from . import utils as u
from . import opcode
from . import lexer
import tokenize


class machine:
    def __init__(self, code):
        self.__stack = u.stack()
        self.__op = opcode
        self.__lexer = lexer.main(code, self.__op, tokenize)
        self.__pointer = 0

    def run(self):
        bytecode = self.__compile(self.__getTokens())
        while self.__pointer < len(bytecode):
            if bytecode[self.__pointer] == self.__op.정수:
                self.__stack.push(int(bytecode[self.__pointer + 1]))
                self.__pointer = self.__pointer + 1
            elif bytecode[self.__pointer] == self.__op.더하기:
                self.__stack.push(self.__stack.pop() + self.__stack.pop())
            elif bytecode[self.__pointer] == self.__op.곱하기:
                self.__stack.push(self.__stack.pop() * self.__stack.pop())
            elif bytecode[self.__pointer] == self.__op.빼기:
                self.__stack.push(self.__stack.pop() - self.__stack.pop())
            elif bytecode[self.__pointer] == self.__op.나누기:
                self.__stack.push(self.__stack.pop() / self.__stack.pop())
            elif bytecode[self.__pointer] == self.__op.출력:
                print(self.__stack.pop())
            elif bytecode[self.__pointer] == self.__op.개행:
                pass
            else:
                raise RuntimeError(
                    "Bytecode Error %s" % (bytecode[self.__pointer]))
            self.__pointer = self.__pointer + 1

    def __compile(self, tokens):
        bytecode = []
        for v in tokens:
            if v['toTy'] == '정수':
                bytecode.append(self.__op.stringToHex[v['toTy']])
                bytecode.append(v['toVal'])
            else:
                bytecode.append(self.__op.stringToHex[v['toTy']])

        # return "".join(map(str, bytecode))
        return bytecode

    def __getTokens(self):
        return self.__lexer.run()
