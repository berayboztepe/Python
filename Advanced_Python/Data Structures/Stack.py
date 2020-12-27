class Stack:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.size = 6


class First:
    def __init__(self):
        self.top = None
        self.first = None

    def push(self, data):
        s = Stack(data)

        if self.size() == False:
            print("Stack is Full for {}".format(data))
            return

        else:
            if self.first is None:
                self.first = s
                self.top = s
                s.next = None
                return

            s1 = self.first

            while s1.next:
                if s1.data == data: return
                s1 = s1.next

            if s1.data == data: return
            s1.next = s
            self.top = s

            if not self.size() == 5:
                self.top.next = None


    def size(self):
        tp = self.first
        count = 0
        while tp:
            count += 1
            tp = tp.next
        return[True if count <= 5 else False][0]

    def print(self):
        tp = self.first
        while tp:
            if tp != self.top:
                print("|", tp.data, end=" ")
            else:
                print("|", tp.data, end=" |")
            tp = tp.next

    def pop(self):
        temp = self.first
        while temp.next != self.top:
            temp = temp.next

        free = self.top
        temp.next = None
        self.top = temp
    def peek(self):
        return self.top.data

s = First()
s.first = Stack(5)
s.push(10)
s.push(15)
s.push(20)
s.push(30)
s.push(20)
s.push(30)
s.push(40)
s.push(50)

print("\n\n")
print("Stack")
s.print()
print("\tPeek : ", s.peek())

s.pop()
print("\n\n")
print("After Pop")
s.print()
print("\tPeek : ", s.peek())

s.pop()
print("\n\n")
print("After Pop")
s.print()
print("\tPeek : ", s.peek())

s.pop()
print("\n\n")
print("After Pop")
s.print()
print("\tPeek : ", s.peek())

s.pop()
print("\n\n")
print("After Pop")
s.print()
print("\tPeek : ", s.peek())

s.push(20)
print("\n\n")
print("After Push")
s.print()
print("\tPeek : ", s.peek())
