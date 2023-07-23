import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def main():

    fig = plt.figure()
    image_1 = []
    Ts = [i for i in range(0, 50)]

    #波の速度
    c1 = 1
    c2 = 5

    for t in Ts:
        xx = np.linspace(-70, 30, 1000)
        x = np.linspace(-50, 50, 1000)
        theta_1 = np.sqrt(c1)*(xx-c1*t)/2
        theta_2 = np.sqrt(c2) * (x - c2 * t) / 2
        varphi_1 = c1/(2*(np.cosh(theta_1))**2)
        varphi_2 = c2/(2*(np.cosh(theta_2)) ** 2)
        varphi = varphi_1 + varphi_2

        result_1 = plt.plot(x, varphi)
        image_1.append(result_1)

    ani = animation.ArtistAnimation(fig, image_1, interval=200)
    ani.save("not_soliton.gif", writer="imagemagick")
    #plt.show()

    return True

if __name__ == '__main__':
    main()