# Description
Details of the kinematic equations used for this MPC implementation can be found here: https://borrelli.me.berkeley.edu/pdfpub/IV_KinematicMPC_jason.pdf

We want to be able to guide the center of mass of the car to a desired trajectory. For this example, we'll consider the following conditions:
- From some initial speed, acceleration, and angle, we want to be able to follow a lane
- We'll define the distance from the desired trajectory as <img src="https://latex.codecogs.com/gif.latex?\hat{y}" />
- We'll also assume some arbitrary desired speed (could be from speed limits, safety concerns, etc.) to track as opposed to some final goal distance
- Control inputs are the steering angle, <img src="https://latex.codecogs.com/gif.latex?\phi"/>, and the acceleration, <img src="https://latex.codecogs.com/gif.latex?a" />
- Enforce input limits on the acceleration and steering angle

# Model considerations

Given the simplified model of the car, as well as ignoring the dynamic effects of friction and drag, limitations of the model should be acknowledged:
- Steering angle is not instantaneous, but a penalty was assigned to large changes in the steering input between time steps
- Dynamic/inertial effects ignored
- Singularities can exist in zero configurations (should be fixed in future code updates)

# Results
Eventually, the results from the MPC program should be communicated via LCM to visualize a fully 3D model of a car following the calculated position and orientation in Unity.

The animation below tracks the position of the car in space over the first several iterations, starting at an initial angle of <img src="https://latex.codecogs.com/gif.latex?\pi/3"/> from the horizontal and an initial speed of 1 m/s.
![Animation of position](position.gif?raw=true "Title")
The corresponding control inputs and velocity over time is shown below.
![Alt text](control.png?raw=true "Title")

Oscillating behaviour can be seen in the position of the car as it approaches the desired target of 0, and the control inputs oscillate as well. This could be fixed by specifying a target range of position values rather than an exact position, which could be explored in the future.

A variety of trajectories and initial conditions should be tested next to determine how robust the parameters are to new situations, especially the time step between iterations.
