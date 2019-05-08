from . import utils as u
from . import opcode
from . import lexer


class machine(u.stack):
    def __init__(self, code):
        self.lexer = lexer
        self.code = code
        self.stack = u.stack()
        self.pointer = 0
        self.op = opcode

    def run(self):
        bytecode = self.__compile(self.__getTokens())
        while self.pointer < len(bytecode):
            if bytecode[self.pointer] == self.op.정수:
                self.stack.push(int(bytecode[self.pointer + 1]))
                self.pointer = self.pointer + 1
            elif bytecode[self.pointer] == self.op.더하기:
                self.stack.push(self.stack.pop() + self.stack.pop())
            elif bytecode[self.pointer] == self.op.곱하기:
                self.stack.push(self.stack.pop() * self.stack.pop())
            elif bytecode[self.pointer] == self.op.빼기:
                self.stack.push(self.stack.pop() - self.stack.pop())
            elif bytecode[self.pointer] == self.op.나누기:
                self.stack.push(self.stack.pop() % self.stack.pop())
            elif bytecode[self.pointer] == self.op.출력:
                print(self.stack.pop())
            elif bytecode[self.pointer] == self.op.개행:
                pass
            else:
                raise RuntimeError(
                    "Bytecode Error %s" % (bytecode[self.pointer]))
            self.pointer = self.pointer + 1
        return self.list()

    def __compile(self, tokens):
        bytecode = []
        for v in tokens:
            if v['toTy'] == '정수':
                bytecode.append(self.op.stringToHex[v['toTy']])
                bytecode.append(v['toVal'])
            else:
                bytecode.append(self.op.stringToHex[v['toTy']])

        # return "".join(map(str, bytecode))
        return bytecode

    def __getTokens(self):
        return self.lexer.main(self.code).run()
