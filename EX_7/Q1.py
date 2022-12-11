import numpy as np
import cvxpy as cp
import random
import matplotlib.pyplot as plt

t2 = -1
check_numpy = {}
check_cvxpy = {}
def my_timer(orig_func):
    import time
    def wrapper(*args, **kwargs):
        global t2
        t2=0
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{ orig_func.__name__} ran in: {t2} sec')
        return result
    return wrapper

@my_timer
def numpy_solve(A,B):
    return np.linalg.solve(A, B)

@my_timer
def cvxpy_solve(x,objective,constraints):
    prob = cp.Problem(objective, constraints)
    prob.solve()
    return x.value

def solve_random_linear_equation(i):
    global t2
    global check_numpy
    global check_cvxpy
    print(f"make_linear_equation {i} ")
    m =n = i
    A = np.random.randint(1, 10, (m, n))
    B = np.random.randint(1, 10, m)
    print(f"Matrix A {m}x{n} is: \n {A} \n, Matrix B is : \n {B} \n")
    ans_np = numpy_solve(A,B)
    print("numpy solution : ",ans_np)
    check_numpy[m]=t2
    print()
    x = cp.Variable(n)
    constraints = [A @ x == B]
    objective = cp.Minimize(cp.sum(A @ x - B))
    ans_cvxpy = cvxpy_solve(x,objective,constraints)
    check_cvxpy[m]=t2
    print("cvxpy solution : ",ans_cvxpy)
    print("------------------------------------------------------------------------")


def print_graph():
    global check_cvxpy
    global check_numpy
    plt.plot(check_cvxpy.keys(),check_cvxpy.values(),'-ok',color='red')
    plt.plot(check_numpy.keys(), check_numpy.values(), '-ok', color='blue')
    plt.show()


if __name__ == '__main__':
    # Problem data.
    for i in range(1,50):
        solve_random_linear_equation(i)
    print_graph()