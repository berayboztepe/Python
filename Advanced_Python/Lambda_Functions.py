# They are anonymous functions. They have no name

# 1, w function

def f(x):
    return 3 * x + 1


print(f(7))

# 1, w lambda
f1 = lambda x: 3 * x + 1
print(f1(7))

# 1 in single line
print((lambda x: 3 * x + 1)(7))
# 2, w lambda

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(full_name("twenty", "TWO"))


# we can not use this with multi-line
# 3

def build_quadratic_functions(a, b, c):
    # returns the function f(x) = ax^2 + bx + c
    return lambda x: a * x ** 2 + b * x + c


f2 = build_quadratic_functions(2, 3, -5)
print(f2(3))  # it needs a x value
# or
print(build_quadratic_functions(2, 3, -5)(3))

# 4, using with funcs

print((lambda x, func: x + func(x) + 2)(4, lambda x: x*x))

#lambda function can not contain any statements such as return, pass, assert

#5
print((lambda x: x % 2 and 'odd' or 'even')(22))#if x%2 is False, return odd else return even


#using lambda with **kwargs
print((lambda **kwargs: sum(kwargs.values()))(ten=10, nine=9, three=3))


#using with map
print(list(map((lambda x: x*2), range(11, 12))))

#6
func = []
for i in range(3):
    func.append(lambda i=i: print(22))

for f in func:
    f()


#with sort()
num = ['d1', 'd70', 'd8', 'd2', 'd10', 'd3']
print(sorted(num, key=lambda x: int(x[1:])))#sort the integer numbers in strings

