![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# List Comprehensions

## Lesson Goals

* Learn about the concept of combining storage with iteration.
* Learn how list comprehensions combine storage and iteration in an efficient way.
* Learn how to incorporate conditional logic into list comprehensions.
* Learn how to construct list comprehensions with multiple for loops.
* Add conditional logic to multi-loop list comprehensions.
* Learn some use cases for list comprehensions.

## Introduction

As you continue improving your Python programming skills, you will encounter useful ways to combine some of the basic concepts you learned earlier in the program. In this lesson, we will learn about list comprehensions. List comprehensions combine the concepts of storage in data structures, iteration, and even conditional logic into an efficient form.

## Combining Storage and Iteration

The main idea behind list comprehensions is iterative storage. In some of the previous lessons, we have encountered scenarios where we had to create an empty list and iterate through a for loop appending a value to the list at the end of each iteration.

```python
lst = []

for i in range(10):
    lst.append(i)

print(lst)

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

In this example, we created an empty list and for every number in the range, we appended that number to the list as we encountered it.

## List Comprehensions

A list comprehensions is a way to streamline that logic into a single line of Python code. Instead of creating an empty list and filling it with the `append` method, the list comprehension's square brackets cause the results returned to be packed into a list. Below is what the previous example looks like as a list comprehension.

```python
lst = [i for i in range(10)]
print(lst)

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

As you can see, we get the same result from less code, which is generally a good thing. Inside the square brackets, we are requesting the value for every value in that range.

## Adding Conditions to List Comprehensions

We can also incorporate conditional statements into our list comprehensions. When adding conditions, they need to be placed after the appropriate for loop in order to exclude results that do not satisfy our condition. The example below returns every value in a range but only if the value is greater than or equal to 5.

```python
lst = [i for i in range(20) if i >= 5]
print(lst)

[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
```

## Multiple For Loops in List Comprehensions

Sometimes we encounter more complex situations where multiple loops are required. For example, suppose you had some nested lists whose values you wanted to unpack into a single list. Using regular lists and for loops, we would do that as follows.

```python
lst_lst = [[1,2,3], [4,5,6], [7,8,9]]

lst = []

for x in lst_lst:
    for y in x:
        lst.append(y)

print(lst)

[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

List comprehensions provide us with a very efficient way of handling these cases as well. In order to construct a list comprehension with multiple for loops, we would request the final result that we want followed by the series of loops. This may seem a little confusing because we are asking up front for the result that comes at the end of the last loop, but after writing them for a while, you will find that it helps you think about the result you want and then how to get it.

```python
lst_lst = [[1,2,3], [4,5,6], [7,8,9]]

lst = [y for x in lst_lst for y in x]
print(lst)

[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Note that the order of the for loops within the list comprehensions is exactly the same as the order you would have written it with regular for loops. You will be tempted to write it backwards (`[y for y in x for x in lst_lst]`), but that will not return the result we want. So just remember that the for loop order is the same within a list comprehension as it would be outside the list comprehension.

## Adding Conditions to Multi-Loop List Comprehensions

List comprehensions can handle quite a bit of complexity. We can even incorporate conditional logic into list comprehensions that contain multiple loops. For example, suppose we had a list of lists such as the one in the example below and we wanted to extract a list of even numbers that appear in nested lists shorter than 4 elements long. We could achieve this with a list comprehension containing two for loops and two conditional statements as follows.

```python
lst_lst = [[1,2,3,4,5], [6,7,8], [9,10]]

lst = [y for x in lst_lst if len(x) < 4 for y in x if y % 2 == 0]
print(lst)

[6, 8, 10]
```

Note that the condition for each for loop comes directly after the for loop it applies to. This ability to handle complex logic with such efficiency makes list comprehensions a very powerful tool to have in your arsenal.

## Practical Uses for List Comprehensions

### Reading Multiple Files

One use case where list comprehensions come in handy is when data is split across multiple files. For example, suppose we had a data directory that contained several CSV files (among other files), each with the same information (columns) for separate groups or divisions. We could use a list comprehension with an `endswith('.csv')` condition in it to get a list of just the CSV files in that directory. We could use another list comprehension to have Pandas read each of those files and then the `pd.concat` method to combine them all into a single data set that we can analyze as follows.

```python
import os
import pandas as pd

file_list = [f for f in os.listdir('./data') if f.endswith('.csv')]
data_sets = [pd.read_csv(os.path.join('./data', f)) for f in file_list]
data = pd.concat(data_sets, axis=0)
```

We did all this with three lines of Python code, which is pretty amazing!

### Selecting Data Frame Columns Based on Conditions

Another use case would be selecting data frame columns based on a condition that they have in common. The example below reads our vehicles data file, uses the `_get_numeric_data` method to retrieve all numeric columns, and then uses a list comprehension to return just the columns that have a mean greater than 15.

```python
data = pd.read_csv('vehicles.csv')

selected_columns = [col for col in data._get_numeric_data() if data[col].mean() > 15]
print(selected_columns)

['Year', 'Fuel Barrels/Year', 'City MPG', 'Highway MPG', 'Combined MPG', 'CO2 Emission Grams/Mile', 'Fuel Cost/Year']

```

## Summary

In this lesson, we learned all about list comprehensions. We began the lesson with the concept of combining storage and iteration, upon which list comprehensions are based. We then introduced list comprehensions as a method for efficiently combining storage and iteration. From there, we went beyond basic list comprehensions, adding conditional logic and looking at list comprehensions with multiple for loops. We ended the lesson with taking a look at two of the many ways that list comprehensions can be helpful to us in our data wrangling and analysis work.
