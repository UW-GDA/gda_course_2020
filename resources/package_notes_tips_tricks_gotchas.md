# Notes, tips, tricks, gotchas and other useful information
UW Geospatial Data Analysis  
CEE498/CEWA599  
David Shean  

These are a set of loosely organized notes, tips, tricks and gotchas for tools used during the course.  

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
