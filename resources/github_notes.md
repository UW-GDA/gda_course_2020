# Github and Github Classroom Notes
UW Geospatial Data Analysis  
CEE498/CEWA599  
David Shean  

These are a set of loosely organized notes, tips, tricks and gotchas for git and Github resources used during the course.  Additional notes on initial setup and weekly workflow can be found in the [GDA instructor resources](https://github.com/UW-GDA/gda_2020/tree/master/resources/instructors).

There are many good resources on git and Github on the web.  See the [Week 01](https://github.com/UW-GDA/gda_2020/tree/master/modules/01_Shell_Github) reading assignment and demo.  

Additional UW eScience Hackweek resources on initial Github setup and navigation: https://icesat-2hackweek.github.io/learning-resources/preliminary/github/

## First time login
`git config --global user.name "Matt Damon"`  
`git config --global user.email "email@example.com"`

## Improved git log formatting
`git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit`  
*Note: Can add as alias to ~/.gitconfig*

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
See the instructor resources on the weekly Github Classroom workflow for assignment distribution.

#### Issues accepting assignments
In both 2019 and 2020, during one week, the students went to accept their assignment, and the progress bar froze. Worked for a few students, then majority of class can't get the assignment. Panic ensues.
Can make starter code visible to the student team, then show them how to Fork
In dire circumstances, just post the notebook on Slack channel
A good teaching moment.
The issue resolves itself within ~24 hours, students can use their fork or clone the assignment repo, then copy working notebook

