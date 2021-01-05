import matplotlib.pyplot as plt
from sympy import Symbol
import pandas as pd

data = pd.read_csv("maaslar.csv")
X = data.iloc[:, 1:2].values
Y = data.iloc[:, -1].values.reshape(-1, 1)
x = Symbol('x')
y = Symbol('y')


# to find sums of x and x exponents.
# for example, for second degree poly, we need to find sum of x^0, x^1, x^2, x^3 and x^4
def sum_x(X, m):
    xs = []
    for i in range(m * 2 + 1):
        sums = 0
        for j in X:
            sums += (j ** i)
        xs.append(sums[0])
    return xs


# to find x mulp y. For example, for second degree poly, we need to find sum of y, x*y, x^2*y
def x_mul_y(X, Y, m):
    x_y = []
    for i in range(m + 1):
        sum1 = 0
        for j in range(len(X)):
            sum1 += (X[j] ** i) * Y[j]
        x_y.append(sum1[0])
    return x_y


# Solution of matrix with gauss elimination
def gauss(A):
    n = len(A)

    for i in range(0, n):
        maxEl = abs(A[i][i])
        maxRow = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > maxEl:
                maxEl = abs(A[k][i])
                maxRow = k

        for k in range(i, n + 1):
            tmp = A[maxRow][k]
            A[maxRow][k] = A[i][k]
            A[i][k] = tmp

        for k in range(i + 1, n):
            c = -A[k][i] / A[i][i]
            for j in range(i, n + 1):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]

    x = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = A[i][n] / A[i][i]
        for k in range(i - 1, -1, -1):
            A[k][n] -= A[k][i] * x[i]
    return x


# to find all coefficients and return its solve
def coeff(m):
    x_sum = sum_x(X, m)
    x_m_y = x_mul_y(X, Y, m)
    coeff = []
    for i in range(m + 1):
        coeff.append([])
        for j in range(i, i + m + 1):
            coeff[i].append(x_sum[j])
        coeff[i].append(x_m_y[i])
    return gauss(coeff)


# it's for equation of polynom
def equation(m):
    coef = coeff(m)
    a = coef[0]
    l = {i: coef[i] * (x ** i) for i in range(1, m + 1)}
    y1 = 0
    for i in l.values():
        y1 += i
    y = a + y1
    return y


# to predict our y value. and we choose degree in here
def predict(pre):
    return equation(5).subs({x: pre})


print('y = ', equation(5))
print(f'predict {6} = {predict(6)}')

_y = []
[_y.append(predict(X[i])) for i in range(len(X))]

plt.scatter(X, Y)
plt.plot(X, _y)
plt.show()