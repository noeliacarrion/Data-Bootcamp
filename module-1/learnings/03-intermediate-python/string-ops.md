![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# String Operations

## Lesson Goals

* Gain an understanding of Python string operations.
* Learn how to subset and split strings.
* Understand how to leverage boolean methods for string operations.
* Learn how to manipulate string cases with Python.
* Learn how to strip white spaces and replace strings with other strings.
* Learn some basic regular expressions and how to apply them.

## Introduction

As a data analyst, you will find yourself wrangling with text strings regularly. Categorical variables, documents, and other text-based data often come inconsistently structured. Because of this, it is helpful to know about different methods for transforming, cleaning, and extracting text. Python comes with several tools for performing string operations. In this lesson, we will learn about how to use these tools to work with strings.

## Python String Operations

Thus far in this program, you have seen a few examples here and there that involve string operations in the context of other topics we have covered. In this section, we will cover string operations more comprehensively so that you have a solid understanding of how to use them.

Recall from your Python prework that the `+` operator concatenates two strings together and that the `*` operator repeats a string a given number of times.

```python
print('Hello' + 'World')

HelloWorld
```

```python
print('Hello' * 8)

HelloHelloHelloHelloHelloHelloHelloHello
```

Recall that you can also join strings in a list together using a designated separator with the `join` method.

```python
x = 'Happy'
y = 'Puppies'
z = [x,y]

' '.join(z)

'Happy Puppies'
```

We also covered how to get the length of strings and how to subset them via indexing.

```python
len('automobile')

10
```

```python
word = 'automobile'

print(word[0])
print(word[5])
print(word[-1])

a
o
e
```

We can use the `split` method to turn strings into lists based on a separator that we designate (spaces if left empty).

```python
a = 'They ate the mystery meat. It tasted like chicken.'

print(a.split())
print(a.split('.'))
print(a.split('m'))

['They', 'ate', 'the', 'mystery', 'meat.', 'It', 'tasted', 'like', 'chicken.']
['They ate the mystery meat', ' It tasted like chicken', '']
['They ate the ', 'ystery ', 'eat. It tasted like chicken.']
```

We can also use boolean methods such as `startswith`, `endswith`, and `in` to check if strings start with, end with, or contain certain characters or other strings.

```python
b = 'There is no business like show business.'

print(b.startswith('T'))
print(b.startswith('There'))
print(b.startswith('there'))

True
True
False
```

```python
print(b.endswith('.'))
print(b.endswith('business.'))
print(b.endswith('Business.'))

True
True
False
```

```python
print('like' in b)
print('business' in b)
print('Business' in b)

True
True
False
```

Note from the examples above that these are case sensitive. Speaking of cases, Python provides us with several useful ways to change the cases of strings.

```python
c = 'shE HaD a maRveLoUs aSsoRtmeNt of PUPPETS.'

print(c.lower())
print(c.upper())
print(c.capitalize())
print(c.title())

she had a marvelous assortment of puppets.
SHE HAD A MARVELOUS ASSORTMENT OF PUPPETS.
She had a marvelous assortment of puppets.
She Had A Marvelous Assortment Of Puppets.
```

We can also remove any white space from the beginning, end, and middle of a string with the `lstrip`, `rstrip`, and `strip` methods respectively.

```python
d = ' I have a tendency to leave trailing spaces. '

print(d.lstrip())
print(d.rstrip())
print(d.strip())

I have a tendency to leave trailing spaces. 
 I have a tendency to leave trailing spaces.
I have a tendency to leave trailing spaces.
```

Another useful string operation, which we saw briefly in the data wrangling lessons, is using the `replace` method to replace one string for another.

```python
e = 'I thought the movie was wonderful!'

print(e.replace('wonderful', 'horrible'))
print(e.replace('wonderful', 'just OK'))

I thought the movie was horrible!
I thought the movie was just OK!
```

## Regular Expressions

Python's string operation methods can take us a long way, but we will inevitably encounter a situation where we need to rely on some additional tools called regular expressions. Regular expressions allow us to perform different types of pattern matching on text in order to arrive at the result we want.

In order to use regular expressions, we will import the `re` library.

```python
import re
```

Some of the most useful methods in the `re` library are:

* `search`: Returns the first instance of an expression in a string.
* `findall`: Finds all instances of an expression in a string and returns them as a list.
* `split`: Splits a string based on a specified delimiter.
* `sub`: Substitutes a string/substring with another.

Regular expressions consist of sequences that represent certain types of characters that can appear in strings. We can enclose characters in square brackets and then use the `findall` method to return all characters in a string that match as follows.

```python
text = 'My neighbor, Mr. Rogers, has 5 dogs.'
print(re.findall('mneiasdo', text))

['n', 'e', 'i', 'o', 'o', 'e', 's', 'a', 's', 'd', 'o', 's']
```

This found any character we explicitly designated in our regular expression and returned them as a list. Note that the capital M was not returned since regular expressions are case sensitive.

Regular expressions also have sets that we can use as shortcuts so that, for example, we don't have to type out every letter in the alphabet or every number in order to match them. Below are some of the most useful regular expression sets.

* **[a-z]**: Any lowercase letter between a and z.
* **[A-Z]**: Any uppercase letter between A and Z.
* **[0-9]**: Any numeric character between 0 and 9.

```python
print(re.findall('[a-z]', text))

['y', 'n', 'e', 'i', 'g', 'h', 'b', 'o', 'r', 'r', 'o', 'g', 'e', 'r', 's', 'h', 'a', 's', 'd', 'o', 'g', 's']
```

Note that this set returned all lower case letters and excluded the capital M, the number 5, and all the punctuation marks. We can add the `^` character inside the square brackets to return everything that doesn't match the sequence we have designated.

```python
print(re.findall('[^a-z]', text))

['M', ' ', ',', ' ', 'M', '.', ' ', 'R', ',', ' ', ' ', '5', ' ', '.']
```

In this case, it returned the capital letters, the number, and all punctuation and white spaces.

What if we wanted to extract both upper and lower case letters from our string? We can just add `A-Z` inside our square brackets.

```python
print(re.findall('[a-zA-Z]', text))

['M', 'y', 'n', 'e', 'i', 'g', 'h', 'b', 'o', 'r', 'M', 'r', 'R', 'o', 'g', 'e', 'r', 's', 'h', 'a', 's', 'd', 'o', 'g', 's']
```

And if we wanted to also extract spaces, we can add a space.

```python
print(re.findall('[a-zA-Z ]', text))

['M', 'y', ' ', 'n', 'e', 'i', 'g', 'h', 'b', 'o', 'r', ' ', 'M', 'r', ' ', 'R', 'o', 'g', 'e', 'r', 's', ' ', 'h', 'a', 's', ' ', ' ', 'd', 'o', 'g', 's']
```

Once we get to a point where we are adding multiple things to our regular expression, we will want to leverage additional shortcuts called character classes (also known as special sequences). Below are some of the most useful ones and what they match.

* `\w`: Any alphanumeric character.
* `\W`: Any non-alphanumeric character.
* `\d`: Any numeric character.
* `\D`: Any non-numeric character.
* `\s`: Any whitespace characters.
* `\S`: Any non-whitespace characters.

Let's take a look at how some of these work.

```python
print(re.findall('[\d]', text))

['5']
```

```python
print(re.findall('[\w]', text))

['M', 'y', 'n', 'e', 'i', 'g', 'h', 'b', 'o', 'r', 'M', 'r', 'R', 'o', 'g', 'e', 'r', 's', 'h', 'a', 's', '5', 'd', 'o', 'g', 's']
```

```python
print(re.findall('[\S]', text))

['M', 'y', 'n', 'e', 'i', 'g', 'h', 'b', 'o', 'r', ',', 'M', 'r', '.', 'R', 'o', 'g', 'e', 'r', 's', ',', 'h', 'a', 's', '5', 'd', 'o', 'g', 's', '.']
```

We can use the `split` method to split a string on specific characters, such as commas or any numeric values.

```python
print(re.split(', ', text))

['My neighbor', 'Mr. Rogers', 'has 5 dogs.']
```

```python
print(re.split('[0-9]', text))

['My neighbor, Mr. Rogers, has ', ' dogs.']
```

Let's also take a look at how we can use the `sub` method to substitute out how many dogs our neighbor has.

```python
print(re.sub('[0-9]', '100', text))

My neighbor, Mr. Rogers, has 100 dogs.
```

## Summary

In this lesson, we learned how to manipulate strings with Python. We started by reviewing some of the Python string operations we had seen in previous lessons. Then we learned how to subset strings and split them based on designated characters. From there, we covered boolean methods and how to use them while operating on strings. We also looked at how to change cases of strings, how to strip white spaces, and how to replace substrings with other strings. Finally, we finished up the lesson learning about some of the most frequently used regular expressions and how to use them to match characters in strings.
