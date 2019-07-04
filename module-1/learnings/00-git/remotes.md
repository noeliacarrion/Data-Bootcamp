![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Git Remotes

## Lesson Goals

In this lesson we will learn how to manage remote repositories in GitHub. This will enable us to work collaboratively.

## Introduction

Using remote repositories is essential to working collaboratively. In this course, your remote repositories will be hosted on GitHub. However, there are other places to host code remotely like AWS or BitBucket. 

## Listing Remote Repositories

We can use the `git remote` command to list all remote repositories.

```
$ git remote
origin
```

Origin is the default name for the origin of a repository.

We can also use the `-v` option to specify more details about the remote for the repository

```
$ git remote -v
origin  https://github.com/ironhack/data-labs.git (fetch)
origin  https://github.com/ironhack/data-labs.git (push)
```
## Adding an Alternative Remote

We might want to synchronize our repository with multiple remote Git repositories. The first one is added implicitly when we use the `git clone` command. However, we can add additional remote Git repositories and push and pull from them as needed. 

We use the format `git remote add <nickname> <url>`

```
$ git remote add personal https://github.com/ironhack/personal-data.git
$ git remote -v
origin  https://github.com/ironhack/data-labs.git (fetch)
origin  https://github.com/ironhack/data-labs.git (push)
personal	https://github.com/ironhack/personal-data.git (fetch)
personal	https://github.com/ironhack/personal-data.git (push)
```


## Fetching from a Remote

`git pull` is a combination of `git fetch` and `git merge`. Therefore, if we only want to get data about your remote projects, we can use the command
`git fetch remote`. For example:

```
$ git fetch origin
```

This command only downloads all the latest changes from this repository but does not merge them with our local copy. In order to merge as well, we use `git pull`.

## Pushing to a Remote

Since we have now defined an additional remote, we have to be more explicit when using the `git push` command. We must now specify the remote. We can also specify the branch. The format for this is: `git push <remote> <branch>`.

For example:

```
$ git push origin master 
```

## Removing a Remote

We can remove the remote that we have added and stay just with the origin remote. We do this using the following command:

```
$ git remote remove personal
```

We now check that it has indeed been removed:

```
$ git remote
origin
```
## Summary

In this lesson we learned to add and remove remotes. We also learned to push, pull and fetch when we have more than one remote. 
