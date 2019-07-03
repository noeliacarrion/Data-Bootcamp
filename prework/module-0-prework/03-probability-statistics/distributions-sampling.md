![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Learn the basics of sampling and distributions

## Lesson Goals

In this lesson, you will learn the basics of sampling and distributions including:

* An overview of sampling and when to use it.
* How to estimate a sample statistic.
* How to obtain samples using Google Sheets.
* Generating a sampling distribution.
* Different types of probability distributions.
* How to sample from probability distributions in Google Sheets.

## Introduction

In the last lesson, we learned about descriptive statistics. In this lesson, we are going to prepare ourselves for the inferential statistics we will encounter later in the program by learning about sampling, sampling distributions, and probability distributions.

The data set we are going to use for this lesson will be the same cars data set that we used for the descriptive statistics lesson.

## Sampling

The main goal of inferential statistics is to infer insights from some large data set, called a *population*, of which we only have access to a small part, called a *sample*. In order to better understand this, let's look at a metaphor.

Assume you are cooking a big pot of soup. You add all your ingredients to the pot, season it with salt and pepper, stir everything around to make sure it is properly mixed, and then dip a spoon into the soup and taste it. The spoonful of soup is essentially a sample of the larger pot of soup (the population), which would be impossible to taste all at once. The spoonful is representative of the larger pot of soup, and it helps you estimate whether you need to add more seasoning, just as a sample is representative of the population it comes from and helps you estimate population parameters and make determinations about what the population might look like.

Sampling is useful when you have a very large data set but you do not have access to distributed computing or big data tools to process and compute the statistics you need quickly. Taking samples and performing the necessary operations on them will allow you to produce accurate estimates for the values without having to compute on the entire data set.

### Estimation

The reason for sampling is often to try to estimate some value in the population (such as the mean of a field). For example, let's say we wanted to estimate the average MPG for the entire population of cars out there. In our cars data set, we only had a total of 32 vehicles. There are more than 32 types of vehicles in the world, so what we are working with is essentially just a sample of the larger population of cars.

Assuming that the sample we have is representative of the population, what we need to do to estimate the population's average MPG is to sample repeatedly from the data we have and calculate the *sample statistic* (the average MPG) for each sample. Every time we sample, we will record the sample statistic, which will be a little different every time because each sample will consist of a different group of cars. Once we have sampled enough times and accumulated a large enough set of sample statistics, we will start to get a sense of what range of values could contain the population mean.

### Sampling in Google Sheets

Let's look at how to do this in Google Sheets. To our cars data set, we are going to add a column at the end called Random. In the first cell under Random column, we are going to enter `=RAND()` and then copy and paste it for every cell in that column.

:bulb: Tip: Instead of copying-and-pasting the formula, you can also click-and-hold the bottom right corner of the cell (the square dot) then drag your cursor down to automatically fill the formula in the cell range you select. 

This is going to generate a random number for each row, which will be critical for sampling. The results should look something like the image below, although since we are generating random numbers, the actual numbers in the Random column will be different for everyone.

![Random Column](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/images/random_column.png)

Next, create a new sheet (*Sheet2*) and type in `=Sheet1!A1` in cell A1. Then drag the cell horizontally and vertically across to copy the formula all the way to Column L and Row 16. By doing this you have synced the first 15 rows of the data in the *Sheet1* to *Sheet2*. If you change any data in the first 15 rows of *Sheet1*, the corresponding data in *Sheet2* will automatically update.

:information_source: Note: If your first sheet is not named *Sheet1*, the formula you use in *Sheet2* should reflect the actual name. For instance, if your first sheet is called *mtcars*, the formula you enter in Cell A1 should be `=mtcars:A1` instead of `=Sheet1!A1`.

In cell A18, type "Mean" and in the cell next to it (B18), enter `=AVERAGE(B2:B16)`, which will calculate the average MPG for the sample (our sample statistic). Sheet2 should now look like the image below.

![Random Column](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/images/sample.png)

Now that our spreadsheet is set up properly for obtaining samples, we actually need to start randomly generating them. The way we are going to do that is by sorting our data in Sheet1 based on the Random column. Select all the data in the data set (cell range A1:M33), click Data from the menu and then choose the "Sort range..." option. In the pop-up box, check the box that says "Data has header row," choose the Random column to sort by, and then click the Sort button.

![Random Column](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/images/sort_range.png)

If you go to Sheet2 now, you will see a different set of rows and a different sample mean than we had previously.

![Random Column](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/images/sample_1.png)

Sheet2 is always going to sample the top 15 records, so by sorting by a randomly generated field, we will ensure that we are sampling properly.

### Generating a Sampling Distribution

Our spreadsheet is now set up properly for sampling, and we have successfully taken one random sample from our data. Now, we just need to repeat the sorting of the data and recording of the sample statistic a sufficient number of times to get a *sampling distribution*. In our case, let's take a total of 20 samples.

Below are the results I got.

**Sample**|**Mean**
:-----:|:-----:
1|19.40666667
2|18.74
3|20.58
4|21.43333333
5|21.92666667
6|21.60666667
7|19.09333333
8|18.66
9|18.36
10|20.74666667
11|20.88666667
12|18.24
13|20.21333333
14|18.00666667
15|18.71333333
16|20.83333333
17|20.33333333
18|19.98666667
19|20.43333333
20|19.68666667

The results you get might vary slightly, but from this sampling distribution, we can estimate that the true population mean is somewhere between 18 and 22 MPG. Although this is typically done using the mean as the sample statistic, you can also use the median, standard deviation, or any other statistic that you are trying to estimate for a population.

## Probability Distributions

Thus far in our studies of statistics, we have encountered frequency distributions and sampling distributions. Both distributions counted the number of times we observed values in our data, binned them into categories, and then presented us with the total number of observations in each category. This provided us with an idea of how often we are likely to see certain values.

Probability distributions are similar in that they also provide us with an idea of how often we are likely to see certain values, but instead of coming directly from the data we are working with, they come from some pre-defined probability function. From a practical perspective, when modeling a real-world scenario, you usually need to inject randomness into your simulation of the scenario. When this is the case, probability distributions come in very handy. There are many different probability distributions out there, but we will just focus on the following 4 for now.

* Normal Distribution
* Student's t-Distribution
* Binomial Distribution
* Discrete Uniform Distribution

### Normal Distribution

The *normal distribution* is one of the most well-known probability distributions. If you've ever heard someone refer to a bell curve, the normal distribution is what they were likely referring to. A normal distribution looks like this.

![Random Column](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/images/normal_distribution.png)

The normal distribution has the following properties:

* Approximately 68% of observations fall within 1 standard deviation (+ or -) around the mean.
* Approximately 95% of observations fall within 2 standard deviation (+ or -) around the mean.
* Approximately 99% of observations fall within 3 standard deviation (+ or -) around the mean.

We use μ to denote the mean and σ to denote the standard deviation in the normal distribution.

Typically the sample statistics you calculate, be they means from a sampling distribution or performance metrics for iterations of your machine learning models, for a large number of samples will be approximately normally distributed according to the Central Limit Theorem. According to the Central Limit Theorem, when we generate a large amount of samples and compute the mean for each sample, the distribution of those means will be approximately normally distributed. Note the use of the word *approximately* in the previous sentences. In the real-world, it is reasonable to find observations that are approximately normally distributed (heights, IQs, etc.) but very difficult to find examples that are truly normally distributed. Therefore, most of the time you use it, you will be making an approximation or assumption.

### Student's t-Distribution

The *student's t-distribution* is a normally shaped distribution, but its tails are little thicker and longer than those of the normal distribution. Whereas assuming a normal distribution can lead to underestimation of extreme events, longer-tailed distributions like the t-distribution can help reduce the risk of not considering them. It should be noted, however, that the larger your sample becomes, the more normally shaped the t-distribution becomes.

![Random Column](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/images/normal-vs-t.png)

### Bernoulli Distribution

The *Bernoulli distribution* is useful when you need to model a scenario where one of two independent outcomes is possible (usually referred to as a success and a failure) and there is some probability associated with each outcome. The classic example is a coin toss, where the probabilities of a success (heads) and a failure (tails) are both 50%. This is applicable to much more than a coin toss though. Which of two candidates is will win an election, which of two opposing teams will win at a game, and whether you'll get accepted into Ironhack's prestigious data analytics program are all examples of other real-life applications for the Bernoulli distribution.

### Discrete Uniform Distribution

The *discrete uniform distribution* is similar to the Bernoulli distribution, but instead of just two potential outcomes, there are multiple and they all have the same probability of occurring. The classic example for this is a roll of the dice. The dice has 6 sides and the probability of it landing on any side is the same. The discrete distribution would be used for modeling scenarios where you know that one of a specific number of events is going to occur and you're making an assumption that each event is going to be equally likely.

## Sampling from Probability Distributions

Now that we know a little bit about each of these distributions, let's take a look at how to sample from them using Google Sheets.

To obtain a random sample from the normal distribution, you would use the `NORMINV()` and `RAND()` formulas and then specify the mean and standard deviation which would determine the distribution's positioning and width.

```excel
=NORMINV(RAND(), mean, standard deviation)
```

To sample from the student's t-distribution, you would also use the `RAND()` formula, but this time inside the `T.INV()` formula, and you would specify the degrees of freedom for the distribution. The degrees of freedom...

```excel
=T.INV(RAND(), degrees of freedom)
```

For the Bernoulli and discrete uniform distributions, you would use the `RANDBETWEEN()` formula and enter the beginning and ending number of options or events. For Bernoulli, you would just use (0,1) to represent failures and successes whereas for discrete random, the second number would depend on the number of options.

```excel
=RANDBETWEEN(0, number of options)
```

## Summary

This lesson has covered a lot. We have learned about sampling, estimation of sample statistics, how to obtain samples in Google Sheets, and how to generate a sampling distribution. We also learned about probability distributions and how to sample from them using Google Sheets.

Working with these concepts in spreadsheets can sometimes be a bit tedious, but it helps solidify understanding of these concepts. Later in the program, once you have some additional Python experience, we can examine how to automate sampling and the recording of sample statistics, which will be a very useful tool to have in your analytics toolbox.
