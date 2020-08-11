# Initial Setup for Instructor

We use multiple platforms during this course, which required some prep before the quarter started.

## Slack
#### Create a new Slack workspace
1. Go to https://slack.com/create
1. Recommend naming with course name and year:
    * Geospatial Data Analysis: W2020
    * uwgda2020.slack.com
1. Optional: add a unique icon (useful if you are logged into many workspaces on Desktop app)
1. For a 10-week course with ~15 students, the free plan was sufficient. For larger classes, you might hit the 10K message limit during the quarter, in which case, some early messages will not longer be visible.

#### Set up workspace
1. Add private `#admin` channel for TAs, IT staff
1. Add public `#it_help` channel for students to get help with Jupyter issues
1. Add public `#project` channel for discussion of student projects (will see more activity later in quarter)
1. On the `#general` channel, post a new welcome message and create a quick-reference list of links to the various resources that will be used throughout the course (Jupyterhub url, Github Organization url, etc.).  Pin this by clicking the three dots in upper right corner o fthe message and selecting "Pin to channel".  Add a note that students can always find this list by clicking the Pin icon near top of the channel.
1. Review and modify additional workspace settings and configuration on the Slack website
1. Can use "Manage members" to set TAs or other course admin to "Workspace Admin" if desired.

#### Invite students
1. Can do this with list of email addresses or click the "Get an invite link to share" and send to email list
1. Set default channels to join (add the new channels you created above)

## Github
If you don't already have a Github account, create one: https://help.github.com/en/github/getting-started-with-github/signing-up-for-a-new-github-account

## Github Organization
#### Create a new Organization
1. Click the + icon in upper right hand corner of Github landing page after logging in.
1. Choose the "Free" option (can sign up for edu account later)
1. Use a simple name for the Organization (e.g., "UW-GDA")
1. Select "My personal account" so you can maintain control over the Organization
#### Invite members
1. Students will create accounts and send you their github usernames
1. Invite them to the organization (from the "People" tab)

### Settings
1. Base permissions -> None
1. Repostory creation -> enable Private

### Create teams
These will have different priveleges, and can be selectively assigned to repos in the Organization
1. Admin team: "w2020_admin"
1. Instructor team: "w2020_instructors"
1. Student team: "w2020_students"

#### Solutions repo
1. Create a Private repo called "w2020_solutions", where you will post solutions each week for student review
1. Go to "Settings" tab (upper right) and "Manage access"
1. Add teams:
  * instructor team with role "Write"
  * admin team with role "Maintain"
  * student team with role "Read"

## Github Classroom
1. Create new classroom (big green button)
1. Select your Github Organization
1. Give the classroom a descriptive name with year "Geospatial Data Analysis W2020"
1. Invite TAs
1. Send invitation to students to join
1. Skip integration with LMS (Canvas is listed, but UW-IT has not connected)
1. Upload list of student names, email or github usernames 

## Jupyterhub
See Initial Setup section in general [Jupyter Notes](../jupyter_notes.md)

## ReviewNB
* https://github.com/marketplace/review-notebook-app
* Install in Github Organization
