# Particle Swarm Optimization (PSO) with Various Test Functions

This repository implements Particle Swarm Optimization (PSO), an optimization algorithm inspired by the social behavior of birds flocking or fish schooling. The implementation uses PSO to find the minimum of several well-known mathematical functions commonly used in optimization problems.

## Features

- Custom Functions: The code includes a custom objective function as well as several classic test functions:
  - Ackley
  - Rosenbrock
  - Rastrigin
  - Himmelblau
  - McCormick
  - Three-hump camel
- Particle Swarm Optimization: The PSO algorithm is implemented with customizable parameters, such as inertia weight (w), cognitive (c1), and social (c2) coefficients.
- Visualization: You can visualize the particles’ movement across the solution space with a real-time contour plot animation. This demonstrates how particles converge to the global minimum of the objective function.

## Installation

To run the code, you need the following Python libraries:
- numpy
- matplotlib

Install them using:
```
pip install numpy matplotlib
```

## Usage

To run the PSO algorithm, execute:

```
python main.py
```

This will apply PSO to the selected test functions and display the optimization process as an animation if show=True is set.

## Function Details

Each test function is defined to test the optimization algorithm’s effectiveness. These are classical functions in optimization research. A custom objective function f(x, y) is also provided.

## Videos

You can view the optimization process for each function in the following videos:

- Ackley Function:

https://github.com/user-attachments/assets/e87eabd4-37d4-4a9d-a408-a1adbc7a28b6

- Rosenbrock Function:

https://github.com/user-attachments/assets/17cf2e7f-f180-4f7d-9a10-42fcb71c0013


- Rastrigin Function:

https://github.com/user-attachments/assets/a3162084-9f30-4552-a7a7-50599b2ec78b

- Himmelblau Function:

https://github.com/user-attachments/assets/dc04e124-5bfb-4ab1-8dd9-03a3298b8168

- McCormick Function:

https://github.com/user-attachments/assets/080b0f74-9cee-497d-a03a-37be91deb020

- Three-Hump Camel Function:

https://github.com/user-attachments/assets/f0dd2c38-730a-4116-8fa9-b63c42957dbf

PSO Parameters

You can adjust the PSO parameters in the ParticleSwarmOptimization class:

- `n_epoch`: Number of epochs (iterations).
- `n_particles`: Number of particles.
- `c1`: Cognitive coefficient (influence of personal best).
- `c2`: Social coefficient (influence of global best).
- `w`: Inertia weight (velocity retention across iterations).

License

This project is licensed under the MIT License.
