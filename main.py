#モジュールのインポート
import numpy as np
from scipy.sparse import csr_matrix as sparse_matrix
from scipy import integrate

def make_differential_ops(nx, dx):
    f0 = np.identity(nx, dtype=int)
    f1 = np.roll(f0, 1, axis=1)#u(delta+1)
    f2 = np.roll(f0, 2, axis=1)#u(delta+2)
    f_1 = f1.transpose()#u(delta-1)
    f_2 = f2.transpose()#u(delta-2)

    #1階、3階偏微分
    Dx = sparse_matrix(f1 - f_1) / (2.0 * dx)
    Dxxx = sparse_matrix(f2 - 2.0 * f1 + 2.0 * f_1 - f_2) / (2.0 * dx**3)

    return Dx, Dxxx

def f_kdv(t, u, df1, df3):
    u_x = df1.dot(u)
    u_xxx = df3.dot(u)

    #2、3項目を移項した形
    return -6.0 * u * u_x - u_xxx

def main():
    nx = 1000
    x_max = 100.0
    x = np.linspace(0, x_max, nx, endpoint=False)
    dx = x[1] - x[0]

    #初期値
    u0 = np.sin(x * (2.0 * np.pi / x_max))
    op_df1, _, op_df3 = make_differential_ops(nx, dx)

    t_max = 10.0
    sol = integrate.solve_ivp(f_kdv, (0, t_max), u0, dense_output=True, args=(op_df1, op_df3), rtol=1e-8)
    print(sol.message)

    nt = 101
    t = np.linspace(0, t_max, nt)
    dt = t[1] - t[0]

    u_xt = sol.sol(t)  # u(x, t)
    u_tx = u_xt.T  # u(t, x)

    #結果の保存
    np.savez("kdv_solve_ivp", x=x, t=t, u_tx=u_tx)

if __name__ == '__main__':
    main()