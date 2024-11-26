import sympy as sp
import matplotlib.pyplot as plt
from tabulate import tabulate

y0 = 1
x0 = 0
xn = 1
h = 0.1


def runge_kutta_2(x0, xn, y0, h):  # метод Рунге-Кутти 2-го порядку
    x = x0
    y = y0
    yD = [(x, y)]
    while x < xn:
        k1 = h * f(x, y)
        k2 = h * f(x + h, y + k1)
        y += h * (k1 + k2) / 2
        x += h
        yD.append((round(x, 2), round(y, 5)))
    return yD


def runge_kutta_4(x0, xn, y0, h):
    x = x0
    y = y0
    yD = [(x, y)]
    while x < xn:
        k1 = h * f(x, y)
        k2 = h * f(x + h / 2, y + k1 / 2)
        k3 = h * f(x + h / 2, y + k2 / 2)
        k4 = h * f(x + h, y + k3)
        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x += h
        yD.append((round(x, 2), round(y, 5)))
    return yD


def f(x, y):
    yD = 2 * x * sp.exp(x**2 - y)  # диференціальне рівняння
    return yD


rk2_result = runge_kutta_2(x0, xn, y0, h)
print(rk2_result)
rk4_result = runge_kutta_4(x0, xn, y0, h)
print(rk4_result)


def find_partial_solution(x, y):  # частинний аналітичний розв'язок
    x, y, C = sp.symbols("x y C")
    general_equation = sp.ln(sp.exp(x**2) + C)
    C_value = sp.exp(y0) - sp.exp(x0**2)
    partial_solution = general_equation.subs(C, C_value)
    return partial_solution


def check_general():
    x, y, C = sp.symbols("x y C")
    general_equation = find_partial_solution(x, y)
    derivative_general = sp.diff(general_equation, x)
    print(derivative_general)
    return derivative_general


answer = check_general()
partial = find_partial_solution(x0, y0)
print(f"Частинний розв'язок: {partial}")


def analytical_solution(x_value, y0):
    x, y, C = sp.symbols("x y C")
    C = sp.exp(y0) - sp.exp(x0**2)
    general_equation = sp.ln(sp.exp(x**2) + C)
    return float(general_equation.subs(x, x_value))


# для таблиць
table_data_2 = []
x = x0
while x <= xn:
    rk2_value = [item[1] for item in rk2_result if item[0] == round(x, 2)][0]
    analytical_value = analytical_solution(x, y0)
    table_data_2.append([round(x, 2), round(analytical_value, 3), rk2_value])
    x += h

headers_rk2 = [
    "x",
    "Аналітичний розв'язок",
    "Наближений розв'язок (Рунге-Кутта 2-го порядку)",
]
print(tabulate(table_data_2, headers=headers_rk2, tablefmt="grid"))

table_data_4 = []
x = x0
while x <= xn:
    rk4_value = [item[1] for item in rk4_result if item[0] == round(x, 2)][0]
    analytical_value = analytical_solution(x, y0)
    table_data_4.append([round(x, 2), round(analytical_value, 3), rk4_value])
    x += h

headers_rk4 = [
    "x",
    "Аналітичний розв'язок",
    "Наближений розв'язок (Рунге-Кутта 4-го порядку)",
]
print(tabulate(table_data_4, headers=headers_rk4, tablefmt="grid"))


h_values = [0.1, 0.05, 0.025, 0.01]
new_table_data_2 = []
new_table_data_4 = []

for h in h_values:
    rk2_result = runge_kutta_2(x0, xn, y0, h)
    rk4_result = runge_kutta_4(x0, xn, y0, h)
    rk2_value = rk2_result[-1][1]  # наближене значення у точці xn
    rk4_value = rk4_result[-1][1]
    analytical_value = analytical_solution(xn, y0)
    actual_error_2 = abs(analytical_value - rk2_value)
    actual_error_4 = abs(analytical_value - rk4_value)
    new_table_data_2.append(
        [
            h,
            round(analytical_value, 3),
            round(rk2_value, 3),
            round(actual_error_2, 6),
        ]
    )
    new_table_data_4.append(
        [
            h,
            round(analytical_value, 3),
            round(rk4_value, 3),
            round(actual_error_4, 6),
        ]
    )

headers_rk2 = [
    "h",
    "Аналітичний розв'язок",
    "Наближений розв'язок (Рунге-Кутта 2-го порядку)",
    "Похибка (Рунге-Кутта 2-го порядку)",
]

headers_rk4 = [
    "h",
    "Аналітичний розв'язок",
    "Наближений розв'язок (Рунге-Кутта 4-го порядку)",
    "Похибка (Рунге-Кутта 4-го порядку)",
]

print("Таблиця для Рунге-Кутта 2-го порядку:")
print(tabulate(new_table_data_2, headers=headers_rk2, tablefmt="grid"))

print("\nТаблиця для Рунге-Кутта 4-го порядку:")
print(tabulate(new_table_data_4, headers=headers_rk4, tablefmt="grid"))


# для графіка
def theoretical_error_2(h):
    return h**2


def theoretical_error_4(h):
    return h**4


h_values = [0.05, 0.1, 0.5]
actual_errors_rk2 = []
theoretical_errors_rk2 = []
actual_errors_rk4 = []
theoretical_errors_rk4 = []

for h in h_values:
    rk2_result = runge_kutta_2(x0, xn, y0, h)
    rk4_result = runge_kutta_4(x0, xn, y0, h)

    analytical_result = analytical_solution(xn, y0)

    actual_error_rk2 = abs(analytical_result - rk2_result[-1][1])
    actual_error_rk4 = abs(analytical_result - rk4_result[-1][1])

    actual_errors_rk2.append(actual_error_rk2)
    actual_errors_rk4.append(actual_error_rk4)

    theoretical_errors_rk2.append(theoretical_error_2(h))
    theoretical_errors_rk4.append(theoretical_error_4(h))


plt.plot(
    h_values,
    actual_errors_rk2,
    label="Фактична похибка (Рунге-Кутта 2-го порядку)",
    marker="o",
)
plt.plot(
    h_values,
    theoretical_errors_rk2,
    label="Теоретична похибка (Рунге-Кутта 2-го порядку)",
    marker="x",
)
plt.plot(
    h_values,
    actual_errors_rk4,
    label="Фактична похибка (Рунге-Кутта 4-го порядку)",
    marker="s",
)
plt.plot(
    h_values,
    theoretical_errors_rk4,
    label="Теоретична похибка (Рунге-Кутта 4-го порядку)",
    marker="^",
)
plt.xlabel("Крок h")
plt.ylabel("Похибка")
plt.title("Залежність похибки від кроку h")
plt.legend()
plt.grid()
plt.show()
