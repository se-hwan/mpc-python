import numpy as np
import matplotlib.pyplot as plt
from casadi import *
from casadi.tools import *
import pdb
import sys
import time
sys.path.append('../../')
import do_mpc
from model import bicycle_model
from mpc import bicycle_mpc
from simulator import bicycle_simulator



def plot_setup_mpc(mpc_plot):
    """
    Setup graphic:
    """
    color = plt.rcParams['axes.prop_cycle'].by_key()['color']

    fig1, ax1 = plt.subplots(4,1, sharex=True, figsize=(9, 9))

    ax1[0].set_title('Position:')
    mpc_plot.add_line('_x', 'y', ax1[0], color=color[0], linestyle='-', alpha=0.5)
    ax1[0].axhline(0.0,linestyle = 'dotted')
    ax1[0].set_ylabel('Y Position [m]')

    ax1[1].set_title('Velocity:')
    mpc_plot.add_line('_x', 'v', ax1[1], color=color[1], linestyle='-', alpha=0.5)
    ax1[1].axhline(15,linestyle = 'dotted')
    ax1[1].set_ylabel('Velocity [m/s]')

    ax1[2].set_title('Input: acceleration')
    mpc_plot.add_line('_u', 'a', ax1[2],color = color[2],linestyle='-')
    ax1[2].set_ylabel('Acceleration [m/s^2]')

    ax1[3].set_title('Input: steering angle')
    mpc_plot.add_line('_u', 'phi', ax1[3],color=color[3],linestyle='-')
    ax1[3].set_ylabel('Steering angle [rad]')

#def plot_setup_sim(sim_plot)
