# Introduction to Scientific Visualization with Python

This is the repository for the PyCon Colombia 2019 tutorial on Scientific


 1. [Installation](#installation-instructions)


 # Installation Instructions

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
 source activate scivistutorial
 ```
 or on Windows:

 ```console
 activate scivistutorial
 ```

# Optional installation

## ParaView
We would also discuss ParaView as platform for visualization. The suggested
installation method is to download the package for your particular operative
system on the [official websise](https://www.paraview.org/download/).

## vtki

``vtki`` (previously known as VTKInterface) is a VTK helper module that takes
a different approach on interfacing with VTK through NumPy and direct array
access.

To install ``vtki`` use

    pip install vtki

in your environment.

# Checking the installation

After installation you can check if everything is working running

    python check_installation.py
