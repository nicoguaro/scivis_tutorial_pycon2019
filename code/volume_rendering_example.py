#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 15:50:35 2019

@author: nguarinz
"""
import numpy as np
from mayavi import mlab

x, y, z = np.ogrid[-10:10:20j, -10:10:20j, -10:10:20j]
s = np.sin(x*y*z)/(x*y*z)


mlab.pipeline.volume(mlab.pipeline.scalar_field(s))
mlab.show()