import numpy as np
from casadi import *
from casadi.tools import *
import pdb
import sys
sys.path.append('../../')
import do_mpc


def template_model():
    """
    --------------------------------------------------------------------------
    Variables / RHS / AUX
    --------------------------------------------------------------------------
    """
    model_type = 'continuous' # either 'discrete' or 'continuous'
    model = do_mpc.model.Model(model_type)

    # Model variables:
    var1 = model.set_variable(var_type='_x', var_name='var1')
    var2 = model.set_variable(var_type='_x', var_name='var2')

    state = vertcat(var1,var2)
    state_dot = model.set_variable(var_type='_x', var_name='state_dot', shape=(2.1))

    input1 = model.set_variable(var_type='_u', var_name='input1')


    # Parameters:
    # define Parameters

    model.set_rhs('var1',state_dot[0])
    model.set_rhs('var2',state_dot[1])

    state_dot_rhs = vertcat(
        # rhs1,
        # rhs2)
    model.set_rhs('state_dot',state_dot_rhs)

    model.setup()

    return model
