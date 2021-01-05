import numpy as np
import matplotlib.pyplot as plt
from sympy import Symbol
import time

time_start = time.process_time()
my_data = np.genfromtxt('aylaragoresatis.csv', delimiter=',')
X = my_data[1:, 0].reshape(-1, 1)
Y = my_data[1:, 1].reshape(-1, 1)
x = Symbol('x')
y = Symbol('y')


# equation = Y' = a + b(yx) * x
# Y' is predicted y value
# a is regression constant
# b(yx) = regression coefficient of y to x

# sum of all x values and div it len of x array. x'
def sum_x(x):
    sum_x = 0
    for i in x:
        sum_x += i

    return (sum_x / len(x))[0]


# sum of all y values and div it len of y array. y'
def sum_y(y):
    sum_y = 0
    for i in y:
        sum_y += i

    return (sum_y / len(y))[0]


# multiply of all the same index of x and y values
def x_mul_y(x, y):
    return sum([x[i] * y[i] for i in range(len(x))])[0]


# sum of x values's square
def x_square_sum(x):
    return sum([(x[i] ** 2) for i in range(len(x))])[0]


# to find regression coefficient
def reg_coefficient():
    numerator = x_mul_y(X, Y) - (len(Y) * sum_x(X) * sum_y(Y))
    denominator = x_square_sum(X) - (len(X) * (sum_x(X) ** 2))
    reg = numerator / denominator

    return reg


# this is our equation
def equation():
    a = sum_y(Y) - (reg_coefficient() * sum_x(X))
    y = a + (reg_coefficient() * x)
    return y


# to predict. given a month value to predict salary value
def predict(pre):
    return equation().subs({x: pre})


# predicted y values appending to _y array
_y = []
[_y.append(predict(X[i])) for i in range(len(X))]


# equation printed
print("y = ", equation())
print(predict(17))


# to plot
plt.scatter(X, Y)
plt.plot(X, _y)
plt.show()
time_end = time.process_time()
print(time_end - time_start)

