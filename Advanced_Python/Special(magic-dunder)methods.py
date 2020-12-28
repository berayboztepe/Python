# __blabla__ methods are dunder methods. Dunder means double underscores.

# init is the most common dunder method that we use as constructors.


class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@gmail.com'

    def fullname(self):
        return self.first + " " + self.last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # str is our to_string() method. We can define to_string method with the help of __str__ dunder method
    # str is more human-readable than __repr__ and prints it better way.
    def __str__(self):
        print("inside str")
        return "Name: {}, Surname: {}, Salary: {}, Email: {}".format(self.first, self.last, self.pay, self.email)

    # repr is similar to __str__ but without str, using str() will be give the same answer as repr()
    def __repr__(self):
        print("inside repr")
        return "Employee([{}, {}, {}])".format(self.fullname(), self.pay, self.email)

    # self is left side, other is right side. we're gonna add two employees by their pays
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Joseph', 'Turner', 20000)
emp_2 = Employee('Corey', 'Taylor', 15000)

print("1-", emp_1.fullname(), "2-", emp_2.fullname())
print(emp_2)  # before __str__ if we print emp_2, we see a <__main__.Employee instance at 0x10d5807e8>
# after __str__,  we see Name Corey, Surname Taylor, Salary 15000, Email CoreyTaylor@gmail.com
print(repr(emp_2))

# how to use len()
print(len('time'))
print('time'.__len__())  # we can use both
# but when we try the same to emp_1 we get the len of fullname() method! as 13
print(len(emp_1))

# when we print(1+2) it's actually using a method called __add__ we can also use this like:
print(int.__add__(1, 2))
print(str.__add__('a', 'b'))  # also string objects are using their own add dunder
print(emp_1 + emp_2)  # we can do this by __add__ dunder. if we do this without add dunder, we receive an error
# because the program does not know how to add these together

"""Python is a language based OOP. When we define a int, string etc. we can see that we can use len(), str(), 
int() to convert them etc. due to OOP. these are actually a dunder methods. FE, when we define a class, we cannot use
len(), str() etc. because classes are not objects. Objects are created from classes. Let's take a look:"""

print("\n")


class c1:
    pass


obj = c1()
# len(obj) as we see, we cannot use this. but if we do smt like:


class c2:
    def __len__(self):
        return 5


obj1 = c2()
print(len(obj1))  # we can use this one.


# another example
class c3:
    def __init__(self, num):
        self.list = [i for i in range(num)]

    def __str__(self):
        return str(self.list)

    def __getitem__(self, item):
        return self.list[item]

    def __len__(self):
        return len(self.list)

    def __setitem__(self, key, value):
        self.list[key] = value

    def __call__(self, *args, **kwargs):
        return "list({})".format(str(self.list))

    def __eq__(self, other):
        return self == other

    def __lt__(self, other):
        return self < other


obj2 = c3(5)
# print(obj2) we cannot print it because we do not have str or repr dunder
print(obj2.list)  # we can print it like this.

"""print(len(obj2))
for no in obj2:
    print(no)
print(obj2[1])"""
# these all will cause an error. If we want to use them, we have to implement __len__, __getitem__, __str__
# now we can see the results
print("Len = ", len(obj2))
for no in obj2:
    print(no)
print("obj2[1] = ", obj2[1])

# let's try to set an item in list with the help of __setitem__ dunder
# obj2[1] = 5 without __setitem__ we can not set the item

obj2[1] = 5
print(obj2)

# with __call__ method, we can use c3 as method. if we print obj2(), list will be printed as print(obj2)
print(obj2())

# with __eq__ we can compare equality of two numbers. with __lt__, if first number < second number, then return True
print(obj2[0].__eq__(obj2[1]))
print(obj2[0].__lt__(obj2[1]))
