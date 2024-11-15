from math import cos, sin

import matplotlib.pyplot as plt

points_x = input("Enter the x values  separated by space: ")
points_x_list = [float(value) for value in points_x.split()]
# inter_point = float(input("Enter interpolation point: "))

a = 1
b = 2


def f(x):  # моя функція зі завдання (2га)
    return sin(cos(x))


def InterpolatePolynomialLagrange(x_list, y_list, n):
    def L(x):
        res = 0
        for i in range(n):
            yN = y_list[i]
            term = 1
            for j in range(n):
                if j != i:
                    term *= (x - x_list[j]) / (x_list[i] - x_list[j])
            res += yN * term
        return res

    return L


def LinearInterpolation(x_list, y_list, n):
    def g(x):
        for i in range(n - 1):
            if x >= x_list[i] and x <= x_list[i + 1]:
                return y_list[i] + (x - x_list[i]) * (y_list[i + 1] - y_list[i]) / (
                    x_list[i + 1] - x_list[i]
                )

    return g


def ChooseX(a, b, h):
    last = a
    chosen_x = []
    while last < b:
        chosen_x.append(last)
        last += h
    chosen_x.append(b)
    return chosen_x


def FindY(chosen_x):
    chosen_y = [f(x) for x in chosen_x]
    return chosen_y


n = len(points_x_list)
h = (b - a) / n

chosen_x = ChooseX(a, b, h)
chosen_y = FindY(chosen_x)

interpolated_polynomial = InterpolatePolynomialLagrange(chosen_x, chosen_y, n)
linear_interpolated = LinearInterpolation(chosen_x, chosen_y, n)

x_graph = [a + i * 0.05 for i in range(int((b - a) / 0.05) + 1)]
y_graph = [f(x) for x in x_graph]
L_graph = [interpolated_polynomial(x) for x in x_graph]
g_graph = [linear_interpolated(x) for x in x_graph]
errors = [(f(x) - interpolated_polynomial(x)) for x in x_graph]
max_error = max(errors)

# графік полінома Лагранжа
plt.figure(figsize=(10, 10))
plt.plot(x_graph, y_graph, label="f(x) = sin(cos(x))", color="green")
plt.plot(
    x_graph, L_graph, label="Lagrange Polynomial L(x)", color="red", linestyle="--"
)
plt.plot(x_graph, errors, label="|f(x) - L(x)|", color="blue", linestyle=":")
plt.title(f"Maximum absolute error: {max_error:.5f}")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

# графік лінійної інтерполяції
plt.figure(figsize=(10, 10))
plt.plot(x_graph, y_graph, label="f(x) = sin(cos(x))", color="green")
plt.plot(
    x_graph, g_graph, label="Linear Interpolation g(x)", color="yellow", linestyle="--"
)
plt.title("Linear Interpolation")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
