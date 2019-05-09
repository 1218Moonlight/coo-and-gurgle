class OP(object):
    def __init__(self):
        self.더하기 = 0x1
        self.빼기 = 0x2
        self.나누기 = 0x3
        self.곱하기 = 0x4
        self.나가기 = 0x5
        self.정수 = 0x6
        self.EOF = 0x7

        self.strToHex = {"더하기": self.더하기, "빼기": self.빼기, "나누기": self.나누기, "곱하기": self.곱하기,
                         "나가기": self.나가기, "정수": self.정수, "EOF": self.EOF}
        self.hexToStr = {self.더하기: "더하기", self.빼기: "빼기", self.나누기: "나누기", self.곱하기: "곱하기",
                         self.나가기: "나가기", self.정수: "정수", self.EOF: "EOF"}


class Main(OP):
    def hexToString(self, h):
        return self.hexToStr[h]

    def stringToHex(self, s):
        return self.strToHex[s]
