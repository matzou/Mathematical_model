import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D


def Lotka_Volterra(ys, ts, r1, r2, r3, b1, b2, gamma12, gamma13, gamma21, gamma23, gamma31, gamma32):
    N1, N2, N3 = ys
    d_N1 = N1 * (r1 - b1 * N1 - gamma12 * N2 - gamma13 * N3)
    d_N2 = N2 * (r2 - b2 * N2 - gamma21 * N1 - gamma23 * N3)
    d_N3 = N3 * (-r3 + gamma31 * N1 + gamma32 * N2)
    return np.array([d_N1, d_N2, d_N3])


def main():
    N1 = 0.3
    N2 = 0.3
    N3 = 0.3

    r1, r2, r3 = 0.1, 0.1, 0.1
    b1, b2 = 0.1, 0.05
    gamma12, gamma13 = 0.16, 0.05
    gamma21, gamma23 = 0.1, 0.16
    gamma31, gamma32 = 0.16, 0.1

    ys = np.array([N1, N2, N3])
    ts = np.linspace(0, 365., 5000)
    soln = odeint(Lotka_Volterra, ys, ts,
                  args=(r1, r2, r3, b1, b2, gamma12, gamma13, gamma21, gamma23, gamma31, gamma32))
    rs, fs, gs = soln.T

    plt.plot(ts, rs, label=r"$N1$")
    plt.plot(ts, fs, label=r"$N2$")
    plt.plot(ts, gs, label=r"$N3$")

    plt.title("$Lotka-VolterraEquation$")
    plt.xlabel("$time$")
    plt.ylabel("$Numbers$")
    plt.legend()
    plt.show()

    #３次元プロット
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.set_title("3dimensions Plot", size=20)

    # 軸ラベルのサイズと色を設定
    ax.set_xlabel("Prey1", size=15, color="black")
    ax.set_ylabel("Prey2", size=15, color="black")
    ax.set_zlabel("Predator", size=15, color="black")

    ax.plot(rs, fs, gs, color="green")
    plt.show()


if __name__ == "__main__":
    main()