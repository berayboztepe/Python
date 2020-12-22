class Stack:
    def __init__(self):
        self.st = []
        self.size = 6

    def push(self, data):
        if len(self.st) < self.size:
            if data not in self.st:
                self.st.append(data)
        else:
            print("Stack is Full for {}".format(data))

    def print(self):
        return[x for x in self.st]

    def pop(self):
        last = self.st[-1]
        self.st.remove(last)

    def peek(self):
        return self.st[-1]



st = Stack()
st.push(5)
st.push(5)
st.push(10)
st.push(15)
st.push(20)
st.push(25)
st.push(25)
st.push(35)
print("Stack -> ", st.print(), "\tPeek : ", st.peek())

st.pop()
print("After Pop -> ", st.print(), "\tPeek : ", st.peek())
st.pop()
print("After Pop -> ", st.print(), "\tPeek : ", st.peek())
st.pop()
print("After Pop -> ", st.print(), "\tPeek : ", st.peek())
