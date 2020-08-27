import numpy as np
from casadi import *
from casadi.tools import *
import pdb
import sys
sys.path.append('../../')
import do_mpc


def template_mpc(model):
    """
    --------------------------------------------------------------------------
    template_mpc: tuning parameters
    --------------------------------------------------------------------------
    """
    mpc = do_mpc.controller.MPC(model)

    setup_mpc = {
        'n_robust': 0,
        'n_horizon': 30,
        't_step': .3,
        'store_full_solution': True,
        # Use MA27 linear solver in ipopt for faster calculations:
        #'nlpsol_opts': {'ipopt.linear_solver': 'MA27'}
    }
    mpc.set_param(**setup_mpc)

    var1 = model.x['var1']

    # define cost function variables

    # define weights

    lterm = var1**2 # lagrange term
    mterm = var1**2 # meyer term


    mpc.set_objective(mterm=mterm, lterm=lterm)

    # penalty for changes in input between steps
    mpc.set_rterm(a=1e-2)
    mpc.set_rterm(phi=1e-2)

    # define inputs
    input = model.u['input']

    # define bounds on states or inputs
    mpc.bounds['lower','_u','input'] = 10

    mpc.setup()

    return mpc
