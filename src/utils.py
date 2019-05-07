class st:
    stDic = []


class stack(st):
    def top(self):
        return st.stDic[-1]

    def list(self):
        return st.stDic

    def size(self):
        return len(st.stDic)

    def push(self, val):
        st.stDic.append(val)

    def pop(self):
        return st.stDic.pop()