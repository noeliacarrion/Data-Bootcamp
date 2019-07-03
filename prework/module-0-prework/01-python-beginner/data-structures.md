![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Data Structures: Lists, Dictionaries, Tuples, and Sets

## Lesson Goals

In this lesson, you will learn about Python's data structures including:

* How counting and indexing works.
* How to use lists to store data.
* How dictionaries work and how to use them.
* The differences between lists and tuples.
* What sets are and when to use them.

## Introduction

A lot of what you're going to have to do as a data analyst is going to involve navigating data structures. The more proficient you can get at this, the faster you will be able to analyze data. However, before we dive into Python's data structures, there is a very basic, but very important, topic that we need to cover: how to count.

## Counting and Indexing

Counting things in Python can be a little tricky and confusing. In most other aspects of life, when you are counting, you always start with 1. If you are counting the number of letters in the word "automobile," you would start with the first letter (a), continue counting until you got to the last letter (e), and the last number you would have counted would have been 10. In Python, you would start counting at 0, but the length of the word would still be 10 because there are 10 spaces or *indexes* (0 through 9) that are assigned (one to each character). The table below should help illustrate this.

**Letter**|**Real Life**|**Python**
:-----:|:-----:|:-----:
a|1|0
u|2|1
t|3|2
o|4|3
m|5|4
o|6|5
b|7|6
i|8|7
l|9|8
e|10|9

In Python, you can get the length of an object by using the `len()` function, and you can reference a specific index by using square brackets `[]` with the index number inside.

```python
>>> len("automobile")

10

>>> word = "automobile"
>>> word[0]

'a'

>>> word[1]

'u'

>>> word[9]

'e'

>>> word[10]

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```

As you can see from the examples above, Python accurately calculated the length of the word, indexed the letter "a" at 0, indexed the letter "u" at 1, indexed the letter "e" at 9, and the 10th index position doesn't exist so we get an error when we try to reference it. Additionally, you can use negative numbers to reference starting from the end instead of from the beginning.

```python
>>> word[-1]

'e'

>>> word[-2]

'l'
```

What if you wanted to select multiple letters? You can use indexes in Python to do that as well.

```python
>>> word[:4]

'auto'

>>> word[4:]
'mobile'

>>> word[3:8]

'omobi'
```

In the examples above, we used index ranges to extract just certain characters from our word. With index ranges, the number on the left side of the colon is the starting position and the number on the right is the ending position. When you leave the left side blank, it starts at the beginning and when you leave the right side blank, it goes until the end.

Now that we understand how counting and indexing work in Python, we are ready to dive into data structures. Data structures are essentially objects in Python that hold data. As a data analyst, there are some that you will use often, and others that you will use only every once in a while, as your needs match what they are good for.

## Lists

Lists are one of the most versatile data structures in Python, and one of the most useful as well. They are comprised of a series of *elements* separated by commas and enclosed in square brackets. Below are some examples of what lists look like.

```python
[1,3,5,7,2,4,8,10]

['The', 'man', 'in', 'the', 'blue', 'suit']

['apple', 390, 876, 'orange', 'highway', 2, 87, 36]
```

The elements of a list can be just about anything - strings, numbers, and even other lists (as we will see later on).

Each element in a list has an index, and you typically reference each element by its index. Just like in the example with the word "automobile" above, the way you reference elements in a list is with square brackets.

```python
>>> lst = ['The', 'man', 'in', 'the', 'blue', 'suit']
>>> lst[0]

'The'

>>> lst[1]

'man'

>>> lst[-1]

'suit'

>>> lst[2:4]

['in', 'the']
```

We can add things to lists by using the `append()` method and remove things using the `remove()` method.

```python
>>> lst.append('jacket')
>>> lst

['The', 'man', 'in', 'the', 'blue', 'suit', 'jacket']

>>> lst.remove('suit')
>>> lst

['The', 'man', 'in', 'the', 'blue', 'jacket']
```

We can even add two lists together to combine their elements.

```python
>>> lst2 = ['and', 'the', 'green', 'trousers']
>>> comb_list = lst + lst2
>>> comb_list

['The', 'man', 'in', 'the', 'blue', 'jacket', 'and', 'the', 'green', 'trousers']
```

Lists can also contain other lists as their elements. These are called *nested lists*, and you can reference their elements with multiple sets of square brackets.

```python
>>> nested = [['A', 'man'], ['a', 'plan'], ['a', 'canal'], ['Panama', '!']]

>>> nested[0]

['A', 'man']

>>> nested[0][1]

'man'

>>> nested[-1][0]

'Panama'
```

If you happen to have a list of numeric values, you can also perform mathematical operations with it.

```python
>>> num_list = [34, 12, 93, 783, 330, 896, 1, 55]

# Sum
>>> sum(num_list)

2204

# Mean
>>> sum(num_list)/len(num_list)

275.5

# Minimum
>>> min(num_list)

1

# Maximum
>>> max(num_list)

896

# Sort Ascending
>>> num_list.sort()
>>> num_list

[1, 12, 34, 55, 93, 330, 783, 896]

# Sort Descending
>>> num_list.sort(reverse=True)
>>> num_list

[896, 783, 330, 93, 55, 34, 12, 1]
```

## Dictionaries

The next most important data structures you need to know are dictionaries. Dictionary elements are *key-value* pairs where keys and values are mapped to each other by colons, split from other key-value pairs via commas, and the entire collection of them is wrapped in curly braces (`{}`). Below is an example of a dictionary containing names as keys and ages as values.

```python
>>> ages = {'Brian':23, 'Amy':22, 'Darlene':47, 'Ralph':32, 'Jordan':28, 'Stephanie':35}
```

Whereas with lists, you access an element by referencing its index, with dictionaries, you retrieve a value by referencing its key. You're essentially performing a lookup, and that is the primary difference in usage between dictionaries and lists.

```python
>>> ages['Brian']

23

>>> ages['Stephanie']

35
```

If you wanted to retrieve all the keys in a dictionary, you could do that with the `keys()` method. Likewise, you can retrieve all the values with the `values()` method.

```python
>>> ages.keys()

dict_keys(['Brian', 'Amy', 'Darlene', 'Ralph', 'Jordan', 'Stephanie'])

>>> ages.values()

dict_values([23, 22, 47, 32, 28, 35])
```

You can also add items to a dictionary and delete items from a dictionary as follows.

```python
>>> ages['Vanessa'] = 30
>>> ages

{'Brian': 23, 'Amy': 22, 'Darlene': 47, 'Ralph': 32, 'Jordan': 28, 'Stephanie': 35, 'Vanessa': 30}

>>> del ages['Vanessa']

{'Brian': 23, 'Amy': 22, 'Darlene': 47, 'Ralph': 32, 'Jordan': 28, 'Stephanie': 35}
```

Lists and dictionaries are the two data structures you will use most often when programming in Python, but there are a couple other data structures of which you should be aware.

## Tuples

Tuples are very similar to lists. However, lists are *mutable*, which means that they can be changed. Tuples are *immutable*, which means they cannot be changed. You can visually distinguish between them because lists are enclosed in square brackets and tuples are enclosed in parentheses.

In the example below, we have a list and a tuple with identical elements. Note how you cannot add or remove anything to the tuple or sort its elements because it doesn't have the attributes to do so that a list does.

```python
>>> a = [1,2,3,4,5]
>>> b = (1,2,3,4,5)

>>> a.append(6)
>>> a

[1, 2, 3, 4, 5, 6]

>>> b.append(6)

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'

>>> a.remove(2)
>>> a

[1, 3, 4, 5, 6]

>>> b.remove(2)

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'remove'

>>> a.sort()
>>> a

[1, 3, 4, 5, 6]

>>> b.sort()

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'sort'
```

So when would you use tuples and when would you use lists? You would use tuples when you want a performance gain and you don't want to allow changes to the data structure.

What if you have a tuple that you want to make changes to, or a list that you want to prevent changes to? Luckily, Python makes it easy to convert a list to a tuple or a tuple to a list.

```python
>>> tuple(a)

(1, 3, 4, 5, 6)

>>> list(b)

[1, 2, 3, 4, 5]
```

## Sets

Sets are another useful data structure that you will want to use any time you want to remove duplicates in a list or tuple (dictionary keys don't allow duplicates by default). What you are left with is a series of unique elements. Visually, sets look like a combination between lists/tuples and dictionaries - they have a collection of elements, separated by commas, wrapped in curly braces.

```python
>>> dupe_list = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
>>> uniques = set(dupe_list)
>>> uniques

{1, 2, 3, 4, 5}
```

Like tuples, sets are also immutable, and just like you were able to easily switch back and forth between list and tuple data structures, you can do the same with sets.

```python
>>> list(uniques)

[1, 2, 3, 4, 5]
```

## Summary

In this chapter, we learned about the different data structures in Python, the properties of each one, and when to use them. These data structures are important for data analytics because a lot of the data you will work with will either come packaged in these types of data structures or will have to be converted to one of these data structures to be computed upon.
