# -*- coding: utf-8 -*-
"""Secant.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/185I_NTuNGA5jAjfZw7GYRW1UIzktTL5V
"""

from sympy.abc import x
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor
import pandas as pd
from IPython.display import display, HTML
import numpy as np

def get_x_b(_x_a, _x_b, _f_x_a, _f_x_b):
#     print(f'_x_a: {_x_a}')
#     print(f'_x_b: {_x_b}')
#     print(f'_f_x_a: {_f_x_a}')
#     print(f'_f_x_b: {_f_x_b}')
    numerator = _f_x_b*(_x_a-_x_b)
    denominator = _f_x_a - _f_x_b
    return _x_b - (numerator/denominator)
    
    
def get_error(_f_x_b, _f_x_a):
    return abs(((_f_x_b - _f_x_a) / _f_x_b)) * 100

# 
#     print(f'f_x_b {f_x_b}')
#     print(f'f_x_a {f_x_a}')
#     print(f'x_b_minus_x_a {x_b_minus_x_a}' )
#     print(f'f_x_a_minus_f_x_b {f_x_a_minus_f_x_b}')

def secant(eq, xa, xb, crit):
    transformations = (standard_transformations +(implicit_multiplication_application,)+(convert_xor,) )
    # Insert value for the equation
    equation = parse_expr(eq, transformations=transformations)

    # Insert initial x_a value
    x_a = xa
    x_b = xb

    # Insert value for stopping criterion
    stopping_criterion = crit

    # Instantiate dataframe
    df = pd.DataFrame(columns=['iteration','x_a','x_b','f_x_a','f_x_b', 'error'])
    # Iteration index
    iteration = int(0)
    error = 100
    f_x_a = equation.subs(x, x_a)
    f_x_b = equation.subs(x, x_b)

    arr = [iteration, x_a, x_b, f_x_a, f_x_b, error]
    # print(arr)
    df= df.append(dict(zip(df.columns, arr)), ignore_index=True)
    iteration+=1

    while error >= (stopping_criterion):
        error = get_error(x_b, x_a)
        x_b_temp = x_b

        x_b = get_x_b(x_a, x_b,f_x_a, f_x_b)
        x_a = x_b_temp
        f_x_a = equation.subs(x, x_a)
        f_x_b = equation.subs(x, x_b)
        arr = [iteration, x_a, x_b,f_x_a, f_x_b, error]

        df= df.append(dict(zip(df.columns, arr)), ignore_index=True)
        iteration+=1

    return (df.to_html())

