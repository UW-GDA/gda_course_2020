# Migrating from the UW Course Jupyterhub

UW Geospatial Data Analysis  
CEE498/CEWA599  
David Shean  

We will be shutting down the course Jupyterhub within 30-60 days of the end of the quarter.

You will no longer be able to access your server, and all of the data you stored on the hub will be permanently deleted.

I recommend that you log in to the hub and review everything stored in your home directory.  A lot of these are temporary files that can be deleted and fetched again from original sources in the future if necessary.  But perhaps you want to preserve copies of these files anyway.

You can use the following strategies to back up your course materials to the cloud and/or transfer to your local machine.

## Push git repos to github

Fortunately, you've been religiously pushing your lab/project notebooks all quarter (right?).  So those materials are already backed up as long as you maintain you Github account (the GDA organization will persist indefinitely).  

But maybe there are a few scratch notebooks or intermediate data files that you want to preserve.  You can add these to existing repos, or create a new repo and push, but remember that large data files (>10 MB) don't belong in Github repos!

## Archive and download your entire home directory

The easiest (smartest?) approach may be to compress and archive _everything_ in your home directory, including all of the temporary files. Then download this archive and store locally (or move to Google Drive or other cloud storage platform).

1. On the hub, open a terminal and run the following command to check your total disk usage:  
`cd ~ ; du -sh * ; du -sh .`
1. If the final line of the output from the above command is >20 GB, I recommend you delete some large files that are no longer needed, especially zip, tif, grib or nc files that can be fetched from the original source the next time you run the notebook.
   * Note that each user has 40 GB of storage space in our 2020 hub configuration.  
1. Run the following command to create a [`tar.gz` archive](https://en.wikipedia.org/wiki/Tar_(computing)) of your home directory:  
`cd ~ ; tar --exclude='.cache' -czvf gda_w2020_backup.tar.gz .` 
   * This may take a while depending on volume and number of files
1. When finished, navigate to the top-level home directory in the Jupyterlab file browser, right-click on the `gda_w2020_backup.tar.gz` file and download to your local computer.
1. To extract (optional):  
`tar -xzvf gda_w2020_backup.tar.gz`

## Reproducing the course environment

To be able to run the same code on your local machine, you will need to replicate the environment that we used on the Jupyterhub. Fortunately, this is easy to do!

1. See notes on the top-level README on how to launch an ephemeral session in the cloud (click the "binder" button): https://github.com/UW-GDA/gda_2020#reproducing-the-gda-course-environment
1. To reproduce locally, you just need to install conda, create the uwgda2020 environment, activate and launch `jupyter lab`: https://github.com/UW-GDA/gda_2020/blob/master/modules/10_Conda_Pangeo_Dask/conda.md#how-to-replicate-the-gda-juptyerhub-environment
1. :tada:
