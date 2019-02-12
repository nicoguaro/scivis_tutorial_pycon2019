def elec_field(x, y, x_coords=[0], y_coords=[0], charges=[1]):
    """Compute the electric field of n charged particles"""
    Ex = np.zeros_like(x)
    Ey = np.zeros_like(x)
    for x0, y0, q in zip(x_coords, y_coords, charges):
        R = np.sqrt((x - x0)**2 + (y - y0)**2) + 1e-6
        Ex += q*(x - x0)/R**3
        Ey += q*(y - y0)/R**3
    return Ex, Ey


y, x = np.mgrid[-3:3:21j, -3:3:21j]
Ex, Ey = elec_field(x, y, x_coords=[-1, 1], y_coords=[0,0],
                    charges=[1, -1])
Emag = np.sqrt(Ex**2 + Ey**2)
dir_x = Ex/Emag
dir_y = Ey/Emag

plt.figure(figsize=(5, 4))
plt.subplot(221)
plt.quiver(x[::2, ::2], y[::2, ::2], dir_x[::2, ::2], dir_y[::2, ::2],
           np.log10(Emag[::2, ::2]), cmap="autumn", scale_units="inches",
           scale=5, width=0.015, pivot="mid")
plt.colorbar()
plt.axis("image")

plt.subplot(222)
plt.streamplot(x, y, Ex, Ey, color=np.log10(Emag),cmap="autumn")
plt.colorbar()
plt.axis("image")

plt.subplot(223)
plt.contourf(x, y, np.log10(Emag), cmap="autumn")
plt.colorbar()
plt.quiver(x[::2, ::2], y[::2, ::2], dir_x[::2, ::2], dir_y[::2, ::2],
           scale_units="inches", scale=5, width=0.010, pivot="mid")
plt.axis("image")


plt.subplot(224)
plt.contourf(x, y, np.log10(Emag), cmap="autumn")
plt.colorbar()
plt.streamplot(x, y, Ex/Emag, Ey/Emag, color="black")
plt.axis("image")

plt.tight_layout()
