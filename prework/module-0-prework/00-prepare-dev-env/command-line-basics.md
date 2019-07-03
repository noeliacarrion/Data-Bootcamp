![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Command Line Basics

## Introduction

In this lesson, we will learn some command line basics. Using the command line takes us out of the world of selecting menus and clicking buttons. Command line can appear daunting to many people but it is indispensible for technology experts because it allows them to have more control and flexibility using the computer. Mastering command line is especially important for us to accomplish complex operations on the computer which no software is available to achieve the purpose.

### Getting Started

For Mac users, go ahead opening your Terminal.

For Windows users, you will need [Git for Windows](https://gitforwindows.org/) which provides a bash window similar to the Mac Terminal. Download the **latest release** as listed in [this page](https://github.com/git-for-windows/git/releases/). Install and run Git for Windows.

:bulb: Tip: Mac is the most convenient machine for this course but you will be fine using Windows. Most of the tutorials and codes in this course will work for both Mac and Windows. In case some things differ in Windows, there will be a special note.

### List Files

When you open up the command line terminal, you will be starting in a certain location which is usually your home directory (which you can refer to with the symbol `~`). What files and folders exist at this location? Listing them all will allow you to know where you can possibly navigate to. This is where the `ls` command comes in handy. Depending on which location you are currently at, you will see output similar to the following:

```
$ ls
Applications	Documents	Library		Music		Public
Desktop		Downloads	Movies		Pictures
```

You can add options after the `ls` command by using the `-` symbol. For example, `ls -a` will also list hidden files that start with `.` in the name:

```
$ ls -a
.			.bash_sessions		.python_history		Documents		Public
..			.cups			.ssh			Downloads
.CFUserTextEncoding	.gitconfig		.viminfo		Library
.DS_Store		.grip			.yarnrc			Movies
.Trash			.ipython		Applications		Music
.bash_history		.mysql_history		Desktop			Pictures
```

And `ls -l` will list files and folders with details:

```
$ ls -l
total 0
drwx------@  4 user  staff   128 Aug  6 12:45 Applications
drwx------+  7 user  staff   224 Aug 23 15:51 Desktop
drwx------+ 17 user  staff   544 Aug 10 13:01 Documents
drwx------+ 13 user  staff   416 Aug 23 14:47 Downloads
drwx------@ 62 user  staff  1984 Aug 21 15:58 Library
drwx------+  3 user  staff    96 Aug  6 12:03 Movies
drwx------+  3 user  staff    96 Aug  6 12:03 Music
drwx------+  3 user  staff    96 Aug  6 12:03 Pictures
drwxr-xr-x+  4 user  staff   128 Aug  6 12:03 Public
```

Also, you can `ls` a specific directory or file:

```
$ ls -l /Users/user/.DS_Store
-rw-r--r--@ 1 user  staff  10244 Aug 23 11:03 .DS_Store
```

:information_source: If your username is not `user` but something else, such as `jacksparrow`, your home directory will be `/Users/jacksparrow` instead of `/Users/user`. In this case, the file `/Users/user/.DS_Store` doesn't exist but `/Users/jacksparrow/.DS_Store` does.

:information_source: `.DS_Store` is a file (macOS only) that stores custom attributes of its containing folder, such as the position of icons or the choice of a background image. Like all other files starting with a `.` in the name, `.DS_Store` is hidden from the Mac user. You do not need to worry about or interact with these hidden files.

### Working Directory Path

At times, you need to know which location you are currently at (a.k.a. the *working directory*). Use the `pwd` command to output the *absolute path* of the working directory:

```
$ pwd
/Users/user
```

### Absolute vs Relative Path

An *absolute path* is the full path of a directory or file in the file system of your machine, which always begins with a `/`. For example, `/Users/user` is the absolute path of a directory and `/Users/user/.DS_Store` is the absolute path of a file.

A *relative path* is the partial path of a directory or file relative to the working directory. Relative paths do not start with `/`. For example, if the absolute path of your working directory is `/Users/user` and there is a file named `.DS_Store` in the working directory, you can reference the file with `.DS_Store`:

```
$ pwd
/Users/user
$ ls -l .DS_Store
-rw-r--r--@ 1 user  staff  10244 Aug 23 11:03 .DS_Store
```

You can also use `.` to explicitly reference the current working directory. For instance, `.DS_Store` is equivalent to `./.DS_Store`. And `ls` is equivalent to `ls .`.

But how to reference the parent directory (directory one level up)? The answer is to use `..`. For example, if your working directory is `/Users/user`, `..` refers to `/Users`.

### Change Directories

In order to navigate to a different directory, use the `cd` command. For example:

```
$ pwd
/Users/user
$ cd ..
$ pwd
/Users
$ ls
Shared		user
$ cd Shared
$ pwd
/Users/Shared
```

### Creating and Deleting Directories

You can create new directories using the command `mkdir`. For example, `mkdir test` creates a directory named *test* in the working directory:

```
$ pwd
/Users/user
$ mkdir test
$ cd test
$ pwd
/Users/user/test
```

To create a directory at a location other than your working directory, you may specify the absolute or relative path of the target directory to be created. The example below shows how to create directories at intended locations with absolute and relative paths:

```
$ pwd
/Users/user
$ mkdir /Users/user/test/test1
$ mkdir test/test2
$ ls test
test1	test2
```

Deleting directories is done using `rmdir` or `rm -r`. `rmdir` works only for an empty directory. If the directory you attempt to delete has content (either files or sub-directories), an error will be reported. For example:

```
$ ls /Users/user/test
test1	test2
$ rmdir /Users/user/test
rmdir: /Users/user/test: Directory not empty
$ ls /Users/user/test/test1
$ rmdir /Users/user/test/test1
$ ls /Users/user/test
test2
```

Deleting a non-empty directory is using `rm -r`. The `rm` command can be used to delete both files and directories. To use it to delete a non-empty directory, you have to add the `-r` option indicating you intend to delete *recursively* (i.e. to delete the directory itself as well as all its content). Otherwise you'll hit an error:

```
$ rm test
rm: test: is a directory
```

The following command will successfuly delete the `test` directory and its content:

```
$ rm -r test
```

:bangbang: **Alert: You will not receive any warning or prompt when you use `rm -r` to remove a directory with content. The files and directories removed in command line will not be recoverable - they will simply disappear on your harddrive skipping the Trash or Recycle Bin. You should exercise caution with this command since you might accidentally delete your entire machine.**

### Root User

We can liken the root user to a game of "Simon Says". Sometimes we give the computer commands that we are not allowed to give. For example, the `reboot` command is used to restart your computer. But if you directly call this command your computer will refuse to execute:

```
$ reboot
reboot: Operation not permitted
```

To instruct your computer that you are the boss, use `sudo` in front of your command:

:exclamation: **Warning: Before you exercise the following command, save all your work to avoid data loss.**

```
$ sudo reboot
Password:
```

When being prompted for the password, enter it and hit ENTER. Your computer will restart.

:bangbang: **Alert: `sudo` must be used with caution. Most often there is a good reason why we are not allowed to perform certain actions. Understand what you are doing and always think twice before overriding the permissions system to avoid data loss or harm to your computer.**

## Summary

In this lesson we learned a few powerful commands that will enable us to navigate through our computer using the terminal. We learned how to list the contents of a folder. We learned how to move around between folders and create and delete folders. We also learned how to force the computer to perform our commands.
