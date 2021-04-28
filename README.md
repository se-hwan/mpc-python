# Description
Model predictive control algorithms applied to various dynamic systems, developed in Python. Using the ```do-mpc``` and ```casadi``` package in Python. Systems implemented:

- Spaceship
- Kinematic bicycle model

# Contents
 - ```models```: Contains subfolders for each model. Model directory will have a description of the system, animated results and plots, and details for how to modify trajectories and tune parameters.
 - ```template```: Contains template code to implement MPC on new systems with ```do-mpc``` package.
 - ```visualizer [WIP]```: Folder containing Unity assets, resources, and scripts to visualize results from MPC control.

# Dependencies
A ```conda``` environment running Python 3.x is recommended with the following packages

- numpy
- CasADi
- matplotlib

The details for installing do-mpc can be found here: https://www.do-mpc.com/en/latest/installation.html

It is recommended to install the HSL MA27 solver for faster computation, which can be found here: http://www.hsl.rl.ac.uk/ipopt/
