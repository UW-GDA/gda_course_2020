# Weekly Procedures for Instructor

## Prepare solutions notebook
* Master notebook with all code, markdown
* Use a '*_solutions.ipynb' filename

## Prepare student notebook
* Manually duplicate the solutions notebook and rename, removing '_solutions'
* Delete desired code or output

*Note: More sophisticated approaches can use tags to programatically remove code*

## Prepare a new "starter code" repository in the GDA organization
1. Click green "New" button to create new repo
1. Fill in details:
    * Repository name: 02_Python_Core_Packages
    * Private 
    * Initialize with README.md
    * Add .gitignore for Python
1. Clone the repo to local or Jupyterhub (wherever student notebook was prepared)
1. Add the student notebook(s), sample data, and any other relevant files
    1. git add, commit, push
1. Optional: update README.md with relevant instructions
1. On Github, create a new feedback branch
    * *Note as of March 2020, Github Classroom now has an option to do this when creating assignment*

## Prepare Github Classroom assignment:
1. Go to https://classroom.github.com/classrooms/ and select the appropriate class
1. New Individual Assignment
1. Provide a name that is consistent with above: 02_Python_Core_Packages
1. Private (otherwise, students can see each other's answers before deadline)
1. Add starter code
    * Copy/paste the starter code repo name "02_Python_Core_Packages", then select
    * Select "Import starter code using source importer" (haven't tried template option)
1. Don't select deadline (set this on Canvas)
1. Don't Grant admin repo access
1. Enable feedback pull requests
    * Untested, did this for Week10, and students could not see markdown files in thier accepted assignment repo

## Create Canvas assignment
#### First Week
* Type: Assignment
* Name: 02_Python_Core_Packages
* Due: midnight no the following Friday
* Points: 20
* More Options:
> Accept the github assignment here: [insert assignment invitation url]. When completed, submit the url to your repo here on canvas.
    * Submission Type: Online, Website URL
* Save and Publish

#### Subsequent Weeks
* Duplicate previous assignment
    * Udpdate Name
    * Update Assignment url
    * Update Due Date

## Post to Slack
* Create new channel: 02_Python_Core_Packages
* Post link to Github Classroom assignment
* Post link to Canvas assignment for submission

#### Optional: Updating assignment repo
* If you discover errors or need to update the assignment materials after distribution...
* Can be messy with Jupyter notebooks, after students start modifying the assignment notebook, especially if they are new to git
* If updates are absolutely needed, students can do the following:
    * `git remote add upstream https://github.com/UW-GDA/02_Python_Core_Packages`
    * `git pull upstream master`

## Teach it!
During class:  
* Open slack channel
* Follow Github Classroom Assignment link
* Click "Accept this assignment"
* Open terminal on Jupyterhub, cd to `~/labs` subdirectory
* `git clone [assignment_url]`
* From file browser, open the relevant notebook(s)
* Work through interactive examples
* Optional: preserve interactive demo
    * Clean up and `git commit` the notebooks
    * `git push` to preserve in the starter code repo

# Grading
### Canvas
* Open Canvas SpeedGrader
* Sort by time of submission
* Click on url pointing to student's Github repo (opens new browser tab)
* Optional: quickly view rendered notebook in Github to make sure figures are properly included (`%matplotlib inline` before submission)
    * If not, send message on Slack

### Github
* Github Pull Request workflow:
    * If feedback branch does not exist:
        * Click on "commits" header
        * Find the last instructor commit (before students modified), click on the `<>` icon next to the github hash (e.g., "f2aca22") to browse files at that commit
        * Create a new "feedback" branch
            * Click on button that says "Tree: f2aca22c94"
            * In dropdown, type "feedback" and hit enter
    * Create a new Pull Request:
        * Click "New pull request" button
        * Under "base:" select the new "feedback" branch
        * Under "compare:" select master branch
        * Should create new dialog
        * Enter "Feedback" in the title (may need to replace existing commit message)
        * Click green "Create pull request" button
* Once the Pull Request has been created
    * Wait a few seconds, and the review-notebook-app bot should add a new cell in the Conversation with a purple button for ReviewNB
        * Click that to open in ReviewNB, see instructions below
    * Can add general comments in the PR discussion

### ReviewNB (https://www.reviewnb.com/)
* With the Pull Request open in ReviewNB, click the Changes tab
* This will render the original notebook on the left, and the student's updated notebook on the right, with new code or output highlighted in green
* To comment on a particular cell/output, hover the mouse, then click the `+` icon to the left of the cell
    * Can enter text as you would on Github, with markdown and other formatting
    * Click the green button to save the comment
* When review is finished, click to 

### Canvas
* Add final grade in SpeedGrader
* Respond to any Canvas comments

## Post solutions notebook to Github solutions repo
* Push the completed notebook with instructor solutions

## Send Slack message
* Let student's know grading is done, and provide link to solutions notebook
* Remind students about weekly procedures and ask them to merge the feedback PR when finished