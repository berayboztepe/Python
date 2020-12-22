class Queue:
    def __init__(self):
        self.qu = []

    def enqueue(self, data):
        if data not in self.qu:
            self.qu.append(data)

    def print(self):
        return[x for x in self.qu]

    def dequeue(self):
        dq = self.qu[0]
        self.qu.remove(dq)

    def size(self):
        return[len(self.qu)][0]

    def peek(self):
        return self.qu[0]



q = Queue()
q.enqueue(10)
q.enqueue(15)
q.enqueue(20)
q.enqueue(20)
q.enqueue(25)
q.enqueue(30)
q.enqueue(5)
q.enqueue(0)
print("Queue -> ", q.print())
print("Size : ", q.size())
q.dequeue()
print("First in First out -> ", q.print())
print("Size : ", q.size())
q.dequeue()
print("First in First out -> ", q.print())
print("Size : ", q.size())
q.dequeue()
print("First in First out -> ", q.print())
print("Size : ", q.size())
print("Peek : ", q.peek())





