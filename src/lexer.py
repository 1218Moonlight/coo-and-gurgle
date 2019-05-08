class main:
    def __init__(self, code, opcode, tokenize):
        self.__op = opcode
        self.__tokenize = tokenize
        self.__code = code

    def run(self):
        tokens = self.__tokenize.generate_tokens(self.__code.readline)
        return self.__tokens(tokens)

    def __tok(self, ty, val):
        # token type = toTy, token value = toVal
        return {'toTy': ty, 'toVal': val}

    def __tokens(self, tokens):
        for toType, toValue, _, _, _ in tokens:
            if toType == self.__tokenize.NUMBER:
                yield self.__tok(self.__op.hexToString[self.__op.정수], toValue)
            elif toType in [self.__tokenize.STRING, self.__tokenize.NAME,
                            self.__tokenize.OP] or toValue in self.__op.stringToHex:
                if toValue == "변수":
                    yield self.__tok(self.__op.hexToString[self.__op.변수], None)
                elif toValue == "더하기":
                    yield self.__tok(self.__op.hexToString[self.__op.더하기], None)
                elif toValue == "곱하기":
                    yield self.__tok(self.__op.hexToString[self.__op.곱하기], None)
                elif toValue == "빼기":
                    yield self.__tok(self.__op.hexToString[self.__op.빼기], None)
                elif toValue == "나누기":
                    yield self.__tok(self.__op.hexToString[self.__op.나누기], None)
                elif toValue == "출력":
                    yield self.__tok(self.__op.hexToString[self.__op.출력], None)
                elif toValue == "나가기":
                    yield self.__tok(self.__op.hexToString[self.__op.나가기], None)
                else:
                    yield self.__tok(self.__tokenize.tok_name[toType], toValue)
            elif toType == self.__tokenize.NEWLINE:
                yield self.__tok(self.__op.hexToString[self.__op.개행], None)
            elif toType == self.__tokenize.ENDMARKER:
                break
            else:
                raise RuntimeError("Unknown token %s: '%s'" % (self.__tokenize.tok_name[toType], toValue))
