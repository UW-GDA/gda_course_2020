# Student weekly workflow

## Accepting Assignments
1. Join the new Slack channel for the lab
1. Click on the link to the Github Classroom assignment
1. Accept the assignment invitation
1. Wait for progress bars to complete (should take ~10-20 seconds)
    * If this fails
1. Click on the resulting link to go to your assignment repository (now has your github username appeneded)
1. Enjoy the lab:
    * Read instructions!
    * Write/modify code
    * Git add/commit as you make progress to record "checkpoints" in your work

## Submitting Completed Assignments

### 1. Prepare Jupyter notebook for submission
* Replace `%matplotlib widget` with `%matplotlib inline`
* From the top menu, click Kernel -> Restart Kernel and Run all Cells…
* Your figures are now statically rendered jpg and may appear smaller.
    * You can resize defaults by adding `plt.rcParams['figure.figsize'] = [10, 8]` after the  `import matplotlib.pyplot as plt` line, or tweaking each figure size in inches.
    * When you’re satisfied, Run All Cells again.  
* Save the notebook by clicking the little floppy disk icon.  

### 2. Git workflow
* In a Jupyterlab terminal, `cd` to your assignment repo
* Use standard git add/commit/push workflow
    * `git add completed_notebook.ipynb`
    * `git commit -m 'Meaningful commit message'`
    * `git push`
* Go to your Github repo, click on the notebook file to render, and verify that everything looks good!

### 3. Canvas submission
* Go to the Canvas assignment page, and submit the url to your Github repo

#### Instructor review
1. Follow the link you submitted on Canvas, review code/answers, create a “feedback” branch on the repo, and open a Pull Request (PR) for inline comments/discussion.
1. If your submission is a Jupyter notebook, cell-level comments will be added using ReviewNB
1. Final grade assigned via Canvas

## Reviewing instructor feedback
1. Open your assignment repo on Github
1. Click the Pull Request tab near the top of the page
1. Click the Pull Request named Feedback
1. Click the purple ReviewNB button
1. Review the cell-level and general comments from instructor
    * Respond to questions/comments
    * Follow up on anything that is unclear
    * If instructor made a mistake during grading, let them know!
1. Merge the Pull Request on github to indicate that you've reviewed the instructor's feedback and interactive discussion is complete.