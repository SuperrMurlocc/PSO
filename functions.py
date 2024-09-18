import numpy as np


def rastrigin(x, y):
    A = 10.0
    return A + (x ** 2 - A * np.cos(2 * np.pi * x)) + (y ** 2 - A * np.cos(2 * np.pi * y)) + 10


def ackley(x, y):
    n = 2
    a = 20.0
    b = 0.2
    c = 2 * np.pi

    term1 = -a * np.exp(-b * np.sqrt(1/n * (x**2 + y**2)))
    term2 = -np.exp(1/n * (np.cos(c * x) + np.cos(c * y)))

    return term1 + term2 + a + np.exp(1)


def rosenbrock(x, y):
    return (1-x)**2 + 100*(y-x**2)**2


def himmelblau(x, y):
    return (x ** 2 + y - 11) ** 2 + (x + y ** 2 - 7) ** 2


def mccormick(x, y):
    return np.sin(x + y) + (x - y)**2 - 1.5 * x + 2.5 * y + 1 + 7


def three_hump_camel(x, y):
    return 2 * x**2 - 1.05 * x**4 + x**6 / 6 + x * y + y**2
