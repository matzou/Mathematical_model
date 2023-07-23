import numpy as np
import matplotlib.pyplot as plt
import math
import sympy as sp
from sympy.plotting import plot
sp.init_printing()

#初期条件
n = 10
N = np.zeros(n+1)
N[0] = 0.01
t = np.arange(1, n+2, 1)
r, K = 1, 1

#通常の数値計算の場合
first = N[0]
for i in range(n):
    T = t[i]
    N[i+1] = first*K/(first + (K-first)*math.e**(-r*T))

plt.plot(t, N, "-o")
plt.show()