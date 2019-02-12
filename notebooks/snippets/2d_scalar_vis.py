"""
This dataset corresponds to a slice of a tomography dataset. This fact makes
the image visualization appropriated because of familiarity with this type of
datasets.
"""

data = np.load("../data/2d_exercise.npy")
plt.imshow(data, cmap="bones")
