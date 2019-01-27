# -*- coding: utf-8 -*-
"""
One dimensional visualization of atmospheric pressure

@author: Nicolas Guarin-Zapata
"""
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("../img/matplotlib.mplstyle")

# Data
fname = "../data/international_standard_atmosphere.csv"
labels = np.genfromtxt(fname, delimiter=",", usecols=(1,), skip_header=1,
                       dtype=str)
altitude = np.loadtxt(fname, delimiter=",", usecols=(3,), skiprows=1)
pressure = np.loadtxt(fname, delimiter=",", usecols=(6,), skiprows=1)

# Plotting
plt.figure()
plt.plot(pressure, altitude)
plt.xlabel("Pressure (Pa)")
plt.ylabel(u"Altitude MSL (m)")
plt.show()
