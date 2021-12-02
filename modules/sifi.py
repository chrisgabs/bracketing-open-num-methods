import sympy
from sympy.abc import x
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor
import pandas as pd

def get_error(curr_f_x, prev_f_x):
    return abs(((curr_f_x - prev_f_x) / curr_f_x)) * 100

def sifi(eq,fx, crit):
    transformations = (standard_transformations + (implicit_multiplication_application,) + (convert_xor,))
    # Insert values for rearranged formula
    # e.g. f(x) = 2 sin(sqrt(x) - x = 0 ->
    #    2 * sympy.sin(sympy.sqrt(x))
    # equation = 2 * sympy.sin(sympy.sqrt(x))
    equation = parse_expr(eq, transformations=transformations)
    # Insert initial f_x value
    f_x = fx
    # Insert value for stopping criterion
    stopping_criterion = crit

    # Instantiate dataframe
    df = pd.DataFrame(columns=['iteration', 'f_x', 'error'])
    # Iteration index
    iteration = int(0)
    error = 100

    arr = [iteration, f_x, error]
    df = df.append(dict(zip(df.columns, arr)), ignore_index=True)
    iteration += 1

    while error >= float(stopping_criterion):
        f_x = equation.subs(x, f_x)
        error = get_error(f_x, df.at[iteration - 1, 'f_x'])
        arr = [iteration, f_x, error]
        df = df.append(dict(zip(df.columns, arr)), ignore_index=True)
        iteration += 1

    return (df.to_html())