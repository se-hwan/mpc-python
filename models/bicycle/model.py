import numpy as np
from casadi import *
from casadi.tools import *
import pdb
import sys
sys.path.append('../../')
import do_mpc


def bicycle_model():
    """
    --------------------------------------------------------------------------
    model: "bicycle model" approximation of 2D car kinematics
    Variables / RHS / AUX
    --------------------------------------------------------------------------
    """
    model_type = 'continuous' # either 'discrete' or 'continuous'
    model = do_mpc.model.Model(model_type)

    # Model variables:
    x = model.set_variable(var_type='_x', var_name='x')
    y = model.set_variable(var_type='_x', var_name='y')
    psi = model.set_variable(var_type='_x', var_name='psi')
    v = model.set_variable(var_type='_x', var_name='v')
    beta = model.set_variable(var_type='_x', var_name='beta') # additional state for beta

    state = vertcat(x,y,psi,v)
    state_dot = model.set_variable(var_type='_x', var_name='state_dot', shape=(4,1))

    phi = model.set_variable(var_type='_u', var_name='phi')
    a = model.set_variable(var_type='_u', var_name='a')


    # Parameters:
    l_r = 2.25 # distance to rear wheels from CoM
    l_f = 2.25 # distance to front wheels from CoM

    model.set_rhs('x',state_dot[0])
    model.set_rhs('y',state_dot[1])
    model.set_rhs('psi',state_dot[2])
    model.set_rhs('v',state_dot[3])

    state_dot_rhs = vertcat(
        v*np.cos(psi+beta),
        v*np.sin(psi+beta),
        v*np.sin(beta)/l_r,
        a)
    model.set_rhs('state_dot',state_dot_rhs)
    model.set_rhs('beta',np.arctan2(l_r*np.tan(phi),(l_f+l_r)))

    model.setup()

    return model
