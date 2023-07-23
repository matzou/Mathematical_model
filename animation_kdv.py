from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#アニメーションを保存する用の関数
def save_animation(x, t, u_tx, ymin, ymax, filename):
    fig, ax = plt.subplots()

    ax.set_xlabel("$x$")
    ax.set_ylabel("$u(x)$")
    ax.set_ylim((ymin, ymax))

    artists = []
    for i in range(t.size):
        artist = ax.plot(x, u_tx[i, :], '-b')
        artist += [ax.text(0.05, 1.05, "t = %.2f" % t[i], transform=ax.transAxes)]
        artists.append(artist)

    anim = animation.ArtistAnimation(fig, artists, interval=100, repeat=False)
    anim.save(filename, writer="pillow")  # writer="pillow" or "imagemagick" for GIF
    print("saved as '{}'".format(filename))

def main():
    #他のファイルからKdVの関数を呼び出す
    npz = np.load("kdv_solve_ivp.npz")
    print("npz.file = ", npz.files)

    x = npz['x']
    t = npz['t']
    u_tx = npz['u_tx']
    print("x.shape =", x.shape)
    print("t.shape =", t.shape)
    print("u_tx.shape =", u_tx.shape)

    # make an animation
    print("Making animation...")
    save_animation(x, t, u_tx, ymin=-1.5, ymax=3.0, filename="kdv_solve_ivp.gif")


if __name__ == '__main__':
    main()
