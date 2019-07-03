![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Control Flow: Conditional Logic and Loops

## Lesson Goals

In this lesson you will learn about control flow in Python, including:

* What Boolean data types are and how to use them.
* How to use conditional statements to model decision-making.
* How to perform iteration in Python with for and while loops.


## Introduction

Once you have learned the basics of Python and data structures, two of the next topics you will need to master are *conditional statements* and *loops*: collectively known as *control flow*. When you are analyzing data, there are going to be many times where you will need to perform the same calculation or operation on a variety of different objects, sometimes only if certain conditions are met. Knowing how to effectively use loops and conditional statements will make it so that you don't need to write the same code over and over again, which will make you a much more efficient analyst.

**Note:** Up until this point, we have been entering Python code a single line at a time via the Python interpreter on the command line. Thus, all the code examples have had the triple carrot symbol (`>>>`) to designate inputs and text without the symbol preceding have been outputs. From this point on, we will be writing and interpreting multiple lines of Python code at a time, and when you're doing that, it is recommended to use a Jupyter Notebook for interactivity instead of the command line. Therefore, in the code snippets going forward, the entire snippet will be an input, and any outputs will be shown as a separate block containing text.

## Boolean Data Types

In this chapter, we are going to use a new data type in Python: the *Boolean* data type. These data types can have one of two values (True or False), and they are used to evaluate whether some condition has been met. Because of this, they are critical for computational decision-making and control flow.

Boolean data types can either be assigned or evaluated. For assignment, you are basically just assigning to a variable a value of True or False for later use.

```python
happy = True
print("Happy variable is set to ", happy)
```

```text
Happy variable is set to  True
```

Evaluation uses one of the following evaluators to test whether a condition exists and returns True if it does and False if it does not.

- `==`: evaluates whether two objects are equal.
- `!=`: evaluates whether two objects are not equal.
- `>`: evaluates whether an object is greater than another object.
- `<`: evaluates whether an object is less than another object.
- `>=`: evaluates whether an object is greater than or equal to another object.
- `<=`: evaluates whether an object is less than or equal to another object.
- `in`: evaluates whether an object is in some range or data structure.
- `not in`: evaluates whether an object is not in some range or data structure.

Below are some examples.

```python
print(5 + 5 == 10)
print('apple' != 'orange')
print(100 > 75)
print(93 < 80)
print(3 in [1,2,3,4,5])
print(3 not in [1,2,3,4,5])
```

```text
True
True
True
False
True
False
```

In the examples above, we evaluated one condition at a time and returned the Boolean True if each condition was true and False if it was false. In addition to evaluating single conditions, Python allows you to evaluate whether multiple conditions exist at a time. This is very helpful for modeling and automating more complicated decision-making processes.

The two operators you need to do this are the "and" (`&`) operator and the "or" (`|`) operator. When you use the "and" operator, *all* conditions within your statement need to be true for the Boolean returned to be True. When you use the "or" operator, True will be returned in *any* of the statements are true.

```python
print((5 + 5 == 10) & ('apple' != 'orange'))
print((100 > 75) & (93 < 80))
print((100 > 75) | (93 < 80))
print((93 < 80) | (3 not in [1,2,3,4,5]))
```

```text
True
False
True
False
```

Notice that in the example above, we wrapped each condition in parentheses. This is necessary when you are evaluating multiple conditions together. If you don't do this, your conditional statements will not be evaluated properly.

## Conditional Logic

Now that we know about Boolean data types and how to evaluate a statement to get them, we are ready to combine them with conditional logic to model real-world decisions. Conditional logic in Python consists of three main conditional statements:

- `if`: evaluates whether some condition is true or false.
- `elif`: evaluates another condition if all preceding `if` and `elif` statements are false.
- `else`: specifies what happens if all preceding `if` and `elif` statements are false.

Below is an example that illustrates how these three conditional statements work. Try the example below as is, with a number greater than 10, and with a number less than 10 to see how the output changes.

```python
number = 10

if number < 10:
    print("Number is less than 10")
elif number > 10:
    print("Number is greater than 10")
elif number == 10:
    print("Number is exactly 10")
else:
    print("Number is probably not a number at all")
```

```text
Number is exactly 10
```

In addition to conditional logic, there is something else you are seeing here for the first time: code indentation. In Python, whitespaces have meaning, and when you see an indented line in a code block, it means that the line is a continuation of, or is part of the logic belonging to, the most recent unindented line above it. This may take some getting used to, but once you have become accustomed to seeing it, you'll find that it is part of what makes Python code easy to read.

Next, let's try a more complex example that includes multiple conditions and sub-conditions. Let's say we are trying to figure out when we should leave the house to drive to a doctor's appointment. If there will be a lot of traffic or if it is raining outside, we will need to give ourselves extra time to arrive on time. With no rain or traffic, our commute will take 30 minutes. If it is raining, we will need to add 15 minutes to our commute, and if there is traffic, we will need to add 20 minutes to our commute. Below is how we would model this scenario using conditional logic and the Boolean evaluators we learned about.

```python
commute = 30
rain = False
traffic = True

if (rain == True) | (traffic == True):
    if (rain == True) & (traffic == True):
        total_commute = commute + 15 + 20
    elif (rain == True) & (traffic == False):
        total_commute = commute + 15
    elif (rain == False) & (traffic == True):
        total_commute = commute + 20
else:
    total_commute = commute

print("Your total commute time is expected to be", total_commute, "minutes.")
```

```text
Your total commute time is expected to be 50 minutes.
```

Take a few minutes to go through the example above line by line to ensure you understand the logic. Also try changing the variable assignments at the beginning of the code block to see how the outputs change and follow the logic again to ensure you understand why the result is different.

## Iteration: Looping with Python

Learning how to work with loops can make you a much more efficient programmer and save you tons of time. In this section, we are going to learn about two kinds of loops in Python: for loops and while loops.

### For Loops

The first kind of loop we are going to learn about is called a *for loop*. A for loop will iterate through a series of objects and allow you to perform some operation on each one as you loop through them. In the example below, we are going to loop through a range of consecutive numbers. You can use the `range()` function in Python to get a range without having to type out every number in that range.

When we pass a single number to the `range()` function, it automatically creates a range that starts with 0 and ended at that number.

```python
range(10)
```

```text
range(0, 10)
```

Alternatively, we could pass the `range` function a beginning and ending number, and it will create a range between those two numbers.

```python
range(5, 15)
```

```text
range(5, 15)
```

We can also calculate the length of the range using the `len()` function.

```python
len(range(5, 15))
```

```text
10
```

Notice that Python calculated the length of the range between 5 and 15 as 10. If you count both 5 and 15, there are technically 11 numbers in the range, so Python is not counting one of those. Let's see if we can find out which one by looping through it with a for loop and printing out each number in the range.

```python
for i in range(5, 15):
    print(i)
```

```text
5
6
7
8
9
10
11
12
13
14
```

When we iterated through our range with a for loop, it started at the first number we entered for the range (5), but it stopped just short of the number we chose to end our range (15). That is an important behavior to remember: the for loop will not get to the last number of the range you enter.

In addition to looping through ranges, you can also loop through data structures. Below is an example where we iterate through a list of fruit, printing out the name of each fruit as we encounter it.

```python
fruits = ['apple', 'orange', 'banana', 'grapes', 'pineapple']

for fruit in fruits:
    print(fruit)
```

```text
apple
orange
banana
grapes
pineapple
```

In the next example, we will iterate through items in a dictionary. Note that for dictionaries, we have both keys and values, so we need to specify two variables, separated by a comma, after the `for` command in order to fully extract both as well as apply the `items()` method to the dictionary to unpack its items.

```python
ages = {'Brian':23, 'Amy':22, 'Darlene':47, 'Ralph':32, 'Jordan':28, 'Stephanie':35}

for name, age in ages.items():
    print(name, "is", age, "years old.")
```

```text
Brian is 23 years old.
Amy is 22 years old.
Darlene is 47 years old.
Ralph is 32 years old.
Jordan is 28 years old.
Stephanie is 35 years old.
```

We can even do math inside a loop. Let's say we want to keep a running total of the values inside a list as we iterate through it. We can do that as follows.

```python
num_list = [34, 12, 93, 783, 330, 896, 1, 55]

total = 0

for i in num_list:
    total += i
    print("Total is currently", total)
```

```text
Total is currently 34
Total is currently 46
Total is currently 139
Total is currently 922
Total is currently 1252
Total is currently 2148
Total is currently 2149
Total is currently 2204
```

In the example above, we created a `total` variable, to which we initially assigned a value of 0. We then iterated through our number list, and for each element, we added that number to the `total` variable's current value and printed the updated value to the console.

Note that we used the `+=` operator to add each element's value to the total. Alternatively, we could have done this as follows: `total = total + i`. It does the same thing, but the way we did it is more concise.

Just like we can iteratively keep track of a running total for elements in a list, we can also iteratively add items to a list using the `append()` method. In the example below, we start with a blank list, and then we iterate through a range of numbers, performing a calculation on each iteration and adding the result to our list.

```python
new_list = []

for i in range(1, 11):
    square = i**2
    new_list.append(square)

print(new_list)
```

```text
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

### While Loops

*While loops* are another type of loop in Python. They are not used as often as for loops but are still worthwhile to know about. Whereas for loops will iterate straight through a series of objects, while loops continue iterating *while* some condition is true. Once the condition is false, the while loop stops iterating.

Let's look at an example. You are baking a cake that needs to sit in the oven for 60 minutes. You put the cake in the oven and then wait, checking every 15 minutes to see if the cake is done. Below is how you would model this.

```python
total_time = 60
minutes_elapsed = 0
wait = 15

print("Cake is in the oven.")
minutes_elapsed += wait

while minutes_elapsed < total_time:
    print("Cake is not done yet.")
    minutes_elapsed += wait

print("It's done. Let's eat cake!")
```

```text
Cake is not done yet.
Cake is not done yet.
Cake is not done yet.
Cake is not done yet.
It's done. Let's eat cake!
```

There are a couple of important things to watch out for when working with while loops. The first is to make sure you design the while loop in a way that it can ultimately get to the limit you have set for it - for example, always have a line of code that serves as an incremental step (increments a variable that will eventually reach your threshold). If you don't do this, when you run it, it will enter an infinite loop and just keep running. You'll have to manually exit out of your program if this happens.

The other thing to watch out for is where you place the incremental step. It is typically placed at the end of a series of actions, but in more complex logic may need to be placed elsewhere within the loop.

## Summary

In this chapter, we have learned about how conditional logic and iteration work in Python. We started the chapter by introducing Boolean data types and looking at how they can be used. We then combined this with the three conditional statements to start writing code that can automate decision-making. Finally, we learned about the two types of loops in Python and when it is appropriate to use each one.
