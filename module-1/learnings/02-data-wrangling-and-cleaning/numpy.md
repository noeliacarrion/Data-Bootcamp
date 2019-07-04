![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Introduction to Numpy

## Lesson Goals

* Learn about Numpy data structures.
* Extract data from Numpy arrays.
* Convert other Python data structures to Numpy arrays.
* Perform basic mathematical functions on arrays and elements.

## Introduction

Many of the libraries you will use to perform data analysis in Python, as well as many of the mathematical functions you'll use, will involve working with Numpy. Numpy (short for Numerical Python) is used for numeric computing and includes support for multi-dimensional arrays and matrices along with a variety of mathematical functions to apply to them. In this lesson, we will learn about Numpy's primary data structures and how to apply some basic math functions to them.

## Importing Numpy

In order to use Numpy, you must first import it. It is common to also alias them to `np` so that you don't have to spell out "numpy" every time you want to call one of its methods.

```python
import numpy as np
```

Once the library has been imported, it is ready to use.

## Numpy Arrays

The basic data structures in Numpy are *arrays*, which can be used to represent tabular data. You can think of arrays as lists of lists, where all the elements of a list are of the same type (typically numeric since the reason you use Numpy is to do numeric computing). A *matrix* is just a two-dimensional array.

The *size* of an array is the total number of elements in every list. The *shape* of an array is the size of the array along each dimension (e.g. number of rows and number of columns for a two-dimensional array). Let's create a two dimensional 10 x 4 array containing random numbers and calculate the shape and size of the array using the `shape` and `size` methods.

```python
a = np.random.random((10,4))
print(a)

[[0.37204558 0.14550841 0.67523958 0.27740608]
 [0.2384028  0.3046173  0.76776426 0.69283903]
 [0.13686505 0.61112455 0.76244717 0.55754906]
 [0.23608745 0.86759653 0.17877306 0.06508108]
 [0.44207297 0.56918924 0.9812652  0.27621236]
 [0.70663236 0.49456892 0.47992486 0.30181397]
 [0.20194912 0.48396116 0.1454686  0.45983845]
 [0.59407381 0.22715311 0.07311169 0.17287725]
 [0.45123938 0.61724233 0.3767673  0.77285286]
 [0.49093615 0.79429658 0.91650027 0.37019243]]
```

```python
print(a.shape)
print(a.size)

(10, 4)
40
```

As you can see, the array has a shape of 10 x 4 (just as we ) and the total number of elements in the array is 40.

Now that we have seen an example of a basic two-dimensional array (a matrix), let's learn about how creating arrays with more dimensions than two works in Numpy. Let's build a three-dimensional array of random numbers and see what that looks like.

```python
b = np.random.random((5,2,3))
print(b)

[[[0.73197433 0.51817745 0.5438668 ]
  [0.79680624 0.59678796 0.0162289 ]]

 [[0.89476545 0.77451774 0.51565387]
  [0.81446545 0.11831641 0.97704742]]

 [[0.82995401 0.68795632 0.21211731]
  [0.1731487  0.36950427 0.0526404 ]]

 [[0.78179768 0.96406835 0.85642039]
  [0.78479238 0.92167604 0.48239683]]

 [[0.87567854 0.46034393 0.69389202]
  [0.22559928 0.54405484 0.0284539 ]]]
```

This created an array with five groups of 2 x 3 matrices. Let's see what happens if we pass four dimensions.

```python
c = np.random.random((2,3,4,5))
print(c)

[[[[0.58736781 0.21494172 0.07269135 0.84555299 0.02206719]
   [0.65722215 0.96007326 0.37839556 0.77171739 0.97087094]
   [0.26840046 0.69882463 0.12102026 0.09301578 0.21322542]
   [0.09457464 0.27874227 0.31017789 0.10225793 0.47767532]]

  [[0.33523433 0.57896303 0.73654348 0.7166764  0.18657457]
   [0.50989621 0.12692175 0.14334705 0.97374411 0.9407015 ]
   [0.82055172 0.61183071 0.68798938 0.21174201 0.10522376]
   [0.73547369 0.66640274 0.50181512 0.79826471 0.42295324]]

  [[0.66188393 0.00233442 0.05928187 0.47321329 0.99491768]
   [0.48274197 0.18776065 0.1922766  0.01806328 0.07497537]
   [0.66245574 0.66172635 0.05026587 0.50701135 0.64959154]
   [0.3402423  0.37189705 0.75641773 0.75925858 0.30409956]]]


 [[[0.64058164 0.52463286 0.75176715 0.42144342 0.74667152]
   [0.55599904 0.83269337 0.12642969 0.91171304 0.20743705]
   [0.32750787 0.78112983 0.90434313 0.79234105 0.91762167]
   [0.73860474 0.97166229 0.93089352 0.42083379 0.8593168 ]]

  [[0.96817543 0.82890525 0.47894736 0.36876444 0.72116376]
   [0.46839119 0.0106908  0.44905365 0.24429013 0.70855621]
   [0.43040031 0.45217997 0.92004515 0.47573257 0.40573254]
   [0.14604264 0.11476539 0.6101247  0.99069972 0.75522514]]

  [[0.57347028 0.09737284 0.53702349 0.10981379 0.03451768]
   [0.4690242  0.24443389 0.19865416 0.22965887 0.57494855]
   [0.77353871 0.41886521 0.72384725 0.45725317 0.85284934]
   [0.47088215 0.00314509 0.05658609 0.01090867 0.12534087]]]]
```

This time, we got two groups of three 4 x 5 matrices.

## Extracting Data from Arrays

Extracting elements from arrays works just like it does for other Python data structures. We just need to reference the indexes of the values we want to extract. Below are some examples of how to reference specific rows, columns, and values in a two dimensional array.

```python
# First row of matrix a
print(a[0])

[0.37204558 0.14550841 0.67523958 0.27740608]

# First column of matrix a
print(a[:,0])

[0.37204558 0.2384028  0.13686505 0.23608745 0.44207297 0.70663236
 0.20194912 0.59407381 0.45123938 0.49093615]

# Value in the fifth row and third column of matrix a
print(a[4,2])

0.9812652012454941
```

What about arrays that have more than two dimensions? You just pass a list of indexes for the values you want, and it will return the corresponding dimensions or values.

```python
# First group of array c
print(c[0])

[[[0.58736781 0.21494172 0.07269135 0.84555299 0.02206719]
  [0.65722215 0.96007326 0.37839556 0.77171739 0.97087094]
  [0.26840046 0.69882463 0.12102026 0.09301578 0.21322542]
  [0.09457464 0.27874227 0.31017789 0.10225793 0.47767532]]

 [[0.33523433 0.57896303 0.73654348 0.7166764  0.18657457]
  [0.50989621 0.12692175 0.14334705 0.97374411 0.9407015 ]
  [0.82055172 0.61183071 0.68798938 0.21174201 0.10522376]
  [0.73547369 0.66640274 0.50181512 0.79826471 0.42295324]]

 [[0.66188393 0.00233442 0.05928187 0.47321329 0.99491768]
  [0.48274197 0.18776065 0.1922766  0.01806328 0.07497537]
  [0.66245574 0.66172635 0.05026587 0.50701135 0.64959154]
  [0.3402423  0.37189705 0.75641773 0.75925858 0.30409956]]]

# Second subgroup of the first group
print(c[0,1])

[[0.33523433 0.57896303 0.73654348 0.7166764  0.18657457]
 [0.50989621 0.12692175 0.14334705 0.97374411 0.9407015 ]
 [0.82055172 0.61183071 0.68798938 0.21174201 0.10522376]
 [0.73547369 0.66640274 0.50181512 0.79826471 0.42295324]]

# Third row of the second subgroup
print(c[0,1,2])

[0.82055172 0.61183071 0.68798938 0.21174201 0.10522376]

# Fourth column of the second subgroup
print(c[0,1,:,3])

0.7166764  0.97374411 0.21174201 0.79826471]

# Value in the third row and fourth column of the second subgroup
print(c[0,1,2,3])

0.21174201468822196
```

## Converting Other Data Structures to Arrays

If you have data in another type of data structure and you would like to convert it to an array so that you can take advantage of Numpy's mathematical functions, you can convert them using the `array()` method as follows.

```python
lst_lst = [[1,2,3],[4,5,6],[7,8,9]]
d = np.array(lst_lst)
print(d)
```

This works the same way whether you have a list of lists, a list of tuples, a tuple of lists, or a tuple of tuples.

## Numpy Math Functions

Now that we know how to create and navigate arrays, let's take a look at how to perform mathematical calculations on them.

One of the most common (and useful) functions is `np.sum`, which lets you obtain the sum of any elements you select from an array.

```python
# Sum of all elements in matrix a
print(np.sum(a))

18.28948734532367

# Sum of each column in matrix a
print(np.sum(a, axis=0))

[3.87030467 5.11525812 5.35726199 3.94666256]

# Sum of each row in matrix a
print(np.sum(a, axis=1))

[1.47019964 2.00362339 2.06798582 1.34753812 2.26873977 1.98294011
 1.29121733 1.06721585 2.21810188 2.57192542]

# Sum of all the elements in the first two groups of array b
np.sum(b[:2])

7.298608038014308
```

The `np.mean` function works the same way and is also very useful.

```python
# Mean of all elements in matrix a
print(np.mean(a))

0.4572371836330918

# Mean of each column in matrix a
print(np.mean(a, axis=0))

[0.38703047 0.51152581 0.5357262  0.39466626]

# Mean of each row in matrix a
print(np.,mean(a, axis=1))

[0.36754991 0.50090585 0.51699646 0.33688453 0.56718494 0.49573503
 0.32280433 0.26680396 0.55452547 0.64298136]

# Mean of all the elements in the first two groups of array b
np.mean(b[:2])

0.6082173365011924
```

In addition to letting you perform calculations on individual arrays, Numpy also lets you perform calculations between arrays. For example, let's select two of the subarrays from array c to illustrate how this works.

```python
x = c[0,0]
print(x)

[[0.58736781 0.21494172 0.07269135 0.84555299 0.02206719]
 [0.65722215 0.96007326 0.37839556 0.77171739 0.97087094]
 [0.26840046 0.69882463 0.12102026 0.09301578 0.21322542]
 [0.09457464 0.27874227 0.31017789 0.10225793 0.47767532]]
```

```python
y = c[0,1]
print(y)

[[0.33523433 0.57896303 0.73654348 0.7166764  0.18657457]
 [0.50989621 0.12692175 0.14334705 0.97374411 0.9407015 ]
 [0.82055172 0.61183071 0.68798938 0.21174201 0.10522376]
 [0.73547369 0.66640274 0.50181512 0.79826471 0.42295324]]
```

We can now add, subtract, multiply, and divide the two arrays.

```python
# Add elements of x and y together
print(np.add(x, y))

[[0.92260213 0.79390476 0.80923482 1.56222939 0.20864175]
 [1.16711836 1.08699501 0.52174261 1.7454615  1.91157244]
 [1.08895218 1.31065533 0.80900964 0.3047578  0.31844918]
 [0.83004833 0.94514501 0.81199301 0.90052264 0.90062856]]

# Subtract elements of x from elements of y
print(np.subtract(y, x))

[[-0.25213348  0.36402131  0.66385213 -0.12887659  0.16450738]
 [-0.14732594 -0.83315151 -0.23504851  0.20202671 -0.03016944]
 [ 0.55215126 -0.08699392  0.56696911  0.11872623 -0.10800166]
 [ 0.64089905  0.38766047  0.19163723  0.69600678 -0.05472208]]

# Multiply elements of x and y together
print(np.multiply(x, y))

[[0.19690585 0.12444331 0.05354034 0.60598787 0.00411718]
 [0.33511509 0.12185418 0.05424189 0.75145527 0.91329975]
 [0.22023646 0.42756237 0.08326066 0.01969535 0.02243638]
 [0.06955716 0.18575461 0.15565196 0.0816289  0.20203432]]

# Divide elements of y by elements of x
print(np.divide(y, x))

[[ 0.57074004  2.69358141 10.13247805  0.84758307  8.45484228]
 [ 0.77583541  0.13220007  0.37882858  1.26178847  0.96892538]
 [ 3.05719195  0.87551394  5.68491054  2.27640959  0.49348601]
 [ 7.77664831  2.39074876  1.61783006  7.80638451  0.88544086]]
```

This is only the tip of the iceberg. Numpy has many more functions, which you can and should explore. You can read more about them in the [Numpy documentation](https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.math.html).

## Summary

In this lesson, we learned the basics of working with Numpy. First, we learned how to import the library so that we could use it. From there, we learned about Numpy arrays, including how to extract data from them and how to convert to them from other Python data structures. Finally, we covered some of the basic mathematical functions in Numpy and saw how we could apply them both to the elements of an array as well as to whole arrays themselves.
