import numpy as np
import sys


def getDataPoints(weights, m, n):

    w = np.array(weights)
    dataPoints = np.zeros((m+n, 3))

    i = 0
    positive_count = 0
    negative_count = 0
    while i < m + n:
        x = [round(np.random.uniform(-100, 100), 1), round(np.random.uniform(-100, 100), 1)]
        product = w[1] * x[0] + w[2] * x[1] + w[0]
        if product <= 0:
            if negative_count < n:
                dataPoints[i] = np.append(x, -1)
                negative_count += 1
            else:
                continue
        else:
            if positive_count < m:
                dataPoints[i] = np.append(x, 1)
                positive_count += 1
            else:
                continue

        i += 1

    np.savetxt('train.txt', dataPoints, fmt='%.1f')


def main():

    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]

    # 将字符串转变为数组
    a = a.strip('[]<>')
    a = a.split(',')
    a = list(map(int, a))

    b = int(b)
    c = int(c)
    getDataPoints(a, b, c)


if __name__ == '__main__':
    main()
