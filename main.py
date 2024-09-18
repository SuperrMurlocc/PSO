from pso import ParticleSwarmOptimization
import functions

X_RANGE = (-5, 5)
Y_RANGE = (-5, 5)


def f(x, y):
    return (1.5 - x - x*y) ** 2 + (2.25 - x + x*y**2) ** 2 + (2.625 - x + x*y**3) ** 2


def main():
    for function in [f, functions.ackley, functions.rosenbrock, functions.rastrigin, functions.himmelblau, functions.mccormick, functions.three_hump_camel]:
        PSO = ParticleSwarmOptimization(function, x_range=X_RANGE, y_range=Y_RANGE)
        PSO.solve(show=True, save=False)


if __name__ == '__main__':
    main()