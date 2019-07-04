![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Introduction to Pandas

## Lesson Goals

* Learn about Pandas data structures and how to extract data from them.
* Convert other Python data structures to Pandas DataFrames.
* Apply Pandas mathematical functions to data frame fields.

## Introduction

As a data analyst with Python in your tool kit, one of the libraries you will use most often will be Pandas. Pandas is a useful library that makes data wrangling, transformation, and analysis easier and more intuitive. In this lesson, we will learn about Pandas data structures and how to apply some basic math functions to them.

As with Numpy in the previous lesson, you must import Pandas to be able to use it. Just like Numpy is typically aliased to `np`, Pandas is usually aliased to `pd`. Let's import both of them so that we can use them in this lesson.

```python
import numpy as np
import pandas as pd
```

Now that both libraries are imported, we can begin using them.

## Pandas Data Structures

The primary data structures in Pandas are *Series* and *DataFrames*. A series is an indexed one-dimensional array where the values can be of any data type. Let's create a series consisting of 10 random numbers using the Pandas `Series()` method.

```python
a = pd.Series(np.random.random(10))
print(a)

0    0.799343
1    0.534252
2    0.810355
3    0.928851
4    0.748286
5    0.762151
6    0.774291
7    0.890176
8    0.267933
9    0.248028
dtype: float64
```

As you can see, this generated an indexed array of random numbers. Just as with other Python data structures, we can reference the elements of this array by their indexes.

```python
a[0]

0.7993425723285518

a[5]

0.7621507835939337
```

The other type of data structure, DataFrames, are two-dimensional indexed structures where each column can be of a different data type. DataFrames are very similar to spreadsheets and database tables, and they are one of the most useful data structures you will be working with as a data analyst.

DataFrames can be generated using the Pandas `DataFrame` method as follows. We are also going to assign specific column names to each column in the data frame by passing a variable named `colnames` with a list of column names to the `columns` argument.

```python
colnames = ['Column1','Column2','Column3','Column4','Column5']
df = pd.DataFrame(np.random.random((10,5)), columns=colnames)
df
```

![DataFrame](../../../static/images/dataframe.png)

We can reference each of the columns in a data frame directly by the column name as follows.

```python
df['Column1']

0    0.742603
1    0.578973
2    0.906471
3    0.013889
4    0.440874
5    0.358352
6    0.196321
7    0.345590
8    0.058615
9    0.708301
Name: Column1, dtype: float64
```

This returns a series consisting of the values in the first column of our data frame. If we wanted to extract just the first three columns of our data frame, we would need to include the column names in a list inside the square brackets (so there would be two sets of square brackets).

```python
df[['Column1','Column2','Column3']]
```

![Three Column DataFrame](../../../static/images/dataframe-three-columns.png)

When we extract more than one column, it returns the results in a data frame since a series is only one-dimensional.

## Converting Other Data Structures to DataFrames

We can also convert data we receive in other Python data structures into data frames so that we can work with them more intuitively. For example, suppose we had a list of prices that houses sold for recently and we wanted to get those into a data frame. We could do that by applying the `pd.DataFrame` method to the list of prices.

```python
lst = [208500, 181500, 223500, 140000, 250000, 143000, 307000, 200000, 129900, 118000]

price_df = pd.DataFrame(lst, columns=['SalePrice'])
price_df
```

![Sale Price DataFrame](../../../static/images/sale-price-dataframe.png)

The list was converted into a one-column data frame with a column name of SalePrice.

What if we had more then just one list of data? What if we had a list of lists where each sublist in the master list contained information about the sale of a house (the lot area, neighborhood, year built, quality score, and final sale price)? We can apply the same `pd.DataFrame` method to that list of lists and Pandas will create a data frame with columns based on each index in the sublists.

```python
lst_lst = [[8450, 'CollgCr', 2003, 7, 208500],
           [9600, 'Veenker', 1976, 6, 181500],
           [11250, 'CollgCr', 2001, 7, 223500],
           [9550, 'Crawfor', 1915, 7, 140000],
           [14260, 'NoRidge', 2000, 8, 250000],
           [14115, 'Mitchel', 1993, 5, 143000],
           [10084, 'Somerst', 2004, 8, 307000],
           [10382, 'NWAmes', 1973, 7, 200000],
           [6120, 'OldTown', 1931, 7, 129900],
           [7420, 'BrkSide', 1939, 5, 118000]]

colnames = ['LotSize','Neighborhood','YearBuilt','Quality','SalePrice']
pd.DataFrame(lst_lst, columns=colnames)
```

![House DataFrame](../../../static/images/house-dataframe.png)

List are not the only data structures that can be converted to a data frame. Data frames can also be created from data stored in a dictionary. Suppose we had a dictionary where the values contained the same information we had in our list of lists, but the keys of the dictionary consisted of the names of each house.

```python
house_dict = {'Baker House': [7420, 'BrkSide', 1939, 5, 118000],
              'Beazley House': [14115, 'Mitchel', 1993, 5, 143000],
              'Dominguez House': [14260, 'NoRidge', 2000, 8, 250000],
              'Hamilton House': [6120, 'OldTown', 1931, 7, 129900],
              'James House': [11250, 'CollgCr', 2001, 7, 223500],
              'Martinez House': [9600, 'Veenker', 1976, 6, 181500],
              'Roberts House': [9550, 'Crawfor', 1915, 7, 140000],
              'Smith House': [8450, 'CollgCr', 2003, 7, 208500],
              'Snyder House': [10084, 'Somerst', 2004, 8, 307000],
              'Zuckerman House': [10382, 'NWAmes', 1973, 7, 200000]}
```

If we use the same approach as with the list of lists, Pandas would by default return a column for each house.

```python
pd.DataFrame(house_dict)
```

![Dictionary to DataFrame](../../../static/images/dict-to-dataframe.png)

This is not the format we want for our data. Instead, we want each house represented as a row and the attributes of the houses represented as columns. There are (at least) two ways to transform the data frame to the format we want. Both methods below will return the same result - a data frame with houses as rows and house attributes as columns.

```python
# You can transpose the result and adjust the column names.
house_df = pd.DataFrame(house_dict).transpose()
house_df.columns = colnames

# Or you can add the from_dict method and specify 'index' for the orient parameter, and then adjust your column names.
house_df = pd.DataFrame.from_dict(house_dict, orient='index')
house_df.columns = colnames
```

![Dictionary to DataFrame](../../../static/images/transposed-dictionary-dataframe.png)

## Applying Mathematical Functions to Data Frames

Like Numpy, Pandas also has some built-in mathematical functions that you can apply to series and data frames. Let's take a look at some of the basic ones.

```python
# Total price of all houses sold
house_df['SalePrice'].sum()

1901400

# Average lot size of houses sold
house_df['LotSize'].mean()

10123.1

# The latest year a house in the data set was built
house_df['YearBuilt'].max()

2004

# The eariliest year a house in the data set was built
house_df['YearBuilt'].min()

1915
```

## Summary

In this lesson, we learned about the two basic Pandas data structures - Series and DataFrames. We also learned how to reference the elements of a series and how to extract specific columns from a data frame. From there, we converted other Python data structures, such as lists and dictionaries, into Pandas DataFrames. Finally, we briefly looked at some basic mathematical functions that can be applied to a data frame's columns. We will be using all of these concepts and math functions as we progress through the program.
