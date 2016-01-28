import sympy as sy
import numpy as np

<<<<<<< HEAD
def fun_1( my_id ):
=======
def fun_1( y_id ):
>>>>>>> 4327bf8c7fd781d02173958fc0d3e9b0a5ec31a2
    ans = hex(my_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate( (sy.exp(-x)*(sy.sin(x)/x)), (x,0, sy.oo) )
    return ans

def my_solution():
    A = np.array( [[3,1,2,3,1,2,5,1,1,2],[3,2,2,1,4,1,1,1,2,1],[1,2,3,4,3,2,1,2,3,4],[2,2,3,1,4,5,3,1,1,2],[2,3,4,1,2,3,2,4,5,3],[1,4,3,2,3,1,2,1,3,2],[1,3,2,1,2,5,4,3,2,1],[3,1,2,4,1,5,3,2,2,2],[2,1,1,1,4,3,1,3,2,4],[1,1,1,4,2,2,3,4,1,3]] )
    b = np.array([2,6,5,1,3,3,4,9,8,2])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    my_id = 1205182
    print('Hexadecimal representation of %d is %s'%( my_id, fun_1( my_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())
