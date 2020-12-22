
class Tree:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def printtree(self):

        print(self.data, end=" ")

        if self.left:
            self.left.printtree()


        if self.right:
            self.right.printtree()


    def insert(self, data):
        if self.data:
            if self.data < data:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.insert(data)
            elif self.data > data:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.insert(data)
        else:
             self.data = data

    def findval(self, data):
        if data < self.data:
            if self.left is None:
                print("{} is Not Found!".format(data))
                return
            return self.left.findval(data)
        elif data > self.data:
            if self.right is None:
                print("{} is Not Found!".format(data))
                return
            return self.right.findval(data)
        else:
            print("{} is Found!".format(self.data))

    def nodecount(self, r):
        return [0 if r is None else self.nodecount(r.right) + self.nodecount(r.left) + 1][0]

    def leafcount(self, r):
        if r is None: return 0
        return [1 if r.left is None and r.right is None else self.leafcount(r.right) + self.leafcount(r.left)][0]

    def foo(self, r):
        node = self.nodecount(r)
        leaf = self.leafcount(r)
        return node-leaf

    def minrightvalue(self, r):
        while r.left:
            r = r.left
        return r


    def remove(self, data, r):
        if r is None:
            return r

        if data > r.data:
            r.right = self.remove(data, r.right)

        elif data < r.data:
            r.left = self.remove(data, r.left)

        else:
            if r.right is None:
                temp = r.left
                r = None
                return temp

            elif r.left is None:
                temp = r.right
                r = None
                return temp

            temp = self.minrightvalue(r.right)

            r.data, temp.data = temp.data, r.data

            r.right = self.remove(temp.data, r.right)


        return r


r = Tree(25)
r.insert(30)
r.insert(20)
r.insert(35)
r.insert(40)
r.insert(15)
r.insert(27)
r.insert(44)
r.insert(31)
r.findval(15)
r.findval(23)
r.findval(20)


print("\n\n")
print("Node Count: ", r.nodecount(r))
print("Leaf Count: ", r.leafcount(r))
print("Internal Node Count: ", r.foo(r))
print("\n\n")
print("\nTree")
r.printtree()
print("\n")
r.remove(44, r)
print("\nAfter removing 44")
r.printtree()
print("\n")
r.remove(20, r)
print("\nAfter removing 20")
r.printtree()
print("\n")
r.remove(25, r)
print("\nAfter removing 25")
r.printtree()



