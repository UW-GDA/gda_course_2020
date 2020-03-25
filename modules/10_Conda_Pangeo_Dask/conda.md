# Conda and Jupyter Setup Instructions

UW Geospatial Data Analysis  
CEE498/CEWA599  
Friedrich Knuth and David Shean  

## Justification

Sadly, our time together is coming to an end, which means the Jupyterhub will no longer be available. No worries! We can recreate an identical environment, so all of the notebooks you created should run as if they were on the Jupyterhub! You can also set up custom python environment(s) for your local system.

## [What is conda?](https://conda.io/en/latest/)

## Basic terminology

**package manager**  
_helps you download and organize open-source software on your machine (think homebrew (MacOS), apt-get (Linux), chocolatey (Windows) etc...)_

**package**  
_a package consists of executable machine instructions, e.g. underlying C/C++ code for NumPy_  

**environment**  
_high-level organization of dependencies (packages that require other packages) and versions to avoid conflicts_  

**channel**  
_source for retrieving packages_

## Why?

But I already have Python installed on my computer, why do I need this?

# How to replicate the GDA JuptyerHub environment

## Install Conda
Downloand and install the Python 3 version of [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/distribution/). 

Miniconda gives you just the conda package manager, while Anaconda provides the package manager along with a large set of additional tools. 

All you need to proceed is the package manager provided by Miniconda, which is a lighter and faster install. The package manager is what enables you to pull together various Python packages, resolve their dependencies, and create a functional custom Python environment. 

Follow the instructions for installation: https://conda.io/projects/conda/en/latest/user-guide/install/index.html

Select yes to initialize conda.  Close your terminal/shell, then open a new terminal session and type `conda` to verify a successfull installation. 

Run the following to see various useful info about your install:
`conda info`

Update to latest version of conda:
`conda update conda`

## Creating the CEWA 599 GDA environment

The environment used for the winter 2020 course is in `uwgda-image` repo in the UW-GDA organization on github:  
https://github.com/UW-GDA/uwgda-image/blob/master/binder/environment.yml

Download or copy the content of this file to your computer. On github, you can right-click on the "RAW" button and save link as.

View it with a text editor and note that it is basically just a list of package names (many you will recognize from this course).  The first line `uwgda2020` defines the conda environment name.

Note that we hardcoded version numbers for most packages. This is not necessary, but is a best practice for our classroom situation. Some packages would likely be updated during the quarter, potentially changing/breaking some functionality. For your personal setup, you may want to remove the version numbers, so conda will automatically fetch the latest version of each package, and you can access latest features (but no guarantee that our notebooks will run out of the box).

To recreated the `uwgda2020` environment on your local machine, run the following from a terminal:

`conda env create -f environment.yml`

This will take a few minutes to download and unzip all of the packages.

Once that's done, you need to activate the `uwgda2020` environment, which contains all of the packages/versions used on the Jupyterhub:

`conda activate uwgda2020`

You should get a different terminal prompt display with `uwgda2020`.  Now when you type `python` it should run the python executable in that conda environment, and all of the GDA packages will be available.

## Starting a jupyter notebook server

Once you have created an environment with the Jupyter kernel installed (make sure you have activated the environment), navigate to your local directory containing your notebooks (from the class, or new notebooks that you will create), then run:

`jupyter lab`

This will launch your browser and bring up the jupyter lab interface. Now, you can open and run the GDA course notebooks, or create your own notebooks with the GDA environment.

To load the classic Jupyter notebook interface:  
`jupyter notebook` 

_If using the classic notebook interface, you should use the matplotlib backend _ `matplotlib %notebook` _ instead of the_ `matplotib %widget` _we used in Jupyter lab._

## Removing or starting over

Most of the time, you should be able to `conda update`, or manage environments to add/remove packages.

One of the best things about conda is the fact that it creates isolated environments, separate from your system Python. So if you no longer need it, or you have unresolvable issues, you can always just delete and start over with a fresh install.

https://docs.anaconda.com/anaconda/install/uninstall/

# Creating a custom setup from scratch

## Conda channels

Sometimes, certain packages or newer versions aren't available through the default conda package distribution source. Fortunately, you can point conda to other "channels" which have different packages available, and maybe more up to date versions. 

https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html

The `conda-forge` channel is user-supported, and has largely superseded the main anaconda package channel

For example, this package called [RISE](https://github.com/damianavila/RISE), which is a jupyter notebook extention that let's you turn your notebook into a presentation, is only available through the conda-forge channel. Note that the author specifies installation as:

`conda install -c conda-forge rise`

This means _conda, please install the package called "rise" from the conda-forge channel_. 

Generally, it is safe to grab the latest packages from conda-forge, which is usually somewhat ahead of the default channel. If you find yourself on shaky ground, you can always specify a previous, more stable version of the package you are looking to install. This is one reason why we use a package manager.

Let's add the conda-forge channel, by typing the following into your terminal:

`conda config --add channels conda-forge`
`conda config --set channel_priority strict`

This adds the conda-forge channel to your conda configuration file located in your home directory (`~/.condarc`). You only need to do this once. Now, when creating a new environment conda will first look for a package on conda-forge, then on the default anaconda distribution channel.

When shopping around for packages, a useful resource to check is the anaconda [repository](https://anaconda.org/anaconda/repo). Search "geopandas", for example and you will see that it is most popular through the conda-forge channel. The package repository is a great way to guage how popular and well supported a specific package is within the community.

## Creating a custom Conda environment

Let's create a new custom envornment called `my_favorite_env` with geopandas and matplotlib.

`conda create -n my_favorite_env geopandas matplotlib`

Notice that conda lists a number of other packages to be installed. These are the dependencies for geopandas and matplotlib. Some of them include seaborn, pandas, numpy etc. which means you don't always have to specify those if you know they will be installed as dependencies for the main packages you want in your environment (in this case, geopandas and matplotlib). If you aren't sure, you can always add them to the installation call, just to be safe.

## Useful commands

<b>List all your environments</b>

`conda env list`

<b>Delete an environment</b>

`conda env remove -n my_favorite_env`

<b>Activate an environment</b>

`conda activate my_favorite_env`

<b>Deactivate a loaded environment</b>

`conda deactivate`

<b>List all installed packages for an environment</b>

`conda list -n my_favorite_env`

<b>Add a package to an environment</b>
In this case we are adding 'xarray'.

`conda install -n my_favorite_env xarray`

<b>Add a package with specific version to an environment</b>
In this case we are adding 'geopandas' with version 0.3.0.

`conda install -n my_favorite_env geopandas==0.3.0`

<b>Remove a package from an environment</b>
In this case we are removing 'geopandas'.

`conda remove -n my_favorite_env geopandas`

<b>Upgrade a installed package from an environment</b>
In this case we are updating 'geopandas' to the latest version.

`conda upgrade -n my_favorite_env geopandas`

<b>Create an environment with specific version of a package</b>

`conda create -n my_favorite_env geopandas==0.3.0 matplotlib`

<b>Create an environment with a specific version of Python</b>

`conda create -n my_favorite_env python=2.7 geopandas matplotlib`

## Jupyter integration

To create a Python environment that can handle jupyter notebooks, add `jupyterlab` to the environment install. 

For example:  
`conda create -n my_favorite_env geopandas matplotlib jupyterlab`

Activate your envornment:  
`conda activate my_favorite_env`

You can then start the jupyter lab environment in your local browser:  
`jupyter lab` 

## Running a Jupyter notebook on a remote machine

Some additional notes (thanks to Shashank!) on how to launch a Jupyter notebook server on a remote machine:

1. Open a terminal
1. Log in to the remote machine: `ssh username@serverIP`
1. `cd` into directory where your notebooks/data are stored
1. `conda activate` your environment
1. Start the jupyter lab/notebook `jupyter lab --port=8888 --no-browser`
1. Open a new terminal on your local machine
1. Open an ssh tunnel to the remote machine: `ssh -f -L 8888:localhost:8888 -N your_user@serverIP`
1. Open your local browser and paste the address `http://localhost:8888`, which should bring up the remote jupyter lab interface
1. :tada: