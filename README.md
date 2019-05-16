

# Introduction to Scientific Visualization with Python

This is the repository for the PyCon Colombia 2019 tutorial on Scientific
visualization.

<img src="./img/heat_smiley.gif"
    alt="Solution of the heat equation"
    width=400>

The previous animation presents a visualization for the heat transfer in a
plate with fixed temperature in the borders set to zero degrees and an initial
temperature distribution following a smiley shape. If we wait long enough the
solution should converge to a stationary state of zero degrees over the whole
domain. The animation can be reproduced running the example provided in
``./code/heat_iteration.py``, for example

    python heat_iteration.py

**Contents**

 1. [Installation](##installation-instructions)
 2. [Optional installation](##optional-installation)
 3. [Checking the installation](##checking-the-installation)


## Installation Instructions

We strongly encourage you to use ``conda`` to install the required packages for
this tutorial. There are non-Python dependencies required that make manual
installation or installing with ``pip`` very involved.

Note also that this tutorial is written for Python 3.6. No guarantees of any
kind are made that it will be compatible with Python 2.



Create a conda environment using the file ``environment.yml`` in the root
of the repository using

```console
conda env create -f environment.yml
```

for Windows use

```console
conda env create -f environment_win.yml
```

instead.

This will create a conda environment named `scivistutorial` with all of the
required packages.

You can activate the environment with

```console
conda activate scivistutorial
```

To activate the [X3D]() backend for Mayavi, that can be used for interactive
visualization in the Jupyter notebook use the following:

```console
jupyter nbextension install --py mayavi --user
```

## Optional installation

### ParaView

We would also discuss ParaView as a platform for visualization. The suggested
installation method is to download the package for your particular operative
system on the [official websise](https://www.paraview.org/download/).

### vtki

``vtki`` (previously known as ``VTKInterface``) is a VTK helper module that
takes a different approach on interfacing with VTK through NumPy and direct
array access.

To install ``vtki`` use

```console
pip install vtki
```

in your environment.

## Checking the installation

After installation you can check if everything is installed

```console
python check_install.py
```

To check if everything is working run the demos with

```console
python demo.py
```

## License
All code is under MIT license and media under Creative Commons Attribute.

The content of this repository is licensed under the
[Creative Commons Attribution 4.0 license](http://choosealicense.com/licenses/cc-by-4.0/),
and the source code that accompany the content is licensed under the
[MIT license](https://opensource.org/licenses/mit-license.php).
