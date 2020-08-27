import numpy as np
import matplotlib.pyplot as plt
from casadi import *
from casadi.tools import *
import pdb
import sys
import time
sys.path.append('../../')
import do_mpc
from model import template_model
from mpc import template_mpc
from simulator import template_simulator

"""
Setup graphic:
"""

def template_plot_setup(mpc_plot):

    color = plt.rcParams['axes.prop_cycle'].by_key()['color']

    fig, ax = plt.subplots(4,1, sharex=True, figsize=(6, 9))

    ax[0].set_title('Title:')
    mpc_plot.add_line('_x', 'var1', ax[0], color=color[0], linestyle='-', alpha=0.5)
    ax[0].axhline(0.0,linestyle = 'dotted')
    ax[0].set_ylabel('y-Axis Label')
