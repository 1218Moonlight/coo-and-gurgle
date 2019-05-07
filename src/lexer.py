from . import opcode as op
import tokenize


def __tok(ty, val):
    # token type = toTy, token value = toVal
    return {'toTy': ty, 'toVal': val}


def main(code):
    tokens = tokenize.generate_tokens(code.readline)
    return __tokens(tokens)


def __tokens(tokens):
    for toType, toValue, _, _, _ in tokens:
        if toType == tokenize.NUMBER:
            yield __tok(op.hexToString[op.정수], toValue)
        elif toType in [tokenize.STRING, tokenize.NAME, tokenize.OP] or toValue in op.stringToHex:
            if toValue == "변수":
                yield __tok(op.hexToString[op.변수], None)
            elif toValue == "더하기":
                yield __tok(op.hexToString[op.더하기], None)
            elif toValue == "곱하기":
                yield __tok(op.hexToString[op.곱하기], None)
            elif toValue == "빼기":
                yield __tok(op.hexToString[op.빼기], None)
            elif toValue == "나누기":
                yield __tok(op.hexToString[op.나누기], None)
            else:
                yield __tok(tokenize.tok_name[toType], toValue)
        elif toType == tokenize.NEWLINE:
            yield __tok(op.hexToString[op.개행], None)
        elif toType == tokenize.ENDMARKER:
            break
        else:
            raise RuntimeError("Unknown token %s: '%s'" % (tokenize.tok_name[toType], toValue))
