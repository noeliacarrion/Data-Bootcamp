![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Error Handling

## Lesson Goals

* Learn about common Python error types.
* Learn how to read Python error messages.
* Write exceptions into your code.
* Catch and handle exceptions in your code.

## Introduction

A significant part of programming involves dealing with errors and exceptions. Beginner Python programmers might initially find errors annoying - constantly reminding you that you did something wrong and presenting you with obstacles in your quest for a solution that works. However, as you progress from beginner to intermediate, you will start to increasingly rely on error messages to write better code. You will learn to view errors and exceptions more as a form of communication that informs you about what is wrong with the code you are writing and where the error is occurring.

In this lesson, we will familiarize ourselves with the different types of errors and exceptions we might encounter in the Python code we write, learn how to write exceptions into our own code, and learn how to handle errors in different ways.

## Python Error Types

There are many types of errors in Python, but below are a few common error types that you are likely to encounter.

* **SyntaxError:** When code has been typed incorrectly.
* **AttributeError:** When you try to access an attribute on an object that does not exist.
* **KeyError:** When you try to access a key in a dictionary that does not exist.
* **TypeError:** When an argument to a function is not of the right type (e.g. a str instead of int).
* **ValueError:** When an argument to a function is of the right type but is not in the right domain (e.g. an empty string)
* **ImportError:** When an import fails.
* **IOError:** When Python cannot access a file correctly on disk.

In addition to letting you know the type of error, Python will also provide an error message that tells you specifically why you are receiving the error.

## Reading Errors

When you encounter an error in Python, there will be a Traceback that informs you of where the error occurs.

```python
from pandas import does_not_exist
```

```text
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)
<ipython-input-105-e9d71fb092be> in <module>()
----> 1 from pandas import does_not_exist

ImportError: cannot import name 'does_not_exist'
```

In the example above, we tried to import something that does not exist. Accordingly, Python gave us an ImportError and told us that it cannot import it. This tells us what is wrong with our code, and the part above it (where the the arrow is) shows us specifically which line of our code caused the error so that we can fix it.

This was a straightforward example, but if you get an error while using a function that itself uses other functions, you will receive several steps in the Traceback above the error line that tell you exactly which lines in which functions errored out.

```python
def func(string):
    print(does_not_exist)

func('this is a string')
```

```text
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-116-5b48da61d415> in <module>()
      2     print(does_not_exist)
      3 
----> 4 func('this is a string')

<ipython-input-116-5b48da61d415> in func(string)
      1 def func(string):
----> 2     print(does_not_exist)
      3 
      4 func('this is a string')

NameError: name 'does_not_exist' is not defined
```

In the error message above, we tried to print a string assigned to a local variable that did not exist, so we received a NameError saying that it is not defined. You can see how the first arrow tells us that there is something wrong with the `func` function and the second arrow shows us specifically that it is the line with the `print` function within `func` that is causing the issue.

## Writing Exceptions Into Our Code

In addition to simply receiving errors, Python allows us to write exceptions into our code so that it throws an error when there is something wrong. We can write conditional statements into our code that check for undesirable conditions and then call the `raise` keyword when one of those conditions is met.

```python
def even_number(number):
    if number % 2 != 0:
        raise ValueError("The number entered is not even!")
    else:
        print("Number accepted.")
        
even_number(3)
```

```text
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-125-195aa3301700> in <module>()
      5         print("Number accepted.")
      6 
----> 7 even_number(3)

<ipython-input-125-195aa3301700> in even_number(number)
      1 def even_number(number):
      2     if number % 2 != 0:
----> 3         raise ValueError("The number entered is not even!")
      4     else:
      5         print("Number accepted.")

ValueError: The number entered is not even!
```

In the example above, we created a function that accepts even numbers. If the number passed to the function is not even, then we raise a ValueError exception and let the user know that they are receiving the error because the number they have passed is not even. The traceback shows that our `even_number` function call errored out and that it is the line with the `raise` keyword within our conditional statement that caused the error to appear.

## Catching Exceptions In Our Code

The last topic we will cover in this lesson is catching exceptions in our code. Periodically, we will know that an exception may occur and our code is going to produce an error, but we will not want the error to crash our entire program. Exception handling can help us address the error while still continuing to run the rest of our code. This is done using `try` and `except` statements.

```python
try:
    even_number(3)
except:
    print("The even_number function errored out.")

print("This line of code still executes.")

The even_number function errored out.
This line of code still executes.
```

In the example above, we tried to call the `even_number` function and pass it the number 3. It doesn't work, but instead of producing an error, it moves to the `except` statement, runs that code, and then continues running the rest of our code. You can use this anytime you want your code to continue running despite encountering errors.

## Summary

In this lesson, we learned about Python errors. We began by learning some of the common error types and when they are raised. We then learned how to read Python error messages and trace back the errors we get to determine their source. We also learned how to write code that raises errors, and finished up the lesson by learning about exception handling with `try` and `except` statements. You should now have a better understanding of errors you may encounter when programming with Python and how to address them.
