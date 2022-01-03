def f(x:float) -> float:
    return -2.4*x**3+6.3*x**2+0.4*x+6
#--------------------------------
def secant(f, x0: float, eps: float=1e-7 ) -> float:
   """
   solves f(x) = 0 by secant method with precision eps
   :param f: f
   :param x0: starting point
   :param eps: precision wanted
   :return: root of f(x) = 0
   """
   x=x0
   x_prev=x0 + 2 * eps
   i = 0
   while abs(x - x_prev) >= eps and i < 1e3:
      x -= f(x) / (f(x) - f(x_prev)) * (x - x_prev)
      x_prev = x
      i += 1
   return x
#--------------------------------
x0=int(input("x="))
x=secant(f, x0)
print(x)
