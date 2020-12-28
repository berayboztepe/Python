from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque

# with counter, we can count the different values in a string, list, dict, tuple etc.
a = "adiabatic"

my_counter = Counter(a)

print(my_counter)  # it returns a dict!

""" print(my_counter.items()) we can also use these
 print(my_counter.keys())
 print(my_counter.values())"""

# if we wanna see the most common one:
print(my_counter.most_common(1))  # the first most common one

# to see all the different elements as a list
print(list(my_counter.elements()))

# counter is same as this code
my_counter1 = {}
for i in a:
    if i in my_counter1:
        my_counter1[i] += 1
    else:
        my_counter1[i] = 1
print(my_counter1)
print("\n")

# namedTuple returns a tuple subclass
Point = namedtuple('Point', 'x, y')  # this will create a class named Point with the fields x and y.
# We can add more fields with ,
pt = Point(2, -1)
print(pt)  # we can see a Point, x = 2, y = -1
print(pt.x, pt.y)
print(pt.x * pt.y)


# namedTuple 2
class Point1(namedtuple('Point1', 'x, y')):
    def multiply(self):
        return self.x * self.y

    def __str__(self):
        return 'Point1 : x = {}, y = {}, multiply = {}'.format(self.x, self.y, self.multiply())


for p in Point1(3, 25), Point1(7, 2):
    print(p)

#  making direct assignments
a = Point1.x.__doc__ = 15
b = Point1.y.__doc__ = 3
print(a * b)
print("\n")

#  OrderedDict same as dictionaries but they order the items.
ordered_dict = OrderedDict()
for i in range(6):
    ordered_dict[i] = i * 5
print(ordered_dict)
#  we can popitem as well. If Last = True, then LIFO returns. If false, FIFO returns
print(ordered_dict.popitem(last=True))
print(ordered_dict.popitem(last=False))
print(ordered_dict)
#  with this method, we can move a key and its pair to end. If last = False, then move it to the beginning
ordered_dict.move_to_end(1)
print(ordered_dict)
ordered_dict.move_to_end(1, last=False)
print(ordered_dict)

ordered_dict1 = {}
for i in range(6):
    ordered_dict1[i] = i * 5
print(ordered_dict1)
#  we cannot use this. Because popitem in dict has no arguments!
"""print(ordered_dict1.popitem(last=True))
print(ordered_dict1.popitem(last=False))"""
#  also we cannot use these ones neither. dict has no method called move_to_end
"""ordered_dict1.move_to_end(1)
ordered_dict1.move_to_end(1, last=False)"""
print("\n")
#  defaultDict similar to dicts. only difference is it has a default value if the key has not been set yet
d = defaultdict(int)  # we give default type like int
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
"""  d['e'] = 'e' we cannot do this. because we set default type as int. so we have to give int values
  if we print a key that does not exists, it will print a default type of integers (0)
  for float-(0.0), list([])
  if we do the same in dicts, it will return an error called KeyError"""
print(d['a'], "---", d['f'])
print("\n")
# deque
d = deque()
[d.append(i) for i in range(4)]  # we can append like lists
print(d)
d.appendleft(5)  # this will append elements at the left side.
print(d)
#  we can also remove elements from both sides
d.pop()
print(d)
d.popleft()
print(d)
# also we can extend both sides
d.extend([4, 5, 6])
print(d)
d.extendleft([-3, -2, -1])
print(d)
# we can also rotate
d.rotate(1)  # rotate all elements one place to the right side
print(d)
# to rotate to the negative side
d.rotate(-1)
print(d)
