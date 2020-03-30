# Shell and Github: Demo notes
UW Geospatial Data Analysis  
CEE498/CEWA599  
David Shean  

## Preparation and discussion
- Make sure all students are on Jupyterhub whitelist (UW netid)
- Distribute link to course Jupyterhub, have students start server
- Discuss remote computing - underlying infrastructure, computer somewhere in Google data center in CA or OR
- Close tab in Jupyterlab - demonstrate persistence
- Ask about OS? Anybody using Linux? All of you!
- Distribute assignment link through Github classroom

# Basic git/Github workflow
1. Clone assignment locally:  
`git clone https://github.com/UW-GDA/01-shell-github-dshean.git`
    * Alternatively, create a new repo called gda_test on Github:
    ```
    git clone https://github.com/dshean/gda_test.git  
    cd gda_test  
    ls -l
    ```
2. Pick a text editor
    * Discuss text editors, pick one for command line, or use Jupyterlab text editor
3. Edit `README.md` and add your name
4. Commit the change
```
git status
git add README.md
git status
git commit -m "Added my name to README.md"
git status
```

### Discussion of local vs origin
* Open web browser to view origin repo on Github
* `git push`
* Refresh page, verify README.md was updated

### Edit README.md on Github, commit directly

### Pull changes to local repo
* `git pull`
* `git log`

# Add a new script to the repo

### Create a new text file
* Discuss extensions (.sh vs. .txt or .py)
* `vim myawesomescript.py`
* Add some lines:
    ```
    #! /usr/bin/env python
    print("Pancakes rule!")
    ```

### Commit the change
```
git status
git add myawesomescript.py
git status
git commit -m "Added myawesomescript.py"
```

### Try to execute script, doesn't work
`./myawesomescript.py`

### Check permissions
`ls -l ./myawesomescript.py`

### Change permissions
```
chmod +x myawesomescript.py
ls -l myawesomescript.py
./myawesomescript.py
```

### Commit permission change
```
git status
git diff myawesomescript.py
git add myawesomescript.py
git status
git commit -m "Change permissions on myawesomescript.py"
```

### Review log, master is ahead of origin
```
git log
git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit
```

### Push to origin
```
git push
git status
```

### Review log, both origin and master are same
```
git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit
```

# Other topics to discuss
* Tab completion
* Shell history (use up arrow)
* Discuss filesystem
    * Output from `which ls`
    * Go to /
    * Explore /bin
* Discuss executables
* `$PATH`
* bits, bytes
* for loop
    ```
    for i in solutions.txt words README.md
    do
        ls $i
    done
    #One line:
    for i in solutions.txt words README.md; do ls $i; done
    ```

# Introduce assignment
* `more words`
* `file words`
* How are we going to count the number of words? Online search term discussion
    * `wc -l words`
* How to submit answers: create a new text file, copy your command and output to a new text file
* `more GLAH14_tllz_conus_lulcfilt_demfilt.csv`