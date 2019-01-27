# -*- coding: utf-8 -*-
"""
Gráfico de una viga en voladizo

@author: Nicolas Guarin-Zapata
@date: Febrero 14, 2018
"""
from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("../img/matplotlib.mplstyle")

# Data
fname = "../data/international_standard_atmosphere.csv"
labels = np.genfromtxt(fname, delimiter=",", usecols=(1,), skip_header=1,
                       dtype=str)
altitude = np.loadtxt(fname, delimiter=",", usecols=(3,), skiprows=1)
pressure = np.loadtxt(fname, delimiter=",", usecols=(6,), skiprows=1)
altitude, pressure = np.meshgrid(altitude, pressure)

# Plotting
plt.figure(figsize=(2, 6))
plt.pcolormesh(np.log(pressure), cmap="magma")
plt.ylabel(u"Altitude MSL (m)")
plt.xticks([])
plt.show()

plt.savefig("1d.png", transparent=True, dpi=300, bbox_inches="tight")