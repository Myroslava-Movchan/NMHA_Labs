from math import cos, sin

# import matplotlib.pyplot as mplt

pointsX = input("Enter the x values  separated by space: ")
pointsXList = [float(value) for value in pointsX.split()]
interPoint = float(input("Enter interpolation point: "))

a = 1
b = 2


def f(x):  # моя функція зі завдання (2га)
    return sin(cos(x))


def InterpolatePolynomLagrange(xList, yList, n):
    def term_string(i, xList, yList):
        term = f"{yList[i]}"
        for j in range(n):
            if j != i:
                term += f" * (x - {xList[j]}) / ({xList[i]} - {xList[j]})"
        return term

    polynomial = " + ".join(term_string(i, xList, yList) for i in range(n))
    return polynomial


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


n = len(pointsXList)
h = (b - a) / n

chosenX = ChooseX(a, b, h)
chosenY = FindY(chosenX)

#points = list(zip(pointsXList, pointsYList))


interpolatedPolynom = InterpolatePolynomLagrange(chosenX, chosenY, n)
#print(interpolatedPolynom)
