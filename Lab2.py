import math

y0 = 1
x0 = 0
xn = 1
h = 0.2

def runge_kutta(x0, xn, y0, h):
    x = x0
    y = y0
    yD = [(x, y)]
    while x < xn:
        k1 = h * f(x, y)
        k2 = h * f(x + h, y + k1)
        y += h * (k1 + k2)
        x += h
        yD.append(x, y)
    return yD


def f(x, y):
    yD = 2 * x * math.exp(x**2 - y)
    return yD
