# Instructor lessons learned

## Slack
* Essential
* No more email, organized discussions, students can post direct or group messages
* Create new channel for each module/lab
* Create a private #admin channel for instructors/TAs/IT
* Create a public #it_help channel
* Remind them that discussing on Slack is not cheating!
* They will often answer each other's questions
* Can review Slack posts at end of quarter for class participation grade (some students don't speak up in class, but are more active on Slack)
* Set boundaries for yourself (use status)

## Github
* Always a major challenge for new users
* Keep it simple - just focus on single-user workflow (clone, add, commit, push) 

## Github classroom
* Simplifies assignment distribution
* Handles forking behind the scenes, enables simple single-user git/github workflow

## Jupyterhub
* Centralized, indentical environment
    * Don't support individual student environment, OS, hardware!
* Admin control panel is useful for monitoring recent usage, restarting student servers if they cannot do so themselves
* Memory limits may be a problem

## Jupyterlab
* Filesystem with icons is good stepping stone to navigating via terminal
* Right-click and download is simple and effective
* Right-click on markdown file, then Open With -> Markdown Preview
* Set up two panes side-by-side (e.g., notebook and rendered markdown file)

## Jupyter notebooks
* Many good resources out there:
    * https://jupyter4edu.github.io/jupyter-edu-book/
    * 
* Teach basic shortcuts to execute cells (shift-Enter), add cells (a or b) and move around in the notebook.

### Using notebooks for problem sets
* Provide a good introduction
* Sample code is good, but make them think or interpret resulting output
* Don't just tell them what to do!
    * Can walk them through steps, provide links to documentation, recommend methods
    * Undergrads may be used to more "plug and chug" problems, while grad students can 

## Large datasets
* Try to fetch data dynamically

## General
* Students benefited from ~15-30 minutes at the beginning of lab to discuss code, answers, issues and questions. Useful before diving into new material. Lots of discussion when I wasn't present, often hard to get them to stop when the time came :). It was critical that they had already attempted to work through the exercises independently (or with recent Slack discussions).
* Throughout the quarter revisit imposter syndrome, emphasize we are all coming in with different backgrounds/experience, learning together
* The grading workflow worked with 15 students, but won't necessarily scale. Can use `nbgrader` or similar for automated grading support
* The transition to remote/online instruction in weeks 8-10 was relatively smooth
   * The students had already established relationships, and the general informal atmosphere of the class was already established. Breakout rooms encouraged discussion.

