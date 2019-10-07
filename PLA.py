import numpy as np
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import sys


def plotPointsAndLine(filename):

    data_points = np.loadtxt(filename)
    points_num = data_points.shape[0]

    w = np.zeros((1, 3))
    is_completed = False

    i = 0
    while not is_completed and i < points_num:

        if data_points[i][-1] * (w[0][1]*data_points[i][0]+w[0][2]*data_points[i][1]+w[0][0]) <= 0:
            w[0][1] = w[0][1] + data_points[i][-1] * data_points[i][0]
            w[0][2] = w[0][2] + data_points[i][-1] * data_points[i][1]
            w[0][0] = w[0][0] + data_points[i][-1]
            is_completed = False
            i = 0
        else:
            i += 1

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title('Perceptron learning algorithm')
    plt.xlabel('x1')
    plt.ylabel('x2')
    labels = np.array(data_points[:, 2])
    idx_1 = np.where(data_points[:, 2] == 1)
    p1 = ax.scatter(data_points[idx_1, 0], data_points[idx_1, 1], marker='o', color='b', label='+', s=20)
    idx_2 = np.where(data_points[:, 2] == -1)
    p2 = ax.scatter(data_points[idx_2, 0], data_points[idx_2, 1], marker='x', color='r', label='-', s=20)
    y_value = ((-w[0][0] + 120 * (w[0][1])) / w[0][2], (-w[0][0] - 120 * (w[0][1])) / w[0][2])
    ax.add_line(Line2D((-120, 120), y_value, linewidth=1, color='black'))
    plt.show()

    return w


def main():
    w = plotPointsAndLine(sys.argv[1])
    print(w)


if __name__ == '__main__':
    main()

