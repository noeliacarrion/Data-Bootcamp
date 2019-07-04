![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Importing and Exporting Data

## Lesson Goals

* Learn how to import and export delimited files with Pandas.
* Learn how to import and export JSON files.
* Learn how to read data from a database.
* Learn how to write data to a database.

## Introduction

No analytics tool operates in a vacuum. Most of the time, the systems that generate the data are not the ones where analysis of that data is conducted. Because of this, we must have a way to obtain data from external data sources, load it into Pandas, and also be able to export data or our results for further use or presentation. In this lesson, we will cover ways to import data from, and export data to, a variety of formats and destinations using Pandas.

## Importing and Exporting Delimited Files

One of the most common places where data originates are delimited files. Most analytics applications have the ability to read and process delimited files, so they are a popular way to pass information from one system to another. There a few common file formats you are likely to see out in the real world.

* Comma-separated variable (CSV) files
* Tab-delimited files
* Pipe-delimited files

Pandas provides us with the ability to import any of these using the `read_csv` method. For files delimited with characters other than commas, we just need to specify the type of delimiter via the method's `sep` parameter so that Pandas knows how it should separate the values.

```python
# Import comma-separated variable file
data = pd.read_csv('vehicles/vehicles.csv')

# Import tab-delimited file
data = pd.read_csv('vehicles/vehicles_tab.txt', sep='\t')

# Import pipe-delimited file
data = pd.read_csv('vehicles/vehicles_pipe.txt', sep='|')
```

Exporting data as delimited files is just as easy. Instead of using the `read_csv` method, you use `to_csv`.

```python
# Export comma-separated variable file
data = pd.to_csv('vehicles/vehicles.csv', index=False)

# Export tab-delimited file
data = pd.to_csv('vehicles/vehicles_tab.txt', sep='\t', index=False)

# Export pipe-delimited file
data = pd.to_csv('vehicles/vehicles_pipe.txt', sep='|', index=False)
```

Note that we set the `index` parameter to False. If we did not do that, it would export the data frame with an extra column containing its indexes. Since the indexes have no meaning to us in this case, we are going to exclude them from our export.

## Importing and Exporting Excel

We can also import and export Microsoft Excel spreadsheets with Pandas. The way to do this is similar to how we imported and exported delimited files, but instead of `read_csv` and `to_csv`, we will use the `read_excel` and `to_excel` methods.

```python
data = read_excel('vehicles/vehicles.xlsx')

data.to_excel('vehicles/vehicles.xlsx', index=False)
```

## Importing and Exporting JSON

Another common format for importing and exporting data is JSON. JSON stands for Javascript Object Notation, and it allows you to format data in intuitive ways so that it can be easily read and processed. We can use Pandas to read and write JSON files as follows.

```python
data = pd.read_json('vehicles/vehicles.json', orient='records')

vehicles.to_json('vehicles/vehicles.json', orient='records')
```

Note that we set the `orient` parameter to `'records'` in our code examples above. We did this because our JSON file was structured as a list of dictionaries where each dictionary represented a complete record of data. When working with JSON files in Pandas, the way the data is organized is going to dictate the value you pass to the `orient` parameter. Below are a few other common ways that JSON files can be structured and the corresponding value you should pass to the `orient` parameter for each one.

* `'split'`: Dictionary containing indexes, columns, and data.
* `'index'`: Nested dictionaries containing {index:{column:value}}.
* `'columns'`: Nested dictionaries containing {column:{index:value}}
* `'values'`: Nested list where each sublist contains the values for a record.
* `'table'`: Nested dictionaries containing schema and data (records).

**Challenge:** Try exporting the data passing each of these values to the `orient` parameter. Open each of the files in a text editor and note the differences in structure.

## Reading Data from Databases

In addition to reading data from various types of files, Pandas also provides us with the ability to read data from MySQL databases. To do so, we need to import the `pymysql` library and the `create_engine` function from the `sqlalchemy` library.

```python
import pymysql
from sqlalchemy import create_engine
```

We must then call the create_engine function and pass it the string below, replacing `username` and `password` with the actual username and password for the MySQL database on your local machine. We will assign the result to a variable called `engine`.

```python
engine = create_engine('mysql+pymysql://username:password@localhost/publications')
```

From there, we can use the Pandas `read_sql_query` function, pass it a SQL statement, and specify that it is to run that statement on the engine connection we created to our MySQL database. In the example below, we are querying all records from the employee table in our publications database.

```python
data = pd.read_sql_query('SELECT * FROM publications.employee', engine)
```

## Writing Data to Databases

Once you have data in a data frame and you have your MySQL database connections saved to the `engine` variable, writing the data to a table in the database is pretty straightforward. You can use Pandas' `to_sql` method and specify the table name you want to give the data set, the database connection, what you want to happen if the table already exists (replace, append, fail, etc.) and whether you want to include or exclude the indexes.

```python
data.to_sql('employee2', engine, if_exists='replace', index=False)
```

If you refresh the publications database, you should now see a table named "employee2."

## Summary

In this lesson, we covered multiple ways to import data into and export data out of Pandas. First, we learned how to read and write delimited files (csv, tab-delimited, and pipe-delimited). Then we learned how to read and write Excel and JSON files, and finished up the lesson with reading and writing to MySQL databases with the help of the `pymysql` and `sqlalchemy` libraries.