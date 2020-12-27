class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None



class FirstNode:
    def __init__(self):
        self.head = None

    def print(self):
        printval = self.head
        while printval:
            if printval.next is None:
                print(printval.data)
            else:
                print(printval.data, end='->')
            printval = printval.next

    def insertbeginning(self, data):
        n = Node(data)
        n.next = self.head
        self.head = n

    def insertending(self, data):
        n = Node(data)

        if self.head is None:
            self.head = n
            return

        l = self.head
        while l.next:
            l = l.next

        l.next = n

    def insertafter_l(self, data, afdata):
        n = Node(data)
        l1 = self.head

        while l1.data is not afdata:
            l1 = l1.next
            if l1 is None:
                print("{} is not in list".format(afdata))
                return

        n.next = l1.next
        l1.next = n

    def remove(self, data):
        l = self.head

        if l is not None:
            if l.data == data:
                self.head = l.next
                l = None
                return

        while l.next.data is not data:
            l = l.next
            if l is None:
                print("{} is not in list".format(data))
                return
        l1 = l.next
        l.next = l1.next
        l1.next = None

    def sort(self):
        l = self.head

        while l:
            flag = True

            l1 = self.head
            while l1:
                if not l1.next is None:
                    l2 = l1.next
                    if l1.data > l2.data:
                        l1.data, l2.data = l2.data, l1.data

                        flag = False

                l1 = l1.next

            l = l.next

            if flag == True:
                break






l = FirstNode()
l.head = Node(30)
l.insertbeginning(25)
l.insertending(35)
l.insertending(40)
l.insertafter_l(27, 25)
l.insertafter_l(33, 30)
l.insertafter_l(37, 35)
l.insertafter_l(42, 40)
l.insertafter_l(22, 10)
l.insertafter_l(45, 30)
l.insertafter_l(21, 40)
l.remove(33)
l.remove(25)
l.remove(42)
l.insertafter_l(20, 30)
l.insertending(10)
l.sort()
#27->30->45->35->37->40->21

l.print()
