mlab.figure()
mlab.points3d([-2, 2], [0, 0], [0, 0], scale_factor=2)
mlab.flow(X, Y, Z, Ex, Ey, Ez, scalars=V, linetype="tube", colormap="viridis",
          integration_direction="both", seedtype="sphere",
          seed_visible=False, seed_resolution=5000)
mlab.contour3d(X, Y, Z, V, contours=[0.03])
mlab.show()
