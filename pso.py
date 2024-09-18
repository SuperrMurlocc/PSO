from random import uniform, random
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation as animation
plt.rcParams['font.family'] = 'DeJavu Serif'


class Particle:
    def __init__(self, x, y, *, f, w, boundaries):

        self.w = w
        self.boundaries = boundaries

        self.position = np.array([x, y])
        self.f = f
        self.velocity = np.random.rand(len(self.position))

        self.personal_best = self.position
        self.p_best = self.position

    @property
    def p_best(self):
        return self.personal_best

    @p_best.setter
    def p_best(self, value):
        self.personal_best = value.copy()
        self.fitness_best = self.f(*value)

    @property
    def p_best_fitness(self):
        return self.fitness_best

    def is_in_boundaries(self, position):
        return self.boundaries[0, 0] <= position[0] <= self.boundaries[0, 1] and self.boundaries[1, 0] <= position[1] <= self.boundaries[1, 1]

    def update(self, *, g_best, c1, c2):
        cognitive = c1 * random() * (self.p_best - self.position)
        social = c2 * random() * (g_best - self.position)

        new_position = self.position + self.velocity
        if self.is_in_boundaries(new_position):
            self.position = new_position

            if self.f(*self.position) < self.p_best_fitness:
                self.p_best = self.position

        self.velocity = self.w * self.velocity + cognitive + social


class ParticleSwarmOptimization:
    def __init__(self, function, *, n_epoch: int = 100, n_particles: int = 100, c1: float = .2, c2: float = .2,
                 w: float = .7, x_range: (int, int) = (-5, 5), y_range: (int, int) = (-5, 5)):
        self.n_epoch = n_epoch
        self.function = function
        self.c1 = c1
        self.c2 = c2
        self.boundaries = np.array([x_range, y_range])
        self.particles = [Particle(uniform(*x_range), uniform(*y_range), w=w, f=function, boundaries=self.boundaries) for _ in range(n_particles)]

    def get_g_best(self):
        p_best_fitnesses = [particle.p_best_fitness for particle in self.particles]
        return self.particles[p_best_fitnesses.index(min(p_best_fitnesses))].p_best

    def solve(self, *, show=False, save=False):
        def epoch(n: int = 0):
            g_best = self.get_g_best()
            for particle in self.particles:
                particle.update(c1=self.c1, c2=self.c2, g_best=g_best)
            if show:
                ax.cla()
                ax.set_xlim(self.boundaries[0, 0], self.boundaries[0, 1])
                ax.set_ylim(self.boundaries[1, 0], self.boundaries[1, 1])
                ax.set_xlabel('x')
                ax.set_ylabel('y')
                ax.contourf(X, Y, Z, cmap="viridis", levels=50)
                ax.scatter([p.position[0] for p in self.particles], [p.position[1] for p in self.particles], color='#E46B71', s=4)
                if n != self.n_epoch - 1:
                    ax.set_title(f'Function: {self.function.__name__}\nEpoch: {n + 1}')
                else:
                    ax.set_title(f'Function: {self.function.__name__}\nBest: (x, y) = ({g_best[0]:.3f}, {g_best[1]:.3f}), f(x, y) = {self.function(*g_best):.5f}')

        if not show:
            for _ in range(self.n_epoch):
                epoch()
        else:
            fig, ax = plt.subplots()
            X, Y = np.meshgrild(np.linspace(*self.boundaries[0], 100), np.linspace(*self.boundaries[1], 100))
            Z = np.power(self.function(X, Y), .2)
            ani = animation.FuncAnimation(fig=fig, func=lambda frame: epoch(frame), frames=self.n_epoch, interval=30, repeat=False)
            if save:
                ani.save(f'videos/{self.function.__name__}.mp4', fps=33)
            else:
                plt.show()

        return self.get_g_best()
