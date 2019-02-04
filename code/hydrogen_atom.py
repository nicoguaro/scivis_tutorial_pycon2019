#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 13:11:07 2019

@author: nguarinz
"""
import numpy as np
from scipy.special import eval_genlaguerre, sph_harm, factorial
from scipy import stats


def hydrogen_wave(n=4, l=3, m=1,
                  limits=(-20, 20, -20, 20, -20, 20),
                  grid=(101, 101, 101)):
    """
    """
    xmin, xmax, ymin, ymax, zmin, zmax = limits
    nx, ny, nz = grid
    X, Y, Z = np.mgrid[xmin:xmax:nx*1j,
                       ymin:ymax:ny*1j,
                       zmin:zmax:nz*1j]
    R = np.sqrt(X**2 + Y**2 + Z**2)
    Rmin = stats.scoreatpercentile(R.ravel(), 1)
    R[R < Rmin] = Rmin
    Phi = np.arccos(Z/R)
    Theta = np.arctan2(X, Y)
    Rho = 2*R/n
    norm = np.sqrt((2/n)**3 * factorial(n - l - 1)/(2*n*factorial(n + l)))
    Lag = eval_genlaguerre(n - l - 1, 2*l + 1, Rho)
    Sph = sph_harm(m, l, Theta, Phi)
    wave = norm * np.exp(-0.5*Rho) * Rho**l * Lag * Sph
    return X, Y, Z, wave


# Data
X, Y, Z, wave = hydrogen_wave()
prob_density = np.real(np.conjugate(wave) * wave)
phase = np.angle(wave)

# Mayavi
from mayavi import mlab
mlab.contour3d(X, Y, Z, prob_density, contours=[3e-5])
axes = mlab.axes()
axes.label_text_property.font_family = 'times'
axes.label_text_property.italic = False
axes.title_text_property.font_family = 'times'
axes.axes.x_label = 'x'
axes.axes.y_label = 'y'
axes.axes.z_label = 'z'

## Matplotlib
from skimage import measure
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

verts, faces, _, _ = measure.marching_cubes_lewiner(prob_density, 3e-5)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(verts[:, 0], verts[:,1], faces, verts[:, 2],
                cmap='Spectral', lw=1)
plt.show()
