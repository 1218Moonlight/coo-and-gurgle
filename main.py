""" python3 """

from src import vm
import sys, os


def cagRun():
    cagPath = sys.argv[1]
    extension = os.path.splitext(cagPath)[1].replace(".", "")
    if not extension == "cag":
        raise RuntimeError("Error Extension 'not .cag'")

    with open(cagPath, 'r', encoding='UTF8') as f:
        vm.machine(f).run()


def repl():
    print("...")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        cagRun()
    else:
        repl()
