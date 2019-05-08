""" python3 """

from src import vm
import sys, os, io


def cagRun():
    cagPath = sys.argv[1]
    extension = os.path.splitext(cagPath)[1].replace(".", "")
    if not extension == "cag":
        raise RuntimeError("Error Extension 'not .cag'")

    with open(cagPath, 'r', encoding='UTF8') as f:
        vm.machine(sys, f).run()


def repl():
    print('[INFO] \"나가기\"를 입력하면 repl가 종료됩니다.')

    while True:
        source = input('>> ')
        vm.machine(sys, io.StringIO(source)).run()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        cagRun()
    else:
        repl()
