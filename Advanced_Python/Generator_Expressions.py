import memory_profiler
import time
import random
import sys


# 1 it's returning list

def square(nums):
    result = []
    for i in nums:
        result.append(i * i)
    return result


my_nums = square([1, 2, 3, 4, 5])
print(my_nums)


# 1 w generator. we're not getting list anymore. we're getting generator object. it's beacuse not generators do not hold the entire result in memory
# it yields one result at a time.
def square_gen(nums):
    for i in nums:
        yield i * i


my_nums = square_gen([1, 2, 3, 4, 5])
print(my_nums)

# we can see all the result like this.
"""print(next(my_nums))#we can see the next result. 1 is the first value
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))"""
# print(next(my_nums))#this gives error because it's out of values

# or
# only this will be printed
print(list(
    my_nums))  # we can easily convert them into list. But if we convert them into list, we lose all of the advantages of generator expressions!

for i in my_nums:
    print(i)

"""****it's more readable than a list
note that the generators do not hold the values in memory. This is why if we print them more than one time, only prints it one time.
fe, we run:
----->for i in my_nums:
----->   print(i)
and
----->print(list(my_nums))
it prints the numbers due to for loop but prints an empty list below!
and after that if we run that:
----->print(next(my_nums))
it return a StopIteration error just like above. Cause it's out of values!


****it has a better performance than lists. Because it does not hold the values in memory!

"""

# a good example to compare them

names = ['John', 'Adam', 'Corey', 'Steve', 'Nick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

#print("Memory(Before): {} Mb".format(memory_profiler.memory_usage())

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result


def people_gen(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person


# t1 = time.perf_counter()
# people_list(10000000)
# t2 = time.perf_counter()
#result:
# Memory(Before): [15.63671875] Mb
# Memory(After): [16.22265625] Mb
# Took 13.4018644 Seconds


t1 = time.perf_counter()
people_gen(10000000)
t2 = time.perf_counter()
#result
# Memory(Before): [15.6015625] Mb
# Memory(After): [15.6328125] Mb
# Took 7.499999999993623e-06 Seconds

print(sys.getsizeof(people_gen(10000000)))#56 generator one is 56 bytes.

#print(sys.getsizeof(people_list(10000000)))#and list one is 40764024 bytes.


#print("Memory(After): {} Mb".format(memory_profiler.memory_usage()))
print("Took {} Seconds".format(t2-t1))
#so it works faster than the lists one! and uses lower memory space!
