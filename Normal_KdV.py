import numpy as np
from numpy.fft import rfft, irfft, fftfreq #フーリエ変換用のライブラリ
from scipy.integrate import solve_ivp#隠的ルンゲクッタ法

#KdVモデルの定義
def KdV(t, u, k, a, b):
    #k:波数
    v = rfft(u)
    ux = irfft(1.0j * k * v)
    conv = u*ux
    disp = irfft((1.0j * k)**3 * v)
    return -a * conv - b * disp

#条件設定
L = 2.0#x軸長さ
T = 10#時間

