import matplotlib.pyplot as plt
import numpy as np
# import seaborn

# while True:


X = np.linspace(0, 2, 1000)
Y = X ** 2 + np.random.random(X.shape)

# plt.ion()
graph = plt.plot(X, Y)[0]

while True:
    Y = X ** 2 + np.random.random(X.shape)
    graph.set_ydata(Y)
    plt.pause(0.01)
    # plt.draw()

    a = np.random.random((1060, 1600))
    plt.imshow(a, cmap='hot', interpolation='nearest')

    # uniform_data = np.random.rand(100, 102)
    # ax = seaborn.heatmap(uniform_data, linewidth=0.5)
