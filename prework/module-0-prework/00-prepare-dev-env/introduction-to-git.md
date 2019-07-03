![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Git and GitHub

## Git

### Introduction

Git is a version control system. Version control is important in technology development because it keeps track of all the changes you and your collaborators have made to the files in your project. If some of the changes you and your collaborators have made are not compatible, Git allows the team to discover the conflicts and resolve them. If some changes are found problematic after they are made, one can also revert to the previous correct version of the code. By using Git, you and your collaborators can work in parallel without worrying about one's work will mess up others'.

### Basic Commands

So far we have encountered the following Git commands:

* `git --version` (showing current Git library version)

* `git config --global user.name <name>` (configure the current Git user name)

* `git config --global user.email <email>` (configure the current Git user email)

Below is a table of some additional basic Git commands:

|Git Command|Description|
|---|---|
|`git init`|Create empty Git repo in specified directory. Run with no arguments to initialize the current directory as a git repository|
|`git clone <repo>`|Clone repo located at <repo> onto local machine. Original repo can be located on the local filesystem or on a remote machine via HTTP or SSH.|
|`git status`|List which files are staged, unstaged, and untracked.|
|`git diff`|Show unstaged changes between your index and working directory|
|`git add <directory>`|Stage all changes in <directory> for the next commit. Replace <directory> with a <file> to change a specific file.|
|`git commit -m "<message>"`|Commit the staged snapshot, but instead of launching a text editor, use <message> as the commit message.|
|`git log`|Display the entire commit history using the default format. |
|`git push <remote> <branch>`|Push the branch to <remote>, along with necessary commits and objects. Creates named branch in the remote repo if it doesn’t exist.|
|`git pull <remote>`|Fetch the specified remote’s copy of current branch and immediately merge it into the local copy.|
|`git branch`|List all of the branches in your repo. Add a <branch> argument to create a new branch with the name <branch>.|
|`git checkout -b <branch>`|Create and check out a new branch named <branch>. Drop the -b flag to checkout an existing branch.|
|`git merge <branch>`|Merge <branch> into the current branch.|

For the complete list of Git commands, refer to the [Git cheat sheet](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet) by Atlassian.

Memorizing a list of Git commands doesn't make much sense and that's why we keep this lesson short. It is more helpful if you use those commands in authentic task contexts. That is exactly what you will be doing in the next lesson.

## GitHub

### Introduction

GitHub is a website for hosting code repositories. Using GitHub allows for collaboration between developers.

#### Creating a Repository

We can create a new repository by selecting "New repository from the drop-down menu in the top right corner.

![New Repository](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/images/new-repo.png)

After creating the repository, select a name for your new repository and make sure to check the box for adding a README file.

#### Cloning a Repository

To clone a repository, we must obtain the remote URL. We can navigate to the repository in GitHub and click on the "Clone or download" link on the top right. We then copy the URL and use it in the `git clone` command.

![git clone](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/images/git-clone.png)

#### Pull Requests

Sometimes we want others to review our work before we merge our branch into the master branch. This is why we need pull requests. After pushing our new branch, we can create a pull request to merge this branch with the main branch. Other collaborators may review your work and approve or reject your request.

To create a pull request, we click on the "New pull request" button in the repository's main page. We then select which branch will be merged into which branch.

#### Issues

When working with code created by others, we might find problems with the code. We might also have suggestions for improving the code. We can create an issue in the repository to report this to the other collaborators.

The issues tab appears on the top left of the page next to the "Code" tab.

![issues](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/images/issues.png)

## Summary

In this lesson we learned about git, a version control system. We learned several basic git commands that allow us to create a repository, clone a remote repository, commit and push our code and create branches.
We also learned about GitHub. We learned about the different creating and cloning a repository, creating a pull request and creating issues.
