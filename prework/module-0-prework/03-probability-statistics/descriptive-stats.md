![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Learn the basics of descriptive statistics

## Lesson Goals

In this lesson, you will learn the basics of descriptive statistics including:

* Numeric and categorical data types.
* Measures of centrality and how to obtain them.
* Measures of dispersion and how to obtain them.
* Measures of variability and how to obtain them.

## Introduction

Before data science became all the rage, statistics was the original science of analyzing data. Statistics is the discipline from which most other forms of data analysis originate, and one of the many things statistical methods are useful for is describing data.

Descriptive statistics is the study of how data can be summarized effectively to describe the important aspects of large data sets. When we calculate descriptive statistics for a data set, it provides us with clues about the data such as what values are normal vs. extreme and how the data is distributed.

For this chapter, we will be using [Google Sheets](https://docs.google.com/spreadsheets/) to perform calculations and illustrate concepts. Google Sheets is a free, in-browser spreadsheet that serves as a viable alternative to other more expensive spreadsheet programs like Microsoft Excel. However, if you already have Microsoft Excel on your computer and would like to use it instead of Google Sheets, please feel free.

The data set we will be using for this lesson is a vehicles data set that contains various statistics about specific models of cars. Download the data set [*mtcars.csv*](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/data/mtcars.csv).

After downloading the data set, open a browser tab and launch [Google Sheets](https://docs.google.com/spreadsheets/). Create a blank spreadsheet and import *mtcars.csv*. After importing, the first few rows of data look like this.

![Cars Data Set](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/images/cars_data_set.png)

## Data Types

Before we start using statistics to analyze data, we must learn a little more about what we are analyzing. This means that we must review the basic data types we are likely to see so that we can tell them apart and treat each type appropriately.

**Numeric Data Types:**

* **Continuous**: Can take on any value, including decimals.
* **Discrete**: Can be any integer (no decimals).

**Categorical Data Types:**

* **Categorical**: Can take on only a specific set of values (categories).
* **Binary**: Categorical data with only two values (e.g. True or False).
* **Ordinal**: Categorical data that has order (e.g. Low, Medium, High).

Let's look at some of the fields in our data set and see if we can identify what data types they are. As a rule of thumb, fields that contain text are typically going to be categorical, so Model, Engine_Shape, and Transmission are all categorical. However, notice that the Engine_Shape field contains only two types of values (V-Shaped or Straight), so we could classify it as a binary type. The same is true for the Transmission field, as its only values are Manual and Automatic.

Our data set also contains several numeric fields. Some of these fields have decimal places (MPG, Displacement, Weight, etc.), so their values are continuous. Other fields contain integers (Cylinders, Fwd_Gears, Carburators, etc.) so they are discrete.

There are currently no ordinal fields in our data, although we could create some if we wanted to by binning our numeric variables and creating categories indicating how high or low they are. We will learn how to do that in a future lesson.

## Measures of Central Tendency

At the heart of descriptive statistics are measures of central tendency. These measures tell us where the middle of a range of values is, which helps us estimate what values we are most likely to see. There are 3 main measures of central tendency, and they each approach finding the middle in a different way.

* **Mean**: Arithmetic average of observations.
* **Median**: Middle item in a range that has been sorted.
* **Mode**: Most frequently occurring value in a distribution.

The mean and median can be calculated for numeric data fields only, while the mode can be applied to both numeric and categorical fields.

Let's examine the MPG field in our data and apply these measures to it. MPG stands for Miles per Gallon, which tells us how far a vehicle can run on a gallon of gasoline. Vehicles with a lower MPG are less fuel-efficient than vehicles with a high MPG

Below are the spreadsheet formulas you would use to get the mean, median, and mode and the result for each.

```excel
=AVERAGE(B2:B33)

20.090625
```

```excel
=MEDIAN(B2:B33)

19.2
```

```excel
=MODE(B2:B33)

21
```

To use these formulas in Google Sheets, scroll down to the bottom of the sheet. Then double click a blank cell under the last value of Column B to enter the formula. For example:

![Average](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/images/descriptive-stats-average.png)

![Median](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/images/descriptive-stats-median.png)

![Mode](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/images/descriptive-stats-mode.png)

What this tells us about the data is that it is very common to see values between 19 and 21 for this field. How common are values outside that range? We will find out in the next section.

## Measures of Dispersion

One major difference between the three measures of central tendency is that the mean can be influenced by extremely large or small values (or *outliers*) whereas median and mode are not. How do we know if our data has outliers? We can calculate measures of dispersion.

Measures of dispersion measure how spread out the data is. There are 5 main measures of dispersion you will need to know.

* **Min**: Smallest value in the data.
* **Max**: Largest value in the data.
* **Range**: The difference between the Max and Min.
* **Quantiles/Percentiles**: What values are located at each percent of the data.
* **Interquartile Range**: The difference between the 75th and 25th percentile (the middle 50%).

Let's calculate each of these for the same MPG field we have been working with.

```excel
=MIN(B2:B33)

10.4
```

```excel
=MAX(B3:B34)

33.9
```

```excel
=MAX(B3:B34)-MIN(B2:B33)

23.5
```

For percentile, let's calculate the 25th and 75th percentiles so that we can confirm our interquartile range results.

```excel
=PERCENTILE(B2:B33,0.25)

15.425
```

```excel
=PERCENTILE(B2:B33,0.75)

22.8
```

```excel
=PERCENTILE(B2:B33,0.75)-PERCENTILE(B2:B33,0.25)

7.375
```

Below is a summary of everything we currently know about the MPG field in our data.

**Statistic**|**Value**
-----|-----
Mean|20.090625
Mode|21
Min|10.4
25th Percentile|15.425
50th Percentile (Median)|19.2
75th Percentile|22.8
Max|33.9
Range|23.5
Interquartile Range|7.375

The values in this field have a total range of 23.5, with a minimum value of 10.4, and a maximum value of 33.9. Fifty percent of the values fall between the interquartile range of 15.425 and 22.8, with 19.2 being the median value, the mean falling a little higher at 20.09, and the mode just above that at 21.

## Frequency Distributions and Histograms

A frequency distribution is a tabular display of data summarized into a relatively small number of intervals.

For our MPG values, we know that the minimum is 10.4 and the maximum is 33.9 so let's create a column of numbers that start at 10, increment by 5, and end at 35. We will enter the following values in cell range N14:N19 of our Google Spreadsheet.

```excel
10
15
20
25
30
35
```

These cells are going to serve as our bins, and we are going to use the `FREQUENCY` formula to count how many MPG values fall into each of these bins. In cell O14, type the following.

```excel
=FREQUENCY(B2:B33,N14:N19)
```

The results should fill in next to the column of numbers we entered in cell range N14:N19 of our spreadsheet. The results should look as follows.

**Bucket**|**Values**
-----|-----
10|0
15|6
20|12
25|8
30|2
35|4
 .|0

What these results mean is that there are:

* 0 values that are less than 10.
* 6 values that fall between 10 and 15.
* 12 values that fall between 15 and 20.
* 8 values that fall between 20 and 25.
* 2 values that fall between 25 and 30.
* 4 values that fall between 30 and 35.
* 0 values that are larger than 35

In addition to viewing these results in a table, we can also create a histogram to get a more visual representation of the MPG value distribution. Below are instructions for creating a histogram in Google Sheets.

* Select column B of the spreadsheet by clicking the column label.
* In the menu bar, select Insert and then choose Chart.
* In the Chart Editor on the right, click on the Chart Type drop-down and select Histogram.

You should get a histogram that looks like the chart below:

![MPG Histogram Wrong](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/images/mpg-histogram-wrong.png)

However, you probably have noticed the average, median, and mode values you created earlier are mis-included in the histogram. So go ahead delete those values. Your histogram should automatically update and you will see:

![MPG Histogram](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/images/mpg-histogram.png)

Note that there are differences between our tabular and histogram results, primarily in the 10-15 bucket and the 15-20 bucket. It turns out that there is one vehicle that has an MPG of exactly 15 in our data set, and the `FREQUENCY` formula is counting that record as part of the 10-15 range while the histogram is counting it as part of the 15-20 range. Keep this behavior in mind when working with frequency distributions.

## Measures of Variability

In addition to measures of centrality and dispersion, we can also calculate measures of variability. Measures of variability measure how wildly the values in the range vary from one another. Below are three common metrics used to measure variability.

* Variance: Average of squared deviations around the mean.
* Standard Deviation: Square root of the variance.
* Mean Absolute Deviation: Average of the absolute values of all the deviations around the mean.

Below are examples of how you would calculate all three of these in Google Sheets and the results. Each of these gives you a different perspective of how values in a field vary.

If you were calculating the variance manually, you would obtain the mean for the field, subtract the mean from each value to get the deviation, square it, and then take the average of all the squared deviations. Luckily, Google Sheets has a `VAR` formula that you can use to obtain the variance without having to perform these steps.

```excel
=VAR(B2:B33)

36.32410282
```

Once you have calculated the variance of a field, you can take the square root of it to obtain the standard deviation. Alternatively, if you wanted to calculate the standard deviation without calculating the variance first, you could use the `STDEV` formula in Google Sheets.

```excel
=STDEV(B2:B33)

6.026948052
```

Finally, we have the mean absolute deviation, which is calculated exactly like the variance except that instead of squaring the deviations, you would take the absolute value. Again, Google Sheets has an `AVDEV` formula that will allow you to obtain this metric for a field without having to go through multiple steps.

```excel
=AVEDEV(B2:B33)

4.714453125
```

**Note**: It is often useful to compare the variability metrics of different fields to each other to get a sense of what fields in your data have the most variability. One problem with doing this, however, is that each field in your data will likely be measured in different units. To get a standardized variability metric, you can calculate the *coefficient of variation*, which is simply the standard deviation divided by the mean.

## Summary

In this lesson, we learned about descriptive statistics and how we can use them to describe our dataset. We learned about measures of centrality, dispersion, and variability, what metrics can be used for each, and how to obtain them in Google Sheets. These are important foundational topics that we will revisit frequently as we work our way through the rest of this program. Many of the more advanced concepts you will learn later on will depend on the concepts you have learned here, so make sure you have a firm understanding of them. In fact, practice calculating all of these metrics for the different numeric data fields that are present in the data set, compare the values you get, and see what you learn!