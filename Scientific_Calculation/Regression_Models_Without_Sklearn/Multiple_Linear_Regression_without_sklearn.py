import pandas as pd
import numpy as np

my_data = pd.read_csv('veriler.csv')
X1 = my_data.iloc[:, 1].values.reshape(-1, 1)
X2 = my_data.iloc[:, 2].values.reshape(-1, 1)
X3 = my_data.iloc[:, 3].values.reshape(-1, 1)
Y1 = my_data.iloc[:, -1].values
Y = []
[Y.append(1) if i == 'e' else Y.append(0) for i in Y1]
Y = np.array(Y).reshape(-1, 1)


# sum of all x values. return sum of X1, sum of X2... sum of Xn
def sums_x(*args):
    x_arrs = []

    [x_arrs.append(sum(i)[0]) for i in args]

    return x_arrs


# Sum of xi * yi's
def x_mul_y(*args):
    x_y_arrs = []
    for j in args:
        sum1 = 0
        for i in range(len(Y)):
            sum1 += (j[i] * Y[i])[0]
        x_y_arrs.append(sum1)
    return x_y_arrs


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


# finding all the coefficients
def coeffs(*args):
    coeff_x = [[]]

    x_sums = sums_x(*args)
    x_y = x_mul_y(*args)
    [coeff_x[0].append(i) for i in x_sums]

    coeff_x[0].insert(0, len(args[0]))
    coeff_x[0].append(sum(Y)[0])

    for i in range(len(x_sums)):
        coeff_x.append([])
        coeff_x[i + 1].append(x_sums[i])
        for j in range(len(x_sums)):
            sum1 = 0
            for k in range(len(args[0])):
                sum1 += int(args[i][k] * args[j][k])
            coeff_x[i + 1].append(sum1)
        coeff_x[i + 1].append(x_y[i])
    return gauss(coeff_x)


# printing the equation. a0 is intercept. other ones are coefficients of x1, x2, ..., xn
def equation(*args):
    coeff = coeffs(*args)
    return [print(f'a{i} = {coeff[i]}') if i == 0 else print(f'a{i} = {coeff[i]} * x') for i in range(len(coeff))]


equation(X1, X2, X3)


# this is for predict. given x values to predict. returns predicted y
def predict(*args):
    coeff = coeffs(X1, X2, X3)
    y = 0
    for i in range(len(coeff)):
        if i == 0:
            y += coeff[i]
        else:
            y += coeff[i] * args[i - 1]
    return y


print(predict(177, 60, 22))
