
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor
import pandas as pd
from sympy import Eq, solve, solveset, symbols
x, y= symbols('x y', real=True)
transformations = (standard_transformations +(implicit_multiplication_application,)+(convert_xor,) )


def get_error(_f_x_b, _f_x_a):
    return abs(((_f_x_b - _f_x_a) / _f_x_b)) * 100


# Lecture sample
transformations = (standard_transformations + (implicit_multiplication_application,) + (convert_xor,))


def nonlinear(eq1_equal_side, eq1_expression_side, eq2_equal_side, eq2_expression_side, x0, y0, crit):
    eq1_var = parse_expr(eq1_equal_side, transformations=transformations)
    eq2_var = parse_expr(eq2_equal_side, transformations=transformations)

    eq1_expression = parse_expr(eq1_expression_side, transformations=transformations)
    eq2_expression = parse_expr(eq2_expression_side, transformations=transformations)

    stopping_criterion = crit

    eq1_val = x0
    eq2_val = y0
    f_eq1 = eq1_expression.subs({eq1_var: eq1_val, eq2_var: eq2_val})
    f_eq2 = eq2_expression.subs({eq1_var: eq1_val, eq2_var: eq2_val})
    iteration = int(0)
    error1 = 100
    error2 = 100

    df = pd.DataFrame(columns=['iteration', eq1_var, eq2_var, f'f({eq1_var})', f'f({eq2_var})', f'error({eq1_var})',
                               f'error({eq2_var})'])
    arr = [iteration, eq1_val, eq2_val, f_eq1, f_eq2, error1, error2]
    df = df.append(dict(zip(df.columns, arr)), ignore_index=True)


    print(f'f({eq1_var}): {f_eq1}')
    print(f'f({eq2_var}): {f_eq2}')

    # while error1>= float(stopping_criterion) and error2>=float(stopping_criterion):
    while error1 >= float(stopping_criterion):
        error1 = get_error(f_eq1, eq1_val)
        error2 = get_error(f_eq2, eq2_val)
        eq1_val = f_eq1
        eq2_val = f_eq2
        # print(f'({eq1_var}): {eq1_val}')
        # print(f'({eq2_var}): {eq2_val}')
        # print(f'error({eq1_var}): {error1}')
        # print(f'error({eq2_var}): {error2}')
        # print(f'f({eq1_var}): {f_eq1}')
        # print(f'f({eq2_var}): {f_eq2}')

        f_eq1 = eq1_expression.subs({eq1_var: eq1_val, eq2_var: eq2_val})
        f_eq2 = eq2_expression.subs({eq1_var: eq1_val, eq2_var: eq2_val})

        arr = [iteration, eq1_val, eq2_val, f_eq1, f_eq2, error1, error2]
        print(arr)
        df = df.append(dict(zip(df.columns, arr)), ignore_index=True)

    return(df.to_html())

# nonlinear('y', '-x^2+x+0.75', 'x', '(x^2-y)/(5y)', 1.2, 1.2, 1)



