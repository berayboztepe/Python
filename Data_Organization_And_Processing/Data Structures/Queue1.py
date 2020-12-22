class Queue:
    def __init__(self, data):
        self.data = data
        self.next = None


class First:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        q = Queue(data)
        if self.front is None:
            self.front = q
            self.rear = q
            q.next = None
            return
        q1 = self.front
        if q1.data == data: return

        while q1.next:
            if data == q1.data: return
            q1 = q1.next

        if q1.data == data: return
        q1.next = q
        self.rear = q

    def print(self):
        pr = self.front
        print("[", end="")
        while pr:
            if pr.next is None:
                print(pr.data, end="")
            else:
                print(pr.data, end=", ")
            pr = pr.next
        print("]", end="")
    def dequeue(self):
        temp = self.front
        self.front = temp.next
        temp.next = None

    def size(self):
        count = 0
        beg = self.front
        while beg:
            count += 1
            beg = beg.next
        return count
    def peek(self):
        return self.front.data

    def peeklast(self):
        return self.rear.data



q = First()
q.front = Queue(25)
q.enqueue(25)
q.enqueue(20)
q.enqueue(35)
q.enqueue(30)
q.enqueue(45)
q.enqueue(5)
q.enqueue(10)
q.enqueue(10)
q.enqueue(5)
print("Queue")
q.print()
print("\tSize : ", q.size())
print("\nFront : ", q.peek(), end="--")
print("Rear : ", q.peeklast())

print("\n\n")

print("After dequeue")
q.dequeue()
q.print()
print("\tSize : ", q.size())
print("\nFront : ", q.peek(), end="--")
print("Rear : ", q.peeklast())

print("\n\n")

print("After dequeue")
q.dequeue()
q.print()
print("\tSize : ", q.size())
print("\nFront : ", q.peek(), end="--")
print("Rear : ", q.peeklast())

print("\n\n")

print("After dequeue")
q.dequeue()
q.print()
print("\tSize : ", q.size())
print("\nFront : ", q.peek(), end="--")
print("Rear : ", q.peeklast())

print("\n\n")

print("After dequeue")
q.dequeue()
q.print()
print("\tSize : ", q.size())
print("\nFront : ", q.peek(), end="--")
print("Rear : ", q.peeklast())


