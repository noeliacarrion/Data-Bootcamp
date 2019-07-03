![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Challenge: Install MySQL and Sequel Pro

## Introduction

Structured Query Language (SQL) is the most prevalent database language in the world allowing one to perform database operations such as storing, retrieving, updating, and deleting data. In this course you will learn [MySQL](https://www.mysql.com/), a popular genre of SQL which is free. After mastering MySQL, you should have no problem in picking up other SQL genres such as MS SQL (by Microsoft), PostgreSQL, and SQLite because these languages are similar in a large part.

In order to learn MySQL, you need to install it first on your computer. In this challenge, you will install MySQL and a database management application called Sequel Pro (or MySQL Workbench for Windows).

:bulb: Tip: SQL Databases are also known as the Relational Databases because they are based on the relational algebra theory. The opposite of SQL is NoSQL a.k.a. the Non-Relational Databases. The main difference between SQL and NoSQL is how they store data - the latter does not require a specific structure of the data in order to store them. An example of the NoSQL databases is [MongoDB](https://www.mongodb.com/).

## MySQL

![MySQL](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/images/mysql.svg)

### Install MySQL

#### Install with Homebrew (Mac)

To install MySQL with Homebrew, run the following command in the terminal:

```
$ brew install mysql
```

#### Install with Installation Package (Mac and Windows)

You can also [download the MySQL Community Server](https://dev.mysql.com/downloads/mysql/) and follow the [official installation documentation](https://dev.mysql.com/doc/refman/8.0/en/installing.html) to install. Make sure to download the latest version `8.x.x` for the OS platform you are using.

:warning: For Mac users, it is recommended to use Homebrew to install MySQL. The official MySQL installation package is known to have issues in working properly for some users. If you installed with the official installation package and encounter issues, uninstall it then re-install with Homebrew.

:warning: For Windows users, make sure to download the **Installer MSI**, not the ZIP Archive. Also, in the Windows Service step during the installation process, check **"Start the MySQL Server at System Startup"** so that you don't have to manually start MySQL every time your computer is restarted.

![MySQL Workbench Windows Service](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/images/mysql-workbench-windows-service.png)

### Is It Working?

#### Testing in Mac

Type `mysql -u root -p` in the terminal to test your MySQL installation, where `-u root` means your MySQL username is `root` and `-p` means a password is required.

When being prompted to enter password, type your password if you have set it during installation. If you haven't set the password, it means your password is still empty so simply hit the ENTER key.

```
$ mysql -u root -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.11 Homebrew

Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```

If you see the welcome message and the `mysql>` prompt, congratulations for successfully installing MySQL!

#### Testing in Windows

It is largely similar in Windows to test the MySQL command as in Mac. The differences are:

1. In order for Git Bash to find MySQL, you need to add the MySQL executable location to the Windows path. To do this, launch Git Bash and run:

	```
	$ cd ~
	$ echo 'export PATH=/c/Program\ Files/MySQL/MySQL\ Server\ 8.0/bin/:$PATH' >> .bash_profile
	```

	* Remember in the previous lesson you already did something with `.bash_profile`? In that lesson you created a `python3` alias in this file. This time, we add `/c/Program Files/MySQL/MySQL Server 8.0/bin/` (where the MySQL application can be found) to the Windows path. If you execute `echo .bash_profile`, you should see its content as below:

	```
	alias python3=python
	export PATH=/c/Program Files/MySQL/MySQL Server 8.0/bin/:$PATH

	```

1. Quit Git Bash then open it again. 

1. To launch MySQL in Git Bash, type:

	```
	$ winpty mysql -u root -p
	Enter password: ******
	Welcome to the MySQL monitor.  Commands end with ; or \g.
	Your MySQL connection id is 25
	Server version: 8.0.12 MySQL Community Server - GPL

	Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.

	Oracle is a registered trademark of Oracle Corporation and/or its
	affiliates. Other names may be trademarks of their respective
	owners.

	Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

	mysql> 
	```

	If you see something similar to the above, well done in installing MySQL in Windows!

:bulb: Tip: To use MySQL in Git Bash, you are required to amend the Windows path and use `winpty` to call `mysql`. Alternatively, you can use the MySQL Command Line application that comes with your MySQL Server to run MySQL commands without amending the Windows path. However, you will not be able to use Git or Python in MySQL Command Line. You can launch MySQL Command Line in **Programs > MySQL > MySQL Server 8.0 > MySQL Server 8.0 Command Line**.

### Changing MySQL Password

If you didn't set the password for your MySQL server (e.g. if you installed with Homebrew), it is a good practice to add a password to the `root` user in order to protect your database. In MySQL command line, type the following command:

```
mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY '<new-password>';
Query OK, 0 rows affected (0.07 sec)
```

:warning: Note: Remember to change `<new-password>` to your desired password.

:warning: Note: Every MySQL command must end with a semicolon (`;`). 

After changing the password, exit MySQL command line and re-launch:

```
mysql> exit;
Bye

$ mysql -u root -p
Enter password:
mysql>
```

When being prompted to enter the password, enter your new password then hit ENTER.

:bangbang: **Alert: Please save your MySQL username and password in a safe place where you know where to find.**

### Starting MySQL

After installing MySQL, the `mysql` service should have automatically started. However, if your MySQL is not running for any reason when you try to access MySQL command line, you will see the following error:

```
$ mysql -u root -p
Enter password:
ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/tmp/mysql.sock' (2)
```

If this happens, you may start the `mysql` service manually.

#### Starting MySQL in Mac

If you installed MySQL with Homebrew, use the following way to start MySQL:

```
$ brew services start mysql
==> Successfully started `mysql` (label: homebrew.mxcl.mysql)
```

If you used the MySQL installation package to install MySQL, the best way to manage it is using the MySQL Launch Daemon which you can find in your System Preferences:

![MySQL Launch Daemon](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/images/mysql-daemon.png)

In the daemon, select the MySQL instance you installed and click Start MySQL Server.

![MySQL Launch Daemon](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/images/mysql-daemon2.png)

Read the [official documentation](https://dev.mysql.com/doc/refman/8.0/en/osx-installation-launchd.html) on MySQL Launch Daemon for more information.

#### Starting MySQL in Windows

Your MySQL should automatically start every time your Windows starts if you selected the "Start the MySQL Server at System Startup" option while installing the MySQL Community Server. If you didn't select that option, however, simply re-install MySQL Community Server.

## Sequel Pro

:exclamation: **Note: Windows users, please skip this section because Sequel Pro is for Mac only. You will be using [MySQL Workbench](https://www.mysql.com/products/workbench/) which you already have when you installed MySQL Community Server.**

![Sequel Pro](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/images/sequel-pro.png)

It is inconvenient to use MySQL command line to interact with the database. Therefore, we will install a database management application to make our future work easier. For Mac users, we recommend you to install [Sequel Pro](https://www.sequelpro.com/). 

### Install Sequel Pro

Sequel Pro can be installed with Brew Cask. Run:

```
$ brew cask install sequel-pro
```

:exclamation: Note: At the time this lesson was written, the latest release of Sequel Pro has some bugs. If your Sequel Pro keeps crashing similar to what [this post](https://github.com/sequelpro/sequelpro/issues/2699) describes, uninstall `sequel-pro` and install **`sequel-pro-nightly`** instead:

```
$ brew cask uninstall sequel-pro
$ brew cask install sequel-pro-nightly
```

`sequel-pro-nightly` contains the latest development of the Sequel Pro where those bugs have been fixed. Those fixes haven't been integrated in the `sequel-pro` release or the official installation package at the time this lesson was written.

Alternatively, Sequel Pro can also be installed using the official installation package. Check out the [Sequel Pro official download page](https://sequelpro.com/download) and follow the documentation in that page.

### Connecting Sequel Pro to Database

1. Locate Sequel Pro in your Applications and launch the software. You will see the following connection window:

    ![Sequel Pro Connection Window](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/images/install-sequel-pro-01.png)

1. Enter the Name, Host, Username, and Password as shown in the following screenshot. Use the password you set for your MySQL in previous steps. Click "Test connection". You should see a message that says `Connection succeeded`.

    ![Sequel Pro Connection Configuration](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/images/install-sequel-pro-02.png)

1. Click "Add to Favorites" so that you can reuse this MySQL connection in the future.

    ![Sequel Pro Connection Add Favorite](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/images/install-sequel-pro-03.png)

1. Now click "Connect". You'll be connected to your localhost MySQL server.

    ![Sequel Pro Connect](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/images/install-sequel-pro-04.png)

Nice work! Now you have installed Sequel Pro and can use it to interact with your MySQL database!

## Summary

Databases are extremely important for data analysts because they allow them to work with data in efficient, reliable, and consistent ways. In this challenge we installed MySQL, a popular database technology used to store, retrieve, and manipulate data. We also installed Sequel Pro, a database management software used to interact with MySQL databases.

Seqeul Pro is not the only database management tool. A good alternative is [MySQL Workbench](https://www.mysql.com/products/workbench/). Sequel Pro and MySQL Workbench provide similar sets of functionalities. Some people may prefer MySQL Workbench because it allows them to accomplish certain advanced tasks such as migrating MS SQL databases to MySQL. In this lesson we recommend Sequel Pro to Mac users because it's more suitable for beginners. For Windows users, however, you'll be using MySQL Workbench because Sequel Pro doesn't support Windows.