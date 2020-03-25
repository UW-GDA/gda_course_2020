# Migrating from the UW Course Jupyterhub

UW Geospatial Data Analysis  
CEE498/CEWA599  
David Shean  

We will be shutting down the Jupyterhub within 30-60 days of the end of spring quarter.

All material in your home directory will be permanently deleted, so make sure you have transferred or pushed anything you might want to preserve for future use.  

## Back up all material on the Jupyterhub

I recommend you commit and push modifications to your notebooks/scripts in assignment repos. This will preserve backup copies on Github in our UW-GDA organization.

### Optional

To see total disk usage:

`cd ~ ; du -sh * ; du -sh .`

Note that each user only has 40 GB of storage space by default.  If the final line is >20 GB, I recommend you delete some large files that are no longer needed, especially zip, tif, grib or nc files that can be fetched from the original source the next time you run the notebook.

To preserve a copy of _everything_ in your home directory, including all of the temporary data files we used along the way:

`cd ~ ; tar --exclude='.cache' -czvf gda_w2020_backup.tar.gz .` 

This will create a large compressed archive. When finished, you can right-click and download that file to your local computer.

If you would like to extract:

`tar -xzvf gda_w2020_backup.tar.gz`

## Replicating course environment

1. Install conda on your local machine
1. Follow instructions to recreate and activate the uwgda2020 environment
1. Create a directory to store your scripts/material
    * `git clone` all assignment/project repos
1. Launch `jupyter lab`
1. :tada:
