# to add module path to sys
# import sys
# sys.path.append(r"PATHTOMODULE")

import mod
from mod import math

print(mod.wel)
print(mod.wel1)


def operations():
    global sum1
    i = 0
    while True:
        if i == 0:
            num1 = int(input("Write a number: "))
            sum1 = math(num1)
            temp = input("Select -, +, *, /, =, abs, sqrt, ** : ")
            while temp != "+" and temp != "-" and temp != "*" and temp != "/" and temp != "=" and temp != "abs" and temp != "sqrt" and temp != "**":
                print("Please try again")
                temp = input("Select -, +, *, /, =, abs, sqrt, ** : ")
            if temp == "=":
                break
            if temp == "abs" or temp == "sqrt" or temp == "**":
                others(temp, sum1)
                return
            num1 = int(input("Write a number: "))
            if temp == "+":
                obj1 = math(num1)
                sum1 = math(obj1 + sum1)
            elif temp == "-":
                obj1 = math(num1)
                sum1 = math(sum1 - obj1)
            elif temp == "*":
                obj1 = math(num1)
                sum1 = math(sum1 * obj1)
            elif temp == "/":
                obj1 = math(num1)
                sum1 = math(sum1 / obj1)
            i += 2
            continue
        temp = input("Select -, +, *, /, =, abs, sqrt, ** : ")
        while temp != "+" and temp != "-" and temp != "*" and temp != "/" and temp != "=" and temp != "abs" and temp != "sqrt" and temp != "**":
            print("Please try again")
            temp = input("Select -, +, *, /, =, abs, sqrt, ** : ")
        if temp == "=":
            break
        if temp == "abs" or temp == "sqrt" or temp == "**":
            others(temp, sum1)
            return
        num1 = int(input("Write a number: "))
        if temp == "+":
            obj1 = math(num1)
            sum1 = math(obj1 + sum1)
        elif temp == "-":
            obj1 = math(num1)
            sum1 = math(sum1 - obj1)
        elif temp == "*":
            obj1 = math(num1)
            sum1 = math(sum1 * obj1)
        elif temp == "/":
            obj1 = math(num1)
            sum1 = math(sum1 / obj1)
        i += 1
    print(sum1)


def others(temp, num1):
    if temp == 'abs':
        print(num1.__abs__())
        return
    elif temp == '**':
        num2 = int(input("Write a pow: "))
        print(math(num1 ** math(num2)))
        return
    elif temp == 'sqrt':
        print(num1.__sqrt__())
        return


# if we use __name__ == '__main__, we can run these all in terminal! otherwise it will do nothing
if __name__ == '__main__':
    operations()
    # print(dir()) will give:
"""['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
 '__package__', '__spec__', 'math', 'mod', 'operations', 'others', 'sum1']"""
