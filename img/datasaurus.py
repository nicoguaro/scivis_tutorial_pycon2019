# -*- coding: utf-8 -*-
"""
Plot of the Datasaurus Dozen

@author: Nicolas Guarin-Zapata
"""
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("ggplot")
plt.rcParams["mathtext.fontset"]='cm'

labels = np.genfromtxt("../data/DatasaurusDozen.tsv", delimiter="\t",
               usecols=(0,), skip_header=1, dtype=str)
X = np.loadtxt("../data/DatasaurusDozen.tsv", delimiter="\t",
               usecols=(1,), skiprows=1)
Y = np.loadtxt("../data/DatasaurusDozen.tsv", delimiter="\t",
               usecols=(2,), skiprows=1)
list_labels = ['wide_lines', 'star', 'h_lines', 'high_lines', 'v_lines',
               'circle', 'bullseye', 'slant_up', 'slant_down', 'x_shape',
               'dots', 'away', 'dino']

#%% Plot of the dozen
plt.figure(figsize=(10, 6))
for k, label in enumerate(list_labels[:-1]):
    plt.subplot(3, 4, k + 1)
    plt.plot(X[labels == label],Y[labels == label], 'ok',
             markersize=3)
    plt.axis("image")
    plt.axis([0, 100, 0, 100])
    if k >= 8:
        plt.xticks(np.linspace(0, 100, 5))
        plt.xlabel(r"$x$")
    else:
        plt.xticks(np.linspace(0, 100, 5), [])
    if k % 4 == 0:
        plt.yticks(np.linspace(0, 100, 5))
        plt.ylabel(r"$y$")
    else:
        plt.yticks(np.linspace(0, 100, 5), [])

plt.tight_layout()
plt.savefig("datasaurus-dozen.svg", bbox_inches="tight")

#%% Plot of the datasaurus
plt.figure(figsize=(2.5, 1.5))
plt.plot(X[labels == 'dino'], Y[labels == 'dino'], 'ok',
             markersize=3)
plt.axis("image")
plt.axis([0, 100, 0, 100])
plt.xticks(np.linspace(0, 100, 5))
plt.yticks(np.linspace(0, 100, 5))
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.savefig("datasaurus.svg", bbox_inches="tight")
plt.show()