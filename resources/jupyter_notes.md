# Jupyter Notes
UW Geospatial Data Analysis  
CEE498/CEWA599  
David Shean  

These are a set of loosely organized notes, tips, tricks and gotchas for Jupyter resources (Jupyterhub, Jupyter lab and Jupyter notebooks) used during the course.  Additional notes on initial setup and weekly workflow can be found in the [GDA instructor resources](https://github.com/UW-GDA/gda_2020/tree/master/resources/instructors).

Additional UW eScience Hackweek resources on initial Jupyterhub setup and navigation:
https://icesat-2hackweek.github.io/learning-resources/preliminary/jupyterhub/

# Jupyterhub

## Initial Instructor Setup

#### Work with UW-IT template 
See sample for 2020 here: https://github.com/UW-GDA/uwgda-image
Most of the user-level customization is found in the `binder` subdirectory.
We used a `dev` branch to submit Pull Requests with modifications (e.g., adding a new package) and then merged into `master` after tests completed. 

#### Add any core utilities to `apt.txt`
This includes common command line tools like `wget` or text editors like `vim`. Sample:    
https://github.com/UW-GDA/uwgda-image/blob/master/binder/apt.txt

#### Create a shared conda environment 
Include all packages that will be needed for the course, with version numbers if desired.
Sample: https://github.com/UW-GDA/uwgda-image/blob/master/binder/environment.yml
Can update this list throughout the course, and continuous integration will automatically rebuild and deploy the updated image.  

#### Add any custom Jupyter lab extensions
Add useful interactive visualization tools (pyviz, leaflet), Dask integration, etc.  
Sample: https://github.com/UW-GDA/uwgda-image/blob/master/binder/postBuild
See available extensions: https://github.com/topics/jupyterlab-extension 

## Default 2020 student server configuration
* 2 CPU
* 8 GB RAM 
* 40 GB storage

## Logging out
Please try to remember to shut down your server and log out of the Jupyterhub when you're done for the day. This will help save money (we'd like to avoid paying for cloud computing resources while you're sleeping), and provides a clean start the next time you log in, which can help avoid various issues listed below.

## Troubleshooting

### 1. Reload the tab in your browser
* Can resolve issues with notebook cells that appear strange or "cut off"
* If you have unsaved changes, save the notebook, then reload

### 2. Restart Jupyterhub Server
* All students have the ability to stop and restart their own server on the Jupyterhub (don’t need to ask instructor or IT).
* **File --> Hub Control Panel --> Stop My Server (wait a ~30 seconds, then start again)**
* After image is updated (e.g., new packages added to default conda environment), all users will need to restart their server to see changes.

### 3. Review the list of common errors and solutions below

### 4. Post a message to #IT_help on the class Slack workspace
* Important to post to public channel, as other students can chime in to help, and if this is a larger issue, confirm similar experiences
* Provide detailed report, with copy/paste of error messages, screenshots, etc. to help diagnose
* Course instructor and IT help will provide assistance

## Common Jupyterhub Errors
#### `Kernel Restarting`
 * Likely ran out of memory. 
 * Can "Restart Kernel and Run up to selected cell" to restore state
 * Remember, closing a notebook tab in JupyterLab interface doesn't actually shut down the kernel! If you have opened/run many notebooks during a session, you may start to experience performance issues. 
 * To remedy, click the "Running Terminals and Kernels" button (square inside a circle) on the left panel. It will show you all of the kernels  that are running. Shut down any that you no longer need.

#### `Dask Server Error`
 * If you see this, it is likely that your server was shut down due to inactivity. Reload the page in your browser, and log back onto the Hub.

#### `File Save Error for *.ipynb` or `Failed to write *.ipynb`
 * Temporary network interruption, dismiss and try manually saving
 * Check to make sure you haven't filled the disk (available storage in your home directory)
     * `cd ~ ; df .` (should be less than 100%)
     * If disk is full, delete some files from `/home/jovyan`

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
