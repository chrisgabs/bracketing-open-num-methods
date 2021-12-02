from sympy.abc import x
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor
import pandas as pd

def get_xr(xl, xu, f_xl, f_xu):
    numerator = f_xu*(xl-xu)
    denominator = f_xl-f_xu
    temp = float(numerator)/denominator
    return xu - temp

def get_error(curr_xr, prev_xr):
    return ((curr_xr - prev_xr) / curr_xr) * 100


def false_position(eq, lower, upper, crit):
    transformations = (standard_transformations +(implicit_multiplication_application,)+(convert_xor,) )
    # Insert value for the equation
    equation = parse_expr(eq, transformations=transformations)
    # Insert value for xl
    xl = lower
    # Insert value for xu
    xu = upper
    # Insert value for stopping criterion
    stopping_criterion = crit

    # Instantiate dataframe
    df = pd.DataFrame(columns=['iteration', 'xl', 'xu', 'f_xl', 'f_xu', 'xr', 'f_xr', 'error'])
    # Iteration index
    iteration = 1
    f_xl = equation.subs(x, xl)
    f_xu = equation.subs(x, xu)
    xr = get_xr(xl, xu, f_xl, f_xu)

    f_xr = equation.subs(x, xr)

    error = 100
    arr = [iteration, xl, xu, f_xl, f_xu, xr, f_xr, error]
    df = df.append(dict(zip(df.columns, arr)), ignore_index=True)
    iteration += 1
    while error >= float(stopping_criterion):
        if f_xr < 0:
            xl = xl
            xu = xr
        else:
            xl = xr
            xu = xu

        f_xl = equation.subs(x, xl)
        f_xu = equation.subs(x, xu)
        xr = get_xr(xl, xu, f_xl, f_xu)
        f_xr = equation.subs(x, xr)

        # get xr from previous iteration
        error = abs(get_error(xr, df.at[iteration - 2, 'xr']))
        arr = [iteration, xl, xu, f_xl, f_xu, xr, f_xr, error]
        df = df.append(dict(zip(df.columns, arr)), ignore_index=True)
        iteration += 1

    return (df.to_html())