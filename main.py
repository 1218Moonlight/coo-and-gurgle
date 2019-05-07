from src import lexer
from src import vm


def main():
    with open('test.cag', 'r', encoding='UTF8') as f:
        tokens = list(lexer.main(f))
        print(vm.machine(tokens).run())


if __name__ == '__main__':
    main()
