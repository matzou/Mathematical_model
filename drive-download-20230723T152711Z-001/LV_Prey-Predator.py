import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from scipy.integrate import odeint


def Lotka_Volterra(ys, ts, r, a, s, b):
    N1, N2 = ys
    d_N1 = N1 * (r - a * N2)
    d_N2 = N2 * (-s + b * N1)
    return np.array([d_N1, d_N2])


def main():
    N1 = 20
    N2 = 4
    r, a, s, b = 2, 1, 2, 1
    ys = np.array([N1, N2])
    ts = np.linspace(0, 30., 5000)
    soln = odeint(Lotka_Volterra, ys, ts, args=(r, a, s, b))
    rs, fs = soln.T
    plt.plot(ts, rs, label=r"$Prey$")
    plt.plot(ts, fs, label=r"$Predator$")
    plt.title("$Lotka-Volterra\ Equation$")
    plt.xlabel("$time$")
    plt.ylabel("$Numbers$")
    plt.legend()
    plt.show()
    plt.plot(rs, fs, label=r"$movement$", color="g")
    plt.title("$Lotka-Volterra\ Equation\ Prey-Predator$")
    plt.xlabel("$Prey$")
    plt.ylabel("$Predator$")
    plt.legend()
    plt.show()

    # ３次元プロット
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.set_title("3dimensions Plot", size=20)

    # 軸ラベルのサイズと色を設定
    ax.set_xlabel("Prey", size=15, color="black")
    ax.set_ylabel("Predator", size=15, color="black")
    ax.set_zlabel("Time", size=15, color="black")

    ax.plot(rs, fs, ts, color="green")
    plt.show()
if __name__ == "__main__":
    main()
