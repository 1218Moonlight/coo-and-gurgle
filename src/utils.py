class stack():
    def __init__(self):
        self.__st = []

    def top(self):
        return self.__st[-1]

    def list(self):
        return self.__st

    def size(self):
        return len(self.__st)

    def push(self, val):
        self.__st.append(val)

    def pop(self):
        return self.__st.pop()
