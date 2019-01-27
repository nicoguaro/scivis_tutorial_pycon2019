#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test the installation for the Scientific visualization workshop on
PyCon 2019

@author: Nicolas Guarin-Zapat
"""
import numpy as np

## Test data: Matlab `peaks()`
x, y = np.mgrid[-3:3:150j,-3:3:150j]
z =  3*(1 - x)**2 * np.exp(-x**2 - (y + 1)**2) \
   - 10*(x/5 - x**3 - y**5)*np.exp(-x**2 - y**2) \
   - 1./3*np.exp(-(x + 1)**2 - y**2) 


#%% Matplotlib
try:
    msg = "Checking Matplotlib installation"
    print(msg)
    print("="*len(msg))
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    from matplotlib.colors import LightSource

    Axes3D
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    
    # Create light source object.
    ls = LightSource(azdeg=0, altdeg=65)
    rgb = ls.shade(z, plt.cm.RdYlBu)
    surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, linewidth=0,
                           antialiased=False, facecolors=rgb)
    plt.show()
    print("Matplotlib is working properly!")
except:
    print("Matplotlib is not working properly!")


#%% Mayavi
try:
    msg = "Checking Mayavi installation"
    print("\n\n" + msg)
    print("="*len(msg))
    from mayavi import mlab
    
    surf = mlab.surf(x, y, z, colormap='RdYlBu', warp_scale='auto')
    # Change the visualization parameters.
    surf.actor.property.interpolation = 'phong'
    surf.actor.property.specular = 0.1
    surf.actor.property.specular_power = 5    
    mlab.show()
    print("Mayavi is working properly!")
except:
    print("Mayavi is not working properly!")


#%% vtki
try:
    msg = "Checking vtki installation"
    print("\n\n" + msg)
    print("="*len(msg))
    import vtki

    grid = vtki.StructuredGrid(x, y, z)
    plotter = vtki.Plotter()
    plotter.add_mesh(grid, scalars=z.ravel(), cmap='RdYlBu',
                     show_edges=False)
    plotter.plot()
    print("vtki is working properly!")
except:
    print("vtki is not working properly!")