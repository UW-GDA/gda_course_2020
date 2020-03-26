# Weekly Procedures for Instructor

## Prepare notebook (including solutions)

## Prepare student notebook
* Manually duplicate, delete code/answers for student exercises

## Prepare a new "starter code" repository in the GDA organization
1. Click green "New" button to create new repo
1. Fill in details:
    * Repository name: 02_Python_Core_Packages
    * Private 
    * Initialize with README.md
    * Add .gitignore for Python
1. Clone the repo to the Jupyterhub
1. Add the student notebook(s), sample data, and any other relevant files
    1. Git add, commit, push
1. On Github, update README.md with relevant instructions
1. On Github, create a new feedback branch
    * Note March 2020, Github Classroom now has an option to do this when creating assignment

## Prepare Github Classroom assignment:
1. Go to https://classroom.github.com/classrooms/
1. New Individual Assignment
Name 02_Python_Core_Packages
Private
Find starter repo
Post assignment invitation url to Slack
If updates are needed:
git remote add upstream https://github.com/my_class_org/assignment_starter
git pull upstream master

## Create assignment in Canvas
### First Week
20 points
02_Python_Core_Packages
Add the following description:
Accept the github assignment here: [insert assignment invitation url]. When completed, submit the url to your repo here on canvas.
Select url submission
Due date Friday midnight

### Subsequent Weeks
Duplicate previous assignment
Udpdate Name
Update url
Update 

## Post to Slack
* Create new channel: 02_Python_Core_Packages
* Post link to Github Classroom assignment ()
* Post link to Canvas assignment for submission

## Teach it!
* Open slack channel
* Click on link
* Open terminal on Jupyterhub, cd to `~/labs` subdirectory
* git clone 
* Work through interactive examples
* Clean up and commit the notebook
* Push to preserve 

# Grading
* Open Canvas SpeedGrader, click on url pointing to student's Github repo (opens new browser tab)
* Optional: quickly view rendered notebook to make sure figures are properly included (`%matplotlib inline` before submission)
* Github Pull Request workflow:
In student repo, create a new “feedback” branch (if it doesn’t already exist)
Click on a file that the student modified
Add a space or modify code for all relevant locations
Commit with message “feedback”
Repeat for additional files
Open Pull Request with message “Feedback”
Click on the “Files changed” tab
Create comments by clicking + for highlighted lines
Add any final comments

## ReviewNB
In student repo, review the commit history, click on the last commit that instructor made before distributing assignment (the commit that the student accepted through Github Classroom)
Check out the code (“Browse Files”) at that commit
Create a new branch called “feedback”
Compare master with feedback branch, Open a new PR
Open ReviewNB and comment

Add final grade on canvas Speed Grader

Students review comments
Create an account on https://www.reviewnb.com/
From comments on the notebook in the Github pull request, click on the “Reply via ReviewNB” link (or find the repo through RiviewNB interface)
Click on the “Pull requests” tab under the repo (may need to switch to feedback branch?)
Review the “Discussion” tab, and if desired, respond to specific comments
Review (and if desired, respond) to general comments on Github pull request
Close the pull request (no reason to merge, as I didn’t change any code)

## Post solutions notebook to Github

### Send Slack message

Hi @channel,
I finished reviewing your Lab02 notebooks. FantasticPlease review the Pull Request in your repo with ReviewNB app:
* Open the repo on github
* Click the Pull Request tab near the top of the page
* Click the Pull Request named Feedback
* Click the purple ReviewNB button
* See discussion

If you attempted the extra credit with standalone Python script, see inline comments on the script file in the pull request directly on Github.

Let me know if anything is unclear, and feel free to respond directly to my comments if you’d like.

Please merge the pull request after you have reviewed - this will let me know that you can see my feedback on ReviewNB/Github.

