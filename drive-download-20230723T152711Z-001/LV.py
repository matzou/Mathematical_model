import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from scipy.integrate import odeint

#数理モデルの設定
def Lotka_Volterra(ys, ts, r1, r2, b1, b2, gamma_12, gamma_21):
    N1, N2 = ys
    d_N1 = N1 * (r1 - b1 * N1 - gamma_12 * N2)
    d_N2 = N2 * (r2 - b2 * N2 - gamma_21 * N1)
    return np.array([d_N1, d_N2])


def main():
    N1 = 0.1
    N2 = 0.8

    r1, r2 = 1.0, 1.0
    b1, b2 = 1.8, 1.0

    gamma = [[2.0, 1, 5], [2.0, 2.5], [0.8, 1.2], [0.8, 2.5]]

    for i in range(4):
        gamma_12, gamma_21 = gamma[i][0], gamma[i][1]

        if r1 / b1 < r2 / gamma_21 and r2 / b2 > r1 / gamma_12:
            print(1)
        elif r1 / b1 > r2 / gamma_21 and r2 / b2 > r1 / gamma_12:
            print(2)
        elif r1 / b1 < r2 / gamma_21 and r2 / b2 < r1 / gamma_12:
            print(3)
        else:
            print(4)
        # print(r1/b1, r2/gamma_21, r2/b2, r1/gamma_12)

        ys = np.array([N1, N2])
        ts = np.linspace(0, 30, 1000)
        soln = odeint(Lotka_Volterra, ys, ts, args=(r1, r2, b1, b2, gamma_12, gamma_21))
        rs, fs = soln.T

        plt.plot(ts, rs, label=r"$N1$")
        plt.plot(ts, fs, label=r"$N2$")

        plt.title("$Lotka-Volterra\ Equation$")
        plt.xlabel("$time$")
        plt.ylabel("$Numbers$")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    main()