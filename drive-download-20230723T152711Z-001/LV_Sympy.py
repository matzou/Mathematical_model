import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
from sympy.plotting import plot
sym.init_printing(use_unicode=True)

#変数の設定
x,y = sym.symbols("x y")
t = sym.symbols("t")
r1,r2,b1,b2,gamma12,gamma21 = sym.symbols("r1,r2,b1,b2,gamma12,gamma21")

#関数の定義
sym.solve(
    [
        sym.Eq((r1-b1*x-gamma12*y)*x, 0),
        sym.Eq((r2-b2*y-gamma21*x)*y, 0)
    ],[x,y])


# 流線プロットによるベクトル場の可視化
def plotVecField(r1, r2, b1, b2, gamma12, gamma21, rangeX, rangeY, meshX, meshY, pat, sol=None):
    U = (r1 - b1 * meshX - gamma12 * meshY) * meshX
    V = (r2 - b2 * meshY - gamma21 * meshX) * meshY

    M = np.sqrt(U ** 2 + V ** 2)


    lineX1 = np.linspace(rangeX[0], rangeX[1], 100)
    lineX2 = np.linspace(rangeX[0], rangeX[1], 100)
    lineX3 = np.array([r1 / b1 for i in range(100)])
    lineX4 = np.array([(b2 * r1 - gamma12 * r2) / (b1 * b2 - gamma12 * gamma21) for i in range(100)])
    isocline1 = np.linspace(rangeY[0], rangeY[1], 100)
    isocline2 = np.array([r2 / b2 for i in range(100)])
    isocline3 = np.linspace(rangeY[0], rangeY[1], 100)
    isocline4 = np.array([(b1 * r2 - gamma21 * r1) / (b1 * b2 - gamma12 * gamma21) for i in range(100)])

    # 作図
    fig, axes = plt.subplots(figsize=(8, 8))
    strm = plt.streamplot(meshX, meshY, U, V, color=M, density=(0.8, 0.8), linewidth=1,
                          arrowsize=2, cmap='gist_rainbow_r')
    fig.colorbar(strm.lines)
    axes.set_aspect("equal")
    axes.set_title(pat)
    plt.plot(lineX1, isocline1, "b--", linewidth=3)
    plt.plot(lineX2, isocline2, "r--", linewidth=3)
    plt.plot(lineX3, isocline3, "y--", linewidth=3)
    plt.plot(lineX4, isocline4, "g--", linewidth=3)
    plt.plot(0, 0, "ko", 0, r2 / b2, "ko", r1 / b1, 0, "ko", (b2 * r1 - gamma12 * r2) / (b1 * b2 - gamma12 * gamma21),
             (b1 * r2 - gamma21 * r1) / (b1 * b2 - gamma12 * gamma21), "ko", markersize=8)
    plt.xlim(rangeX[0] - 0.05, rangeX[1])
    plt.ylim(rangeY[0] - 0.05, rangeY[1])
    plt.xlabel("Creatures A")
    plt.ylabel("Creatures B")

    if sol is not None:
        plt.plot(sol[0], sol[1], ".", linewidth=2)


rangeX = (0, 1.5)
rangeY = (0, 1.5)
meshX, meshY = np.meshgrid(
    np.arange(rangeX[0], rangeX[1], .01),
    np.arange(rangeY[0], rangeY[1], .01))

r1 = 1.0
r2 = 1.0
b1 = 1.8
b2 = 1.0
gamma = [[2.0, 1.5], [2.0, 2.5], [0.8, 1.2], [0.8, 2.5]]
gamma12, gamma21 = 0.8, 1.2
pattern = ["a", "b", "c", "d"]

U = (r1 - b1 * meshX - gamma12 * meshY) * meshX
V = (r2 - b2 * meshY - gamma21 * meshX) * meshY

for i in range(4):
    gamma12, gamma21 = gamma[i][0], gamma[i][1]
    pat = pattern[i]

    plotVecField(r1, r2, b1, b2, gamma12, gamma21, rangeX, rangeY, meshX, meshY, pat, sol=None)