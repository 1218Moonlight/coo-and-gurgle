from . import utils as u
from . import opcode as op


class machine(u.stack):
    def __init__(self, tokens):
        self.tokens = tokens
        self.stack = u.stack()
        self.pointer = 0

    def run(self):
        bytecode = self.__compile(self.tokens)
        while self.pointer < len(bytecode):
            if bytecode[self.pointer] == op.정수:
                self.stack.push(int(bytecode[self.pointer + 1]))
                self.pointer = self.pointer + 1
            elif bytecode[self.pointer] == op.더하기:
                self.stack.push(self.stack.pop() + self.stack.pop())
            elif bytecode[self.pointer] == op.곱하기:
                self.stack.push(self.stack.pop() * self.stack.pop())
            elif bytecode[self.pointer] == op.빼기:
                self.stack.push(self.stack.pop() - self.stack.pop())
            elif bytecode[self.pointer] == op.나누기:
                self.stack.push(self.stack.pop() % self.stack.pop())
            elif bytecode[self.pointer] == op.출력:
                print(self.stack.pop())
            elif bytecode[self.pointer] == op.개행:
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
                bytecode.append(op.stringToHex[v['toTy']])
                bytecode.append(v['toVal'])
            else:
                bytecode.append(op.stringToHex[v['toTy']])

        # return "".join(map(str, bytecode))
        return bytecode
