import numpy as np
import matplotlib.pyplot as plt
from casadi import *
from casadi.tools import *
import pdb
import sys
import time
sys.path.append('../../')
import do_mpc
from celluloid import Camera

""" User settings: """
show_animation = True
store_results = False

"""
Get configured do-mpc modules:
"""
from plots import *
from model import bicycle_model
from mpc import bicycle_mpc
from simulator import bicycle_simulator

model = bicycle_model()
mpc = bicycle_mpc(model)
simulator = bicycle_simulator(model)


"""
Set initial state
"""
# Parameters:
l_r = 2.25 # distance to rear wheels from CoM
l_f = 2.25 # distance to front wheels from CoM

x0 = 0 # initial x position
y0 = -10 # initial y position
psi0 = np.pi/3 # initial angle offset from horizontal
v0 = 1 # initial velocity
beta0 = 0 # velocity angle offset from bicycle
a0 = 0# initial acceleration

x0 = np.array([x0,y0,psi0,v0,beta0,
    v0*np.cos(psi0+beta0),v0*np.sin(psi0+beta0),
    v0*np.sin(beta0)/l_r,a0])

# in order:
# x, y, psi, v, beta, x_dot, y_dot, psi_dot, v_dot


mpc.x0 = x0
simulator.x0 = x0

# Set initial guess for MHE/MPC based on initial state.
mpc.set_initial_guess()

data = do_mpc.graphics.Graphics(mpc.data)
mpc_plot = do_mpc.graphics.Graphics(mpc.data)
sim_plot = do_mpc.graphics.Graphics(simulator.data)

plot_setup_mpc(mpc_plot)
plot_setup_sim(sim_plot)
plot_setup_data(data)

fig4, ax4 = plt.subplots(1,1, sharex=True, figsize=(6, 5))

"""
Run MPC main loop:
"""


for k in range(200):
    u0 = mpc.make_step(x0)
    x0 = simulator.make_step(u0)
    plt.close(3)
    #plt.close(4)
    #plt.close(2)
    #plt.close(5)

    if show_animation:
        mpc_plot.plot_results()
        mpc_plot.plot_predictions()
        sim_plot.plot_results()
        mpc_plot.reset_axes()
        sim_plot.reset_axes()
        data.plot_results()
        xPosn = data.result_lines['_x','x'][0].get_ydata()
        yPosn = data.result_lines['_x','y'][0].get_ydata()

        ax4.plot(xPosn,yPosn,color='red')
        ax4.set_xlabel('X Position [m]')
        ax4.set_ylabel('Y Position [m]')
        plt.pause(0.01)

#animation = camera.animate()
#animation.save('mpc.gif', writer = 'imagemagick')
input('Press enter to exit.')
