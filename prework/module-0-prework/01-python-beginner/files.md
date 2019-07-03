![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Challenge: Working with Files in Python

## Lesson Goals

In this lesson you will learn how use Python to work with files, including:

* How to identify, navigate, change, and create directories.
* How to write content to files.
* How to read files and print content to the console.
* How to work with csv files and perform basic analyses.

## Introduction

The last topic we are going to cover in the Python Beginner module is working with files. As a data analyst, working with files is going to be something that you do regularly, so it is critical that you are adept at finding them, reading data from them, and writing data to them.

## Navigating Directories and Finding Files

One of the foundational components of every modern computer is a file system. The file system is where files are stored and organized into directories, often visually represented through a graphical user interface as folders. The specific place in a directory where a file is located is called its *path*. For instance, if you had a file named *file.txt* on your Desktop, the file's path might be `/Users/username/Desktop/file.txt` on a Mac or `C:\Desktop\file.txt` on a Windows machine.

There is a tool in Python that makes navigating directories and locating files much easier than it would be otherwise. It is a library called os (which stands for operating system), and you can access it by using the `import` command as follows.

```python
import os
```

Libraries contain additional functions and methods that can help you more easily accomplish what you need to do. Now that we have imported the os library, we can easily do things like find out our current working directory by calling its `getcwd()` method.

```python
os.getcwd()
```

```text
'/ironhack/01-python-beginner'
```

The output you get will almost certainly be different than the output above, but now you know where you currently are in your machine's file system. To change your current working directory, you can use the `chdir()` method and enter the path where you would like to be in the parentheses.

```python
os.chdir('/Users/username/Desktop')
os.getcwd()
```

```text
'/Users/username/Desktop'
```

Another useful method in the os library is the `path.join()` method. This method lets you put together a path from strings or strings stored in variables.

```python
root = 'C:'
level_1 = 'ironhack'
level_2 = 'module_0'
level_3 = 'python-beginner'
level_4 = 'data'

os.path.join(root, level_1, level_2, level_3, level_4)
```

```text
'C:/ironhack/module_0/python-beginner/data'
```

What if we wanted to create a new folder? The os library can help us do that as well. The `path.exists()` method can check to see if a folder with the name we pass it currently exists in the current directory, and if it doesn't, the `makdirs` method can create a folder with that name.

```python
folder_name = 'new_folder'

if os.path.exists(folder_name) == False:
    os.makedirs(folder_name)
```

Now that we know how to navigate directories and create file paths and folders, we are ready to move on and start working with files.

## Writing to Files

One of the main things you can do with files is write to them. We can write to a file in Python by using a `with open() as` combination to open the file for writing (`"w"`), and then the `write` method to actually write content to that file.

```python
with open("example.txt", "w") as f:
    f.write("Hello World! \n")
    f.write("How are you? \n")
    f.write("I'm fine.")
```

The code above will create a file in your current directory called "example.txt" and will write three lines of text to it. The `\n` you see at the end of the first two lines in the code is how you tell the program to go to the next line.

## Reading Files

Now that we have learned how to write to a file, let's read the contents of the file we just created. We can open the file for reading in a similar way that we did for writing, but we will need to change the `"w"` inside the `open()` function to an `"r"` (for "reading"). We can then use the `readlines` method to read all the lines in the file and a simple for loop to print each of the lines.

```python
with open("example.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line)
```

```text
Hello World!

How are you?

I'm fine.
```

## Reading Data from a CSV File

One of the most common file formats used by data analysts are comma-delimited files with a .csv file extension. In these files, commas are used to separate values from one another and new lines are used to separate records from each other. In this section, we are going to read data from a csv file and perform some simple calculations.

Now, download the [*weight_height.csv*](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/data/weight_height.csv) data source. This file contains reported vs. actual weight and height for various men and women. If you open this file in a text editor (not Excel), you'll find the first few lines look like:

```text
gender,actual_weight,actual_height,reported_weight,reported_height
M,77,182,77,180
F,58,161,51,159
F,53,161,54,158
M,68,177,70,175
F,59,157,59,155
M,76,170,76,165
M,76,167,77,165
...
```

As you can see, the different values in the file are separated by commas and each line represents a single person. 

Before working with this downloaded file in Python, we need to figure out its absolute or relative path in order to reference it correctly with code. To figure out the absolute path of the file, use Terminal to navigate to the directory where you downloaded the file, then execute:

```
$ echo `pwd`/`ls weight_height.csv`
```

Then save the absolute path printed from the above command for the next steps. 

Alternatively, if you run Python from the same directory where you downloaded the file, you can use the relative path of either `weight_height.csv` or `./weight_height.csv`.

Now that we have the file's path, let's extract the data from this file and put it into a format that we can work with. First, we are going to create an empty list called `data`. Then we are going to read our csv file, convert each line to a list by leveraging the `split()` method, and append it to our `data` list.

```python
data = []

with open("<file path>", "r") as f:
    lines = f.readlines()
    for line in lines:
        data.append(line.split()[0].split(","))
```

:information_source: Replace `<file path>` with the absolute or relative path of the downloaded CSV file.

In this example, we used the `split()` method twice. The first time, it was used to turn each line into a list, but the content of each list was just a comma-separated string, which we would not have been able to do anything with. In order to access the values we need to access, we needed to reference the 0th element in each list (the comma-separated string) and then split the values wherever there was a comma.

Once we are done with this, our `data` list is actually going to be a list of lists, that looks like this.

```text
[['gender',
  'actual_weight',
  'actual_height',
  'reported_weight',
  'reported_height'],
 ['M', '77', '182', '77', '180'],
 ['F', '58', '161', '51', '159'],
 ['F', '53', '161', '54', '158'],
 ['M', '68', '177', '70', '175'],
 ['F', '59', '157', '59', '155'],
 ['M', '76', '170', '76', '165'],
 ['M', '76', '167', '77', '165'],
 ['M', '69', '186', '73', '180'],
 ['M', '71', '178', '71', '175']
 ...
]
```

We can access any of the values in this list of lists via indexing. For example, if we wanted to extract just the headers, we would get them as follows.

```python
data[0]
```

```text
['gender',
 'actual_weight',
 'actual_height',
 'reported_weight',
 'reported_height']
```

If we wanted to get the gender of the first individual in our data set, we would do that by referencing the list that represents that line (`[1]`) and then referencing the first element in that list (`[0]`).

```python
data[1][0]
```

```text
'M'
```

Now that we have our data in a navigable data structure, let's do some analysis. Let's say we wanted to compare the average actual heights for all the individuals in our data. To do this, we would need to extract all the actual height values. We can do that by using a simple for loop to append all the heights (as integers) to a `heights` list.

```python
heights = []

for person in data[1:]:
    height = int(person[2])
    heights.append(height)
```

Once we have all the heights in a single list, we can sum them up and then divide by the total number of values to get the average.

```python
avg_height = sum(heights)/len(heights)
print(avg_height)
```

```text
170.14835164835165
```

This is great, but what if we wanted to compare the average heights of males vs. females? To do this, we would use a similar approach, but we would also incorporate conditional logic into our for loop so that when the gender of the person is male, the height is appended to a `male_heights` list and when the gender is female, it gets appended to a `female_heights` list.

```python
male_heights = []
female_heights = []

for person in data[1:]:
    height = int(person[2])
    if person[0] == 'M':
        male_heights.append(height)
    elif person[0] == 'F':
        female_heights.append(height)

avg_male_height = sum(male_heights)/len(male_heights)
avg_female_height = sum(female_heights)/len(female_heights)

print("Avg male height:", avg_male_height)
print("Avg female height", avg_female_height)
```

```text
Avg male height: 178.0121951219512
Avg female height 163.7
```

## Summary

In this chapter, we learned the basics of navigating directories, reading and writing to files, and even how to perform some basic analyses on data stored in a csv file. Later in the program, when we cover topics like web scraping and pandas, we will learn more ways to read and write to files and more ways to manipulate and analyze data. For now, having a solid understanding of these basics concepts will allow you to perform the operations and computations you will need until you get to the next Python lesson.
