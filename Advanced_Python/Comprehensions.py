from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#1
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

#1 w comprehensions
my_list = [n for n in nums]
print(my_list)

#1 w reduce. reduce taken a list and a func that has 2 parameters and returns, for this example, multiply of all number that is in list.
#let's say, our list is [1, 2, 3, 4]. it multiplies 1 and 2 and makes it parameter for the same func, then it multiplies (1*2) and 3 and again makes it parameter
#finally it multiplies ((1*2)*3) and 4 and prints it. It's like fact
my_list = reduce(lambda x, y: x*y, [1, 2, 3, 4])
print(my_list)


#2
my_list = []
for n in nums:
    my_list.append(n*n)
print(my_list)

#2 w map, lambda. map is the same with comprehensions. but if it takes a func that return True or False, unlike filter, it returns True or False for each parameters
my_list = map(lambda n: n*n, nums)
print(list(my_list))

#2 w comprehensions
my_list = [n*n for n in nums]
print(my_list)

#3
my_list = []
for n in nums:
    if n % 2 == 0:
        my_list.append(n)
print(my_list)

#3 w comprehensions
my_list = [n for n in nums if n % 2 == 0]
print(my_list)

#3 w filter, filter taken a func that given True or False. and returns a list of True ones.
my_list = filter(lambda n: n%2 == 0, nums)
print(list(my_list))

#4
my_list = []
for letter in 'abcd':
    for n in range(4):
        my_list.append((letter, n))
print(my_list)

#4 w comprehensions
my_list = [(letter, n) for letter in 'abcd' for n in range(4)]
print(my_list)

#5
name = ['bruce', 'clark', 'peter', 'logan']
hero = ['batman', 'superman', 'spiderman', 'wolverine']

my_dict = {}
for letter, letter1 in zip(name, hero):
    my_dict[letter] = letter1
print(my_dict)

#5 w comprehensions dict

my_dict = {letter: letter1 for letter, letter1 in zip(name, hero)}
print(my_dict)

#another example. we can use conditions
my_dict = {letter: letter1 for letter, letter1 in zip(name, hero) if letter != 'peter' and letter1 != 'wolverine'}
print(my_dict)

#6
#set is like lists but has all unique values
nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)

#6 w comprehensions

my_set = {n for n in nums}
print(my_set)

#Generator expressions using yield. it's similar to list comprehensions
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#it's like our other example
def gen(nums):
    for n in nums:
        yield n*n

my_gen = gen(nums)

for i in my_gen:
    print(i, end=' ')
#or
#print(list(my_gen))

#7 w comprehensions. instead of [] and {},  we use () for generator expressions

my_gen = (n*n for n in nums)
print("\n", list(my_gen))