# Notes, tips, tricks, gotchas and other useful information

UW Geospatial Data Analysis  
CEE498/CEWA599  
David Shean  

# Github

## First time login
`git config --global user.name "Matt Damon"`  
`git config --global user.email "email@example.com"`

## Authentication
#### Two-factor authentication
* Disabled by default (for new account)
* If you're using an existing Github account and previously enabled two-factor authentication, you may need to disable for successful Github authentication from terminal on Jupyterhub

#### Store credentials for 15 minutes (900 seconds)
*So you don't have to enter github username and password each time you push*  
`git config --global credential.helper 'cache --timeout=900'`

#### Store permanently
`git config --global credential.helper store`

#### git clone via https or ssh?
* Default is https, requires authentication with Github username and password
* Can also set up ssh keys on Jupyterhub, if that doesn't sound intimidating

#### Large notebooks
*May no longer be relevant*
Github can fail to render notebooks. Sometimes reloading works.

If notebook is in a public Github repo, go to https://nbviewer.jupyter.org/ and paste the url to the notebook.

## Github Organization

#### To make your repo visible to students/instructors in the organization
Settings -> Manage Access - > Invite Teams (Green Button) -> gda_w2020_students, and grant read access to desired teams

#### To make your project repo public for the world
Settings -> Options (left menu) -> Danger Zone -> Make public

To check public visibility, you can always sign out of Github and navigate the GDA org https://github.com/UW-GDA/ to see the public repos.

## Github Classroom
In both 2019 and 2020, during one week, the students went to accept their assignment, and the progress bar froze. Worked for a few students, then majority of class can't get the assignment. Panic ensues.
Can make starter code visible to the student team, then show them how to Fork
In dire circumstances, just post the notebook on Slack channel
A good teaching moment.
The issue resolves itself within ~24 hours, students can use their fork or clone the assignment repo, then copy working notebook

# Jupyterhub

### Troubleshooting 

If things are not working, first try reloading the tab/window in your browser

### Default server configuration
* 2 CPU
* 8 GB RAM
* 40 GB storage

### Restarting Jupyterhub Server
* All students have the ability to stop and restart their own server on the Jupyterhub (don’t need to ask instructor or IT to help).
* File --> Hub Control Panel --> Stop My Server (wait a ~30 seconds, then start again)
* May need to restart server to fetch the latest environment (i.e., new packages added to default conda environment), or as a first troubleshooting step if you are encountering unexplained issues.

### Common Errors
* `Dask Server Error`
    * If you see this, it is likely that your server was shut down due to inactivity.  Reload the page in your browser, and restart server if necessary.
* `Failed to write *.ipynb
    * Temporary network interruption, try again
    * Check to make sure you haven't filled the disk (available storage in your home directory)
        * `cd ~ ; df .` (should be less than 100%)
* `Kernel died`
    * Likely ran out of memory, restart kernel

# Jupyter notebooks

### Disable Jupyter Notebook Warnings
```
import warnings
warnings.filterwarnings('ignore')
```

### Best practices for memory management
* Avoid duplicating large arrays ( as in “dynamically process original and plot in one command” instead of “process original, store as new array, then plot new array”)
* Avoid unnecessarily increasing bit depth (e.g., loading a `UInt16` array as `float64` quadruples memory footprint)
* Release memory from arrays that are no longer needed with `myarray = None` (see https://stackoverflow.com/a/35316944)
* Use Dask!

### Cells have strange spacing, or don't look right
* Reload in your browser to start

# Matplotlib
Review very useful FAQ here: 
* https://matplotlib.org/3.1.1/tutorials/introductory/usage.html
* https://matplotlib.org/api/index.html#usage-patterns

I recommend you use the OOI interface whenever possible (`ax.set_title(“Title”)`), not pyplot (`plt.title(“Title”)`)

I like to use `plt.subplots()`:  

Create figure object and the axes object contained by that figure:  
`f,ax = plt.subplots()`  
Call the plot method of the axes object:  
`ax.plot(x,y)`  
Call the plot function of DataFrame object, passing the axes object to the pandas DataFrame.plot() method, which will update the existing axes object.  
`df.plot(‘x’,’y’,ax=ax)`

```
f,ax = plt.subplots()
ax.plot(x,y)
df.plot(‘x’,’y’,ax=ax)

# Create 3 horizontal subplots
f,axa = plt.subplots(3)
# Plot on first axes object
axa[0].plot(x,y)
# Plot on second axes object
df.plot(‘x’,’y’,ax=axa[1])
# Loop through all axes and set to equal aspect
for ax in axa.ravel():
    ax.set_aspect('equal')
```

## Backend choice

#### `%matplotlib inline`
* Render static figures as jpg and embed in the ipynb file (will appear as binary in json)

#### `%matplotlib widget`
* Interactive figures enabling zoom/pan/selection
* Useful for rasters
* Can be buggy

Note: switching backends in the same notebook can cause issues. You may need to restart your kernel and then run the desired magic function.

Some issues updating previous figure using commands in next cell - Usually create new figure object for each cell, but maybe better solution now?

If you are working locally (not on Jupyterlab interface), best to use:
`%matplotlib notebook`

# Geopandas

### Geopandas colorbar extends beyond axes
```
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.05)
f.colorbar(im, orientation='vertical', cax=cax)
```