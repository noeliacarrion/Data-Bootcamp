![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# MySQL Basics

## Lesson Goals

In this lesson, you will be introduced to the basics of MySQL and Sequel Pro including:

* Basic database concepts and terminology.
* What are the basic MySQL data types.
* How to create and delete databases and tables with MySQL commands and Sequel Pro menu options.
* How to import data from CSV files using Sequel Pro.
* How to write queries to perform basic analyses.

## Introduction

In this lesson, we will cover the basics of how to work with MySQL. As introduced in a previous lesson, SQL refers to the Structured Query Language. SQL databases (a.k.a. relational databases) provide storage and structure to data and allow it to be accessed by users through standard operations. SQL is the formal language through which users can interact with relational databases.

There are many types of relational databases available today, with MySQL being one of the most popular open source ones. Because of this, the concepts you learn in this chapter will be illustrated using MySQL. However, these concepts are also applicable to just about every other relational database you will use in the future (PostgreSQL, SQLite, MS SQL Server, Oracle, etc.).

## Basic Database Concepts and Terminology

Before we delve into interacting with a database, let's learn some database terminology so that the concepts are not confusing when you encounter them later.

The main unit of storage in a relational database is a *table*. Tables in a database have *rows* and *columns* (or fields). Visually, a table looks similar to a spreadsheet, but with a fixed number of rows and columns (as many rows and columns as the data has).

A *query* is a question that you can ask of the data stored in one or more tables. For the database to return a result, the query must be sent via a structured language (SQL), using a standard set of commands.

Most relational databases also have *views*, which are essentially saved queries that are queryable themselves.

## SQL Data Types

When working with databases, data types help keep your data formatted properly for the operations you will be performing. There are a few basic data types you need to know about to get started using SQL. Each one is listed below along with a brief definition.

**Numeric Data Types:**

* **INT**: Integer up to 10 digits.
* **BIGINT**: Integer up to 19 digits.
* **FLOAT**: Floating decimal point number.

**Text Data Types:**

* **CHAR**: Fixed-length string with fixed length (up to 255) specified in parentheses.
* **VARCHAR**: Fixed-length string with max length (up to 255) specified in parentheses.
* **TEXT**: String with a max length of 65,535 characters.

**Date Data Types:**

* **DATE**: Date formatted as YYYY-MM-DD.
* **DATETIME**: Date and time formatted as YYYY-MM-DD HH:MI:SS.
* **TIME**: Time formatted as HH:MI:SS.

## Creating and Deleting Databases

Now that you have an understanding of the basic concepts, you are ready to learn how to create and delete databases and tables. Launch your MySQL command line now if you haven't:

```
$ mysql -u root -p
Enter password:
...
mysql>
```

To create a new database, you would use the `CREATE DATABASE` command followed by the name you would like to give the database. Let's create a database called "Apps" that will contain data about app store ratings for a variety of apps.

```sql
CREATE DATABASE Apps;
```

You can list your existing databases in the following way:

```sql
SHOW DATABASES;

+--------------------+
| Database           |
+--------------------+
| Apps               |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.04 sec)
```

Once a database exists, you can delete it by using the `DROP DATABASE` command followed by the database name.

```sql
DROP DATABASE Apps;
```

If you deleted the Apps database, go ahead and create it again using the `CREATE DATABASE` command.

## Creating and Deleting Tables

Next, we are going to perform table creation in the Apps database. But before that, you must indicate you want to work with Apps:

```sql
USE Apps;

Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
```

Now create a table called "Ratings" using the `CREATE TABLE` command. This table is going to house our data. Note that when creating a table, you must specify the fields you want in your table and also the data type for each field.

```sql
CREATE TABLE Ratings (
    ID INT,
    AppName VARCHAR(255),
    AppSize BIGINT,
    Price FLOAT,
    TotalRatings FLOAT,
    CurrentVersionRatings FLOAT,
    OverallRating FLOAT,
    CurrentVersionRating FLOAT,
    Genre VARCHAR(50)
);
```

You can view your tables in the current database by using the `SHOW TABLES` command. This should provide you with a list of all the tables currently in your database.

Once a table exists, you are able to delete it using the `DROP TABLE` command. You can follow this command with `IF EXISTS` if you want the command to make sure the table exists before deleting it. If the table doesn't exist and you try to drop it, you'll get an error, so it's usually a good idea to check.

```sql
DROP TABLE IF EXISTS Ratings;
```

If you have deleted the *Ratings* table, go ahead and create it again because we will be working with this table later.

## Using Database Management Software Instead of MySQL Command Line

Database management software such as Sequel Pro build in many common database operations in its menu such as creating and deleting databases/tables as well as importing, exporting, adding, updating, and deleting data. It's often more convenient to use database mangement software to interact with the databases than using MySQL command line.

In this section, we'll show how to use Sequel Pro to perform some basic database operations. Due to the length of the lesson, we'll skip the instructions for MySQL Workbench, which can be found in the [MySQL Workbench Documentation](https://dev.mysql.com/doc/workbench/en/).

:information_source: Despite the convenience of using database management software, we still would like you to learn MySQL commands because it's necessary for data analysts to understand what the software does behind the scene - it simply executes commands on your behalf. In particular, in your later work to query databases in Python, you'll have to use MySQL commands.

### Connecting to MySQL Server Using Sequel Pro

Launch your Sequel Pro and enter the Name, Host, and Username as shown below. If you previously set a password for your MySQL server, also enter your password.

![Sequel Pro connection via TCP/IP](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/images/sequel-pro-01.png)

Then click the `Test connection` button. If your credentials are correct you should see a `connection succeeded` message.

After testing the connection, click the `Add to Favorite` button to add a shortcut of this connection to the left.

:bulb: Tip: In addition to connecting to your MySQL server using IP (i.e. `127.0.0.1`), you can also connect via socket. You don't need the IP address if you connect via socket. This connection mode will work only if your MySQL server is installed on the local machine.

![Sequel Pro connection via socket](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/images/sequel-pro-02.png)

Click `Connect` and you'll be taken into the database where you can run your MySQL commands in the Query tab.

![Sequel Pro connection via socket](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/images/sequel-pro-03.png)

### Working with Databases Using Sequel Pro Menu Options

You can click the *Choose Database* drop down to select an existing database to work with or add a new database: 

![Selecting database in Sequel Pro](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/images/sequel-pro-04.png)

After selecting a database, you'll see its tables listed on the left. You can right click the table name to see what you can do with that table.

![Sequel Pro delete table](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/images/sequel-pro-05.png)

:exclamation: Note: Always check if you are performing operations on the intended database because otherwise you could cause permanent data loss!

:warning: Warning: Do not change or delete the system database tables such as `information_schedma`, `performance_schema`, `mysql`, and `sys`! That will break your databases! 

:warning: Warning: Be extremely careful when dropping tables and databases. Remember that what you are deleting contains information that someone else might need and be relying on.

## Importing Data into a Database

At this point, we already have our `Ratings` table in the `Apps` database whose structure is configured with the `CREATE TABLE` command. But there is still no data in that table. A very common way of getting data into your database is to import it from a file.

Data can be imported using MySQL command line or database management software. We'll use database management software in this lesson because it makes many things easier such as matching and converting data field types.

Download [apple_store.csv](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/data/apple_store.csv). This is the data file we will import.

### Importing Data in Sequel Pro

1. Select the *Ratings* table. Then click the *File* menu and select *Import...* from the dropdown.
1. Select the *apple_store.csv* file downloaded to your computer and click *Open*.
1. Sequel Pro will automatically generate the field mapping for you. Review the mappings, then click *Import*.

    ![Sequel Pro import table](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/images/sequel-pro-06.png)
    
1. Sequel Pro will now execute the import for you. 

After import is finished, you should have both the structure and content in your database table *Ratings*. Click the *Structure* and *Content* tabs in Sequel Pro to review how they are related:

![Sequel Pro imported table](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/images/sequel-pro-07.png)

![Sequel Pro imported table](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/images/sequel-pro-08.png)

### Importing Data in MySQL Workbench

1. Right-click on the Ratings table and select *Table Data Import Wizard*
1. Select or enter the file path to where the AppleStore.csv file resides on your computer and click *Next*.
1. Choose the *Use existing table: Apps.ratings* option and click *Next*.
1. Make sure the fields in the file align with the fields in the table and then click *Next*.
1. Click *Next* again to execute the import.

You should receive a message once the import is complete telling you the number of rows imported.

## Querying Data

Now that we have data populated in a table, we can start analyzing it. Let's briefly learn about some basic SQL commands and then start applying them to look at the data in our database. Below is a list of 5 basic commands and what each of them does.

- **SELECT**: Allows you to choose the specific fields you would like displayed in your query results.
- **FROM**: Allows you to specify what table in the database the data is going to come from.
- **WHERE**: Allows you to specify some conditions to filter the data.
- **ORDER BY**: Allows you to sort the data in ascending or descending order by multiple fields.
- **GROUP BY**: Allows you to specify by which fields you want to group your data.

We will cover the first four of these in this lesson, and then the focus on last one (GROUP BY) in the next lesson.

The simplest query you can write is one that just returns everything that is in a table, using just the `SELECT` and `FROM` commands.

```sql
SELECT *
FROM Ratings;
```

**ID**|**AppName**|**AppSize**|**Price**|**TotalRatings**|**CurrentVersionRatings**|**OverallRating**|**CurrentVersionRating**|**Genre**
-----|-----|-----|-----|-----|-----|-----|-----|-----
281656475|PAC-MAN Premium|100788224|3.99|21292|26|4|4.5|Games
281796108|Evernote - stay organized|158578688|0|161065|26|4|3.5|Productivity
281940292|WeatherBug - Local Weather, Radar, Maps, Alerts|100524032|0|188583|2822|3.5|4.5|Weather
282614216|eBay: Best App to Buy, Sell, Save! Online Shopping|128512000|0|262241|649|4|4.5|Shopping
282935706|Bible|92774400|0|985920|5320|4.5|5|Reference

If you want to select only specific fields or columns to display, you can specify them after the `SELECT` statement. Let's just look at AppName, Price, TotalRatings, OverallRating, and Genre.

```sql
SELECT AppName, Price, TotalRatings, OverallRating, Genre
FROM Ratings;
```

**AppName**|**Price**|**TotalRatings**|**OverallRating**|**Genre**
-----|-----|-----|-----|-----
PAC-MAN Premium|3.99|21292|4|Games
Evernote - stay organized|0|161065|4|Productivity
WeatherBug - Local Weather, Radar, Maps, Alerts|0|188583|3.5|Weather
eBay: Best App to Buy, Sell, Save! Online Shopping|0|262241|4|Shopping
Bible|0|985920|4.5|Reference

You can also filter the data based on some criterial by adding a `WHERE` clause. Let's say we are looking specifically for free apps that are rated a 4 or better. Below is how you would write a query to return just those rows.

```sql
SELECT AppName, Price, TotalRatings, OverallRating, Genre
FROM Ratings
WHERE Price = 0 AND OverallRating >= 4;
```

**AppName**|**Price**|**TotalRatings**|**OverallRating**|**Genre**
-----|-----|-----|-----|-----
Evernote - stay organized|0|161065|4|Productivity
eBay: Best App to Buy, Sell, Save! Online Shopping|0|262241|4|Shopping
Bible|0|985920|4.5|Reference
PayPal - Send and request money safely|0|119487|4|Finance
Pandora - Music & Radio|0|1126880|4|Music

If we wanted to sort our results by TotalRatings so that the most rated apps appeared at the top of our results, we would just need to add an `ORDER BY` clause to our query. Since we want the results to be descending, we would simply need to specify `DESC` after the field we wanted to sort by.

```sql
SELECT AppName, Price, TotalRatings, OverallRating, Genre
FROM Ratings
WHERE Price = 0 AND OverallRating >= 4
ORDER BY TotalRatings DESC;
```

**AppName**|**Price**|**TotalRatings**|**OverallRating**|**Genre**
-----|-----|-----|-----|-----
Instagram|0|2161560|4.5|Photo & Video
Clash of Clans|0|2130800|4.5|Games
Temple Run|0|1724550|4.5|Games
Pandora - Music & Radio|0|1126880|4|Music
Pinterest|0|1061620|4.5|Social Networking

Finally, if we wanted to limit our results to just the top 20 apps, we could incorporate another useful SQL command, `LIMIT`, as follows.

```sql
SELECT AppName, Price, TotalRatings, OverallRating, Genre
FROM Ratings
WHERE Price = 0 AND OverallRating >= 4
ORDER BY TotalRatings DESC
LIMIT 20;
```

**Note**: Different databases have different commands for limiting results to just show the top X records. If you are using a database other than MySQL, make sure to research the appropriate method for your database.

## Summary

Hopefully you're starting to see how useful it is to be able to query data with MySQL and how you are able to start with a very basic query and then layer on conditions, sorting, and limiting to arrive at the result you want. Knowing about these core concepts is going to make performing more advanced MySQL operations easier and is going to allow you to build a robust data analysis tool set.

Also, now you should have a basic understanding on how to use Sequel Pro to interact with your databases. In future lessons of this course, we will not specifically instruct you to use Sequel Pro for your work with MySQL. You can assume you'll be using Sequel Pro unless the lesson explicitly indicates otherwise.