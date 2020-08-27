# Description
Details of the kinematic equations used for this MPC implementation can be found here: https://borrelli.me.berkeley.edu/pdfpub/IV_KinematicMPC_jason.pdf

We want to be able to guide the center of mass of the car to a desired trajectory. For this example, we'll consider the following:
- From some initial speed, acceleration, and angle, we want to be able to follow a lane
- We'll define the distance from the desired trajectory as <img src="https://latex.codecogs.com/gif.latex?\hat{y}" />
- We'll also assume some arbitrary desired speed (could be from speed limits, safety concerns, etc.)
- Control inputs are the steeing angle, <img src="https://latex.codecogs.com/gif.latex?\phi"/>, and the acceleration, <img src="https://latex.codecogs.com/gif.latex?a" />

# Model considerations
Given the simplified model of the car, as well as ignoring the dynamic effects of friction and drag, limitations of the model should be acknowledged:
-
