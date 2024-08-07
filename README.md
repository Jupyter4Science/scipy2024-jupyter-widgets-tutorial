# Building Complex Web Applications with Jupyter Notebooks

## Prerequisites

Prior exposure to ipywidgets and/or familiarity with object-oriented
programming is recommended. We review the basics of ipywidgets within
the first hour and quickly move on to more advanced design principles.

## Installation Instructions

There are two ways to access this tutorial. We recommend installing the
environment locally with Anaconda or Miniconda, but if you experience
trouble and need a quick backup, feel free to launch this tutorial with
Binder.

## Local Installation

If you would like to run this tutorial locally on your own computer,
please follow these instructions:

1.  Clone this repository with `git clone https://github.com/Jupyter4Science/scipy2024-jupyter-widgets-tutorial`
2.  If you don’t have it already, you will need to [download and install
    Miniconda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)
3.  Run `conda env create -f environment.yml` to create a conda
    environment called `complexapps-2024`
4.  Run `conda activate complexapps-2024` to activate the conda
    environment
5.  Change directory into the tutorial materials and run `jupyter lab` to launch JupyterLab

## How to use

We will follow the notebooks in the tutorial sequentially, starting with
`00_welcome.ipynb`.

**Put a post-it on your computer when you have this notebook open.**

## Binder

You can launch these notebooks in a Binder environment by clicking the
badge below. This requires no extra installation of software on your part. Just
click the link and follow along.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Jupyter4Science/scipy2024-jupyter-widgets-tutorial/tree/main/main?labpath=00_welcome.ipynb)

### How long will my Binder session last?

Binder will automatically shut down user sessions that have more than 10
minutes of inactivity (if you leave a jupyterlab window open in the
foreground, this will generally be counted as “activity”). Binder tries
to guarantee that active sessions will last up to 6 hours.

### What if my session shuts down during a break?

We will start from a fresh checkpoint after every break, so if your
Binder session ends, you can just restart a new session and the
beginning of the next section.
