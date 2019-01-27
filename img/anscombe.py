# -*- coding: utf-8 -*-
"""
Plot of the Anscombe's quartet

@author: Nicolas Guarin-Zapata
"""
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("ggplot")
plt.rcParams["mathtext.fontset"]='cm'

data = np.loadtxt("../data/ascombe.csv", delimiter=",")
X = data[:, :4]
Y = data[:, 4:]

plt.figure(figsize=(10, 6))
for k in range(4):
    plt.subplot(2, 2, k + 1)
    plt.plot(X[:, k], Y[:, k], 'ok')
    plt.plot([2, 20], [4, 13])
    plt.axis([2, 20, 2, 14])
    if k >= 2:
        plt.xticks(np.linspace(2, 20, 4))
        plt.xlabel(r"$x$")
    else:
        plt.xticks(np.linspace(2, 20, 4), [])
    if k % 2 == 0:
        plt.yticks(np.linspace(2, 14, 4))
        plt.ylabel(r"$y$")
    else:
        plt.yticks(np.linspace(2, 14, 4), [])

plt.tight_layout()
plt.savefig("anscombe.svg", bbox_inches="tight")
plt.show()