# 1 function to add 3 numbers
def add(x, y, z):
    print(x + y + z)


"""or we just use something like that if we do not know how many parameters that will be given

we do not have to give the parameter's name as args!
fe
 def add1(*num):
     print(sum(num))"""


def add1(*args):
    print(sum(args))


add(3, 4, 5)
add1(3, 4, 5)

"""if we try to give 5 parameters to add function, we recieve an error
but if we try the same to add1:
add(3, 4, 5, 6, 7)#TypeError: add() takes 3 positional arguments but 5 were given"""
add1(3, 4, 5, 6, 7, 8)


# args is for numeric parameters

# using kwargs, it's for keyword arguments dictionary!

def add_str(**data):
    for key, value in zip(data, data.values()):
        print("{} is capital city of {}".format(key, value))


add_str(Warsaw='Poland', Ankara='Turkey', Vienna='Austria', Madrid='Spain', Berlin='Germany')
