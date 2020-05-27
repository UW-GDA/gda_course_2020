# Jupyter Notes
UW Geospatial Data Analysis  
CEE498/CEWA599  
David Shean  

These are a set of loosely organized notes, tips, tricks and gotchas for Jupyter resources (Jupyterhub, Jupyter lab and Jupyter notebooks) used during the course.  Additional notes on initial setup and weekly workflow can be found in the [GDA instructor resources](https://github.com/UW-GDA/gda_2020/tree/master/resources/instructors).

Additional UW eScience Hackweek resources on initial Jupyterhub setup and navigation:
https://icesat-2hackweek.github.io/learning-resources/preliminary/jupyterhub/

## Jupyterhub

### Default 2020 student server configuration
* 2 CPU
* 8 GB RAM (increased mid-quarter)
* 40 GB storage

### Troubleshooting 

If something is not working or the text in notebook cells looks strange or "cut off", first try reloading the tab/window in your browser.

### Restarting Jupyterhub Server
* All students have the ability to stop and restart their own server on the Jupyterhub (don’t need to ask instructor or IT to help).
* File --> Hub Control Panel --> Stop My Server (wait a ~30 seconds, then start again)
* May need to restart server to fetch the latest environment (i.e., new packages added to default conda environment), or as a first troubleshooting step if you are encountering unexplained issues.

### Common Errors
* `Dask Server Error`
    * If you see this, it is likely that your server was shut down due to inactivity.  Reload the page in your browser, and restart server if necessary.
* `File Save Error for *.ipynb` or `Failed to write *.ipynb`
    * Temporary network interruption, dismiss and try manually saving
    * Check to make sure you haven't filled the disk (available storage in your home directory)
        * `cd ~ ; df .` (should be less than 100%)
* `Kernel died`
    * Likely ran out of memory, restart kernel

## Jupyter notebooks

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
