from math import cos, sin

# import matplotlib.pyplot as mplt


def f(x):  # моя функція зі завдання (2га)
    return sin(cos(x))


pointsX = input("Enter the x values  separated by space: ")
pointsY = input("Enter the y values respectively  separated by space: ")
interPoint = float(input("Enter interpolation point: "))

pointsXList = [float(value) for value in pointsX.split()]
pointsYList = [float(value) for value in pointsY.split()]
points = list(zip(pointsXList, pointsYList))

n = len(pointsXList)


def InterpolatePolynomLagrange(xList, yList, n):
    def term_string(i, xList, yList):
        term = f"{yList[i]}"
        for j in range(n):
            if j != i:
                term += f" * (x - {xList[j]}) / ({xList[i]} - {xList[j]})"
        return term

    polynomial = " + ".join(term_string(i, xList, yList) for i in range(n))
    return polynomial


interpolatedPolynom = InterpolatePolynomLagrange(pointsXList, pointsYList, n)

a = 1
b = 2
h = (b - a) / n


def ChooseX(a, b, h):
    last = a
    chosenX = []
    while last < b:
        chosenX.append(last)
        last += h
    chosenX.append(b)
    return chosenX


def FindY(chosenX):
    chosenY = [f(x) for x in chosenX]
    return chosenY
