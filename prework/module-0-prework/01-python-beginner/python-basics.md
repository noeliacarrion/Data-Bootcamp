![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Python Programming Basics

## Lesson Goals

In this lesson, you will learn the basics of Python including:

* Access Python from the command line.
* Provide input to a Python built-in function and receive output.
* Perform mathematical calculations with Python.
* Work with strings and numbers.
* Work with variables and user inputs.

## Introduction

[Python](https://www.python.org/) is one of the most useful, versatile, and popular programming languages for data analytics. The language's readability, the number of libraries available for doing just about anything you'd want to do, and Python's large and supportive user community make it an ideal choice for analyzing data, modeling real-world scenarios, generating visualizations, and even building data-driven applications. However, before we can run we must learn how to walk. This chapter will introduce the basics you need to know in order to get started programming with Python.

## Accessing Python from the Command Line

The most straightforward way to program in Python is directly from the command line, which you should have set up during the Preparing Your Development Environment lesson. To access the Python interpreter from the command line, you just type `python` and you should get the three carrot symbols which means you are now accessing the Python interpreter.

```bash
$ python3

>>>
```

From here, you can type Python commands into the interpreter.

:information_source: Remember, Mac users will access Python by typing either `python3` or `python`. The difference is `python3` will launch Python 3 for you whereas `python` will launch Python 2 for you. Python 2 and 3 share a lot of the same syntaxes but there are also many differences. In this course, we are using Python 3.

## Input and Output

When you strip away all the complexity that can come with programming and get right down to the core, you will find that all programming really boils down to is passing some instructions to a computer (input) and receiving some response (output). With Python, and all other programming languages for that matter, the instructions you pass must be formatted in a way that the computer understands and knows how to handle. When you pass these instructions correctly, you get a response. When you pass them incorrectly, you get an error.

For example, in the first command below, we have formatted our input correctly, so the machine understands that you want to print *Hello World* to the screen, and that's exactly what it does. In the second example, we have misspelled the `print` command as `prnt` (which the computer doesn't understand), so we get an error that tells us that `prnt` is not defined. It doesn't know what to do with that command.

```python
>>> print("Hello World")

Hello World

>>> prnt("Hello World")

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'prnt' is not defined
```

This concept of input and output is important, so remember it as best as you can. While you're at it, also remember the `print()` function because you will use it all the time when programming in Python when you want to see the result of whatever it is you are working with.

## Doing Math with Python

One of the things computers are really great at doing is performing calculations, and one of most basic things you can do with Python is to use it as a calculator. Python comes with a variety of mathematical operators built-in. Below are examples of the ones you will use most often.

```python
# Addition
>>> 6 + 4

10

# Subtraction
>>> 100 - 80

20

# Multiplication
>>> 9 * 8

72

# Division
>>> 200 / 24

8.333333333333334

# Exponents
>>> 8**4

4096
```

:bulb: Tip: In Python, lines starting with `#` are comments which are not executed. Use `#` to add notes for your Python code.

:bulb: Tip: `#` is used for single-line comments in Python. For multi-line comments, use paired `"""` as shown below:

```python
"""
These
are
multi-line
comments
"""
>>> print("hello")
``` 

## String and Numeric Data Types

Python comes with a variety of different data types that are important to know. There is a long list of them, but to keep these lessons as intuitive as possible, we will cover them as we encounter them in examples. For this chapter, you will only need to know about string and numeric data types (specifically, integer and floating-point number).

If you don't know the data type of an object in Python, you can use the `type()` function to find out what it is.

```python
>>> type("I ate a banana")

<class 'str'>

>>> type(123)

<class 'int'>


>>> type(98.6)

<class 'float'>
```

A string is a sequence of characters and spaces. In Python, they are wrapped in either single quotes (`'this is a string'`) or double quotes (`"this is another"`). You can apply some mathematical operators to them, such as adding (concatenating) two strings together and multiplying a string by some integer to repeat it a specified number of times. You can also convert something that is not a string (such as a number) to a string by using the `str()` function. Below are examples of all three of these.

```python
>>> "Hello " + "everyone!"

'Hello everyone!'

>>> "Hello " * 8

'Hello Hello Hello Hello Hello Hello Hello Hello '

>>> str(586)

'586'
```

Numeric types in Python are types that you can use for doing math and performing calculations. The most commonly-used ones are integers and floating-point numbers. You have actually already seen both of these in Doing Math we just completed, but here we are going to explicitly call them out so that you know so that you can easily recognize them.

The difference between integers and floating-point numbers is that integers are whole numbers that do not have decimal places. Therefore, when you see a number in Python that looks like `10`, you know right away that it as an integer, whereas if you were to see it with a decimal place (`10.0`), you know it is a floating point number. You can convert a non-float data type to a floating point number by using the `float` function, and a non-integer to an integer by using the `int` function. This can be done for other numeric types as well as strings, as shown in the examples below:

```python
>>> float(137)
137.0

>>> int(596.89)

596

>>> int("42")

42

>>> float("42.97")

42.97

>>> int("42.97")

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '42.97'

>>> int(float("42.97"))

42
```

There are a couple things that are important to call out about the examples above. First, notice that when we converted a float to an integer in the second example, it simply chopped off the decimal. It did not round to the nearest integer. That's an important behavior to remember.

Second, you can't go straight from a floating-point string to an integer. To do that, you need to convert it to a float first and then an integer like we did in the last example.

## Variables

Remember your algebra class in high school? Well here is where those letters that represent numbers come in handy in the real-world. In Python, these are called variables, they can hold much more than just numbers. In fact, they can hold a variety of different kinds of data structures, which we will learn about a little later. For now though, let's stick with numbers.

Below is a simple example. We have assigned a value of 4 to the variable `x`, a value of 5 to the variable `y`, and when we add `x` and `y` together, we get a value of 9.

```python
>>> x = 4
>>> y = 5
>>> x + y

9
```

If we needed to store the result of `x + y` for later, we could have assigned it to another variable `z` like below. We could then do a variety of other things to `z` like print it or use it as part of another calculation.

```python
>>> z = x + y
>>> print(z)

9

>>> z * y

45
```

You can name variables whatever you like, and in fact, it is useful to name them according to what you store in them so that they can be used in an intuitive fashion later on. For example, let's say we were trying to keep track of how many animals (and what types) were in shelters of varying sizes. In the example below, we are combining all the concepts we have learned about so far in this chapter to output the total number of animals, total square feet, and the square footage per animal of the shelter.

```python
>>> dogs = 40
>>> cats = 25
>>> rabbits = 10

>>> shelter_length = 30
>>> shelter_width = 25

>>> total_animals = dogs + cats + rabbits
>>> sqft = shelter_length * shelter_width

>>> print("Total number of animals:", total_animals)

Total number of animals: 75

>>> print("Total shelter square feet:", sqft)

Total shelter square feet: 750

>>> print("Square feet per animal:", sqft/total_animals)

Square feet per animal: 10.0
```

## Accepting Variable Inputs

Instead of hard-coding values, Python also gives you the ability to collect a yet-to-be-defined input from the user at the time that a program runs. You can use the appropriately-named `input` function for to capture an input. In the example below, we are having the program ask the user for their name (to which I respond with Tony) and then printing a personalized greeting for them.

```python
>>> first_name = input("Enter your first name: ")
Enter your first name: Tony

>>> print("Hello,", first_name)

Hello, Tony
```

Note: In order to do the example below, we would have already needed to cover data types. Do a string example first and then go back to this one.

Let's apply this concept to our animal shelter example. If we wanted a user to be able to enter the number of each animal and the dimensions of the shelter from our example above, we would do so a follows.

```python
>>> dogs = int(input("Enter the number of dogs: "))

Enter the number of dogs: 30

>>> cats = int(input("Enter the number of cats: "))

Enter the number of cats: 50

>>> rabbits = int(input("Enter the number of rabbits: "))

Enter the number of rabbits: 0

>>> shelter_length = int(input("Enter the shelter length: " ))

Enter the shelter length: 40

>>> shelter_width = int(input("Enter the shelter width: " ))

Enter the shelter length: 20
```

We have now stored new values into the variables `dogs`, `cats`, and `rabbits` as well as for `shelter_length` and `shelter_width`. One thing to note is that I have used the `int` function to convert the input we receive from the user into an integer so that we can perform calculations with it later. The input accepted when you use the `input` function is a string by default. This is ideal for printing back out what the user entered like we did for our customized greeting example, but it causes problems when the user is entering numbers that you are going to have to perform calculations with after they are entered.

**Pro tip:** Always take into consideration the types of inputs you expect to receive and what you plan to do with them when designing interactive programs like this.

Now that we have updated values, we can recalculate the `total_animals` and `sqft` and then print our summaries out to the console.

```python
>>> total_animals = dogs + cats + rabbits
>>> sqft = shelter_length * shelter_width

>>> print("Total number of animals:", total_animals)

Total number of animals: 80

>>> print("Total shelter square feet:", sqft)

Total shelter square feet: 600

>>> print("Square feet per animal:", sqft/total_animals)

Square feet per animal: 7.5
```

Hopefully, you are starting to get a sense of how powerful this can be and how you could potentially build upon and combine these very basic concepts in different ways to perform more complex and sophisticated programs.

## Summary

In this chapter, we covered the basics of programming with Python. We learned how to access Python from the command line, about inputs and outputs, how to do math and use Python as a calculator, about string and numeric data types, and how to work with variables and user inputs. The few core concepts we learned here have equipped you with a solid foundation for learning the more advanced Python programming topics you are going to encounter later in the program. When combined with a little creativity and curiosity, you'll find that these concepts can get you surprisingly far!
