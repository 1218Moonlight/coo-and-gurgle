""" python3 """

from src import interpreter, lexer, parse
import sys
import os


class VM:
    def __init__(self):
        self.__sys = sys
        self.__os = os
        self.__inter = interpreter

    def run(self):
        if len(self.__sys.argv) > 1:
            self.__cagRun()
        else:
            self.__repl()

    def __cagRun(self):
        cagPath = self.__sys.argv[1]
        extension = self.__os.path.splitext(cagPath)[1].replace(".", "")
        if not extension == "cag":
            raise RuntimeError("Error Extension 'not .cag'")

        with open(cagPath, 'r', encoding='UTF8') as f:
            # todo: 가장 윗줄 코드만 처리됨. 여러 줄 처리가 되도록 해야 함. (*OPCODE 재정의 해야함.)
            result = self.__inter.Main(f.readline().split(), lexer, parse, self.__sys).run()
            print(result)

    def __repl(self):
        print('[INFO] \"나가기\"를 입력하면 터미널이 종료됩니다.')

        while True:
            source = input('>> ')
            result = self.__inter.Main(source.split(), lexer, parse, self.__sys).run()
            print(result)


if __name__ == '__main__':
    VM().run()
