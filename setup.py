import numpy as np
import pandas as pd
import os

class irreversible(Exception):
    """
    Pop up
    """

def calc_coef(arr_x, arr_y):
    XX = np.matmul(arr_x.T, arr_x)
    if np.linalg.det(XX) == 0:
        raise irreversible('Matrix Irreversible')
    else:
        inv_XX = np.linalg.inv(XX)
        temp = np.matmul(inv_XX, arr_x.T)
        arr_coef = np.matmul(temp, arr_y)
        return arr_coef






