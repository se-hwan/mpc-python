import numpy as np
import matplotlib.pyplot as plt
from casadi import *
from casadi.tools import *
import pdb
import sys
import time
sys.path.append('../../')
import do_mpc


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
x0 = np.array([0,0,np.pi/50,0,0,0,0,0,0])

mpc.x0 = x0
simulator.x0 = x0

# Set initial guess for MHE/MPC based on initial state.
mpc.set_initial_guess()




data = do_mpc.graphics.Graphics(mpc.data)
mpc_plot = do_mpc.graphics.Graphics(mpc.data)
sim_plot = do_mpc.graphics.Graphics(simulator.data)
plot_setup_mpc(mpc_plot);

"""
Run MPC main loop:
"""


for k in range(300):
    u0 = mpc.make_step(x0)
    x0 = simulator.make_step(u0)

    if show_animation:
        mpc_plot.plot_results()
        mpc_plot.plot_predictions()
        sim_plot.plot_results()
        mpc_plot.reset_axes()
        sim_plot.reset_axes()
        #xPosn = mpc_plot.result_lines['_x','x'][0].get_ydata()
        yPosn = mpc_plot.result_lines['_x','y'][0].get_ydata()
        #ax[4].plot(xPosn,yPosn)
        plt.pause(0.01)
print(len(mpc_plot.result_lines['_x','y']))
print(mpc_plot.result_lines['_x','y'][0].get_ydata())
#print(mpc_plot.result_lines['_x','x'][0].get_ydata())







input('Press enter to exit.')

'''
# Store results:
if store_results:
    do_mpc.data.save_results([mpc, mhe, simulator], 'rot_oscillating_masses')
'''
