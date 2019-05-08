""" python3 """

from src import vm


def main():
    with open('test.cag', 'r', encoding='UTF8') as f:
        vm.machine(f).run()


if __name__ == '__main__':
    main()
