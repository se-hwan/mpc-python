#Description
Motivated by control schemes for the MIT Cheetah, this repository was created to better understand and learn more about model predictive control. Using the ```do-mpc``` package in Python, MPC was used for a number of different kinematic/dynamic models. Currently, MPC has been implemented on the following systems:

- Kinematic bicycle model

#Contents
 - ```models```: Contains subfolders for each model. Model directory will have animated results and plots, along with details for how to modify trajectories and tune parameters.
 - ```template```: Contains template code to implement MPC on new systems.
 - ```LCM [WIP]```: Lightweight communications marshalling (LCM) implementation to visualize results in the Unity engine (not required).
 - ```visualizer [WIP]```: Folder containing Unity assets, resources, and scripts to visualize results from MPC control.
 - ```A Quick Overview of MPC.pdf```: Simplified summary of the key concepts surrounding MPC.


#Dependencies
A ```conda``` environment running Python 3.x is recommended with the following packages

- numpy
- CasADi
- matplotlib

The details for installing do-mpc can be found here: https://www.do-mpc.com/en/latest/installation.html

It is recommended to install the HSL MA27 solver for faster computation, which can be found here: http://www.hsl.rl.ac.uk/ipopt/
