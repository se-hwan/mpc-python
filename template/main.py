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
from model import template_model
from mpc import template_mpc
from simulator import template_simulator

model = template_model()
mpc = template_mpc(model)
simulator = template_simulator(model)


"""
Set initial state
"""
x0 = np.array([0,0,0,0])
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


"""
Run MPC main loop:
"""


for k in range(200):
    u0 = mpc.make_step(x0)
    x0 = simulator.make_step(u0)


    if show_animation:
        mpc_plot.plot_results()
        mpc_plot.plot_predictions()
        sim_plot.plot_results()
        mpc_plot.reset_axes()
        sim_plot.reset_axes()

        #animation code here

input('Press enter to exit.')
