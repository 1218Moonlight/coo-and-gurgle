class Main:
    def __init__(self, source, lexer, parse, opcode, sys):
        self.__sys = sys
        self.__op = opcode
        self.__lexer = lexer.Main(source, self.__op)
        self.__parse = parse.Main(self.__lexer, self.__op)

    def __view(self, node):
        method_name = 'view_' + type(node).__name__
        visitor = getattr(self, method_name, self.__Error)
        return visitor(node)

    def __Error(self, node):
        raise Exception('No view_{} method'.format(type(node).__name__))

    def view_BinOp(self, node):
        if node.op.type == self.__op.hexToString(self.__op.더하기):
            return self.__view(node.left) + self.__view(node.right)
        elif node.op.type == self.__op.hexToString(self.__op.빼기):
            return self.__view(node.left) - self.__view(node.right)
        elif node.op.type == self.__op.hexToString(self.__op.곱하기):
            return self.__view(node.left) * self.__view(node.right)
        elif node.op.type == self.__op.hexToString(self.__op.나누기):
            return self.__view(node.left) / self.__view(node.right)

    def view_Num(self, node):
        return node.value

    def view_Exit(self, node):
        self.__sys.exit(node.value)

    def run(self):
        tree = self.__parse.run()
        return self.__view(tree)
