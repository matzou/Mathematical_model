import numpy as np
import matplotlib.pyplot as plt
import math
import sympy as sp
from sympy.plotting import plot
sp.init_printing()

#変数の設定・初期条件設定
t = sp.var("t")
N = sp.Function("N")(t)
r, K = 1, 1

#微分方程式をモジュールSympyで解く
eq = sp.Eq(sp.diff(N,t), r*N - r*N**2/K)
ans = sp.dsolve(eq, ics = {N.subs(t,0):0.01})

plot(ans.rhs, (t, 0, 10))