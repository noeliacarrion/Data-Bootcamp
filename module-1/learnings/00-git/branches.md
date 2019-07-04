![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Git Branches

## Lesson Goals

In this lesson we will learn about the typical workflow that is followed when working with branches

- Creating a new branch and switching to other branches.
- Listing all branches and ensuring that we are pulling all branches from the repository.
- Going over the workflow of adding, committing and pushing. 
- Creating pull requests in GitHub.

## Introduction

In the previous module, we touched briefly on branching. However, in this module, we will look at branching more in depth. Branching is most useful when you want to work on encapsulated changes and merge them into your main branch. As a developer, this allows you to have greater control over the introduction of changes to your code base over time. 

![branching](../../../static/images/branching.png)

In the diagram above we see a typical workflow. A new branch is created and, in the meantime, other developers continue to work on the master branch while another developer may work on feature A. Eventually the branch will be merged back into the master branch.

## Creating New Branches

The first step to working with new branches is to create a new branch. Creating a new branch is done by using the `git branch` command. If we want to create a new branch and immediately switch to the new branch as well, we use the `git checkout` command with the option `-b`.

Since we have forked the `data-labs` repository, we will use this repository as an example. We will make a new branch in this repository:

```
$ git checkout -b newfeature
Switched to a new branch 'newfeature'
```

## Switching Branches

We can switch to another existing branch using the `git checkout` command.

For example, we can switch back to our master branch.

```
$ git checkout master
Your branch is up to date with 'origin/master'.
```

## Listing All Branches

Listing all branches can be done by typing `git branch`

```
$ git branch
  master
  * newfeature
```

However, this command will only display branches that you have created or worked on locally. If you want to display all branches, even ones you have not worked on, type `git branch -a` instead.

```
$ git branch -a
* master
  newfeature
  remotes/origin/HEAD -> origin/master
  remotes/origin/editingreadme
  remotes/origin/master
  remotes/origin/newfeature
```
## Pulling From All Branches

In order to get the latest changes in all branches (including ones you have not worked on locally) use the `git pull` command.

```
$ git pull
remote: Counting objects: 3, done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), done.
From https://github.com/ironhack/data-labs
 * [new branch]      editingreadme -> origin/editingreadme
Already up to date.
```

This command will get all changes from all branches since it is a combination of two commands: `git fetch` and `git merge`. The `git fetch` command gets all branches from the repository.

## Adding and Committing Changes

After we make some changes to our new branch, we can add new files and commit with one command. We use the `git commit` command with the option `-am` and add a commit message. We should start with the `git add .` command if we have added completely new files to our branch.

```
$ git add .
$ git commit -am "first commit of newfeature branch"
[newfeature dfc9b4f] first commit for newfeature branch
 1 file changed, 2 insertions(+)
```


## Pushing the Code

When you try to push your branch, using the `git push` command, you will see the following error:

```
$ git push
fatal: The current branch newfeature has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin newfeature
```

This means that git does not know where to push your code to. You will need to declare it using the command shown in the error message.

```
$ git push --set-upstream origin newfeature
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 348 bytes | 348.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/ironhack/data-labs.git
 * [new branch]      newfeature -> newfeature
Branch 'newfeature' set up to track remote branch 'newfeature' from 'origin'.
```

If you see a message similar to the one above, this means that you have successfully pushed your branch to the repository.

## Merging Branches

Once we have finished working on a branch, we can merge it to another branch (or to our master branch) locally and then push the combined branch to our repository in GitHub. For example, in order to merge our new branch to master, we first navigate to the master branch and then merge using the `git merge command`.

```
$ git checkout master
$ git merge editingreadme
Updating af3f5ff..5c3dd87
Fast-forward
 README.md | 3 +++
 1 file changed, 3 insertions(+)
```

If there were no conflicts, you should see the message above (we will cover conflicts in one of the next lessons).

## Pull Requests

Pull requests are important for collaboration since they enable reviewing the code before merging. Other developers can add comments and approve or reject your pull request. 

To create a new pull request, we first commit our branch and push it to GitHub. We go to the main page of our repository on GitHub and select "New pull request" on the top left.

Your base branch should be the master branch (in some cases you might want to use another branch as the base branch). Your compare branch should be the branch containing your latest changes.

![pull request](../../../static/images/pull-request.png)

Like with merging, we should hopefully have no conflicts. If we do have conflicts, then they must be fixed. This will be addressed later in this module.

## Summary

In this lesson we have covered using branches to work collaboratively with other developers. We learned how to create branches, switch branches and list all the branches in our repository. We also learned how to use branches to create smaller code changes and then either merge or pull request to integrate the changes.