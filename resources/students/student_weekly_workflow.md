# Student weekly workflow

## Accepting Assignments
1. Join the new Slack channel for the lab
1. Click on the link to the Github Classroom assignment
1. Accept the assignment invitation
1. Enjoy the lab:
    * Read instructions
    * Write/modify code
    * Git add/commit as you make progress to record "checkpoints" in your work

## Turning in Assignments
1. Before the due date (midnight the following Friday)
1. If turning in Jupyter notebook, see section below on "Prepare Jupyter notebook for submission"
1. Go to Canvas, and submit the github url for your assignment repo

1. I will follow the Canvas link, review your code/answers, create a “feedback” branch on your repo, and open a Pull Request (PR) as a placeholder for inline comments/discussion.
1. I will add comments using ReviewNB or Github PR conversation.
1. I will assign a grade on Canvas
1. Review my comments using ReviewNB or the Github PR conversation. You can directly respond to follow up on anything that is unclear or answer my questions.
1. Merge the Pull Request on Github so I know that you've reviewed my comments.

### Prepare Jupyter notebook for submission
Please replace `%matplotlib widget` with `%matplotlib inline`.  Then, from the top menu, click Kernel -> Restart Kernel and Run all Cells…
Your figures may appear smaller.  You can resize defaults by adding `plt.rcParams['figure.figsize'] = [10, 8]` after the  `import matplotlib.pyplot as plt` line, tweaking the figure size in inches as desired.
When you’re satisfied, Run All Cells again.  Save the notebook by clicking the little floppy disk icon.  Then in the terminal, git add, commit, push.  Go to your github repo and click on the notebook file to render, and verify that the figures appear.
I am using ReviewNB extension for Github to review your submissions, and the figures have to be embedded for this approach to work. 
