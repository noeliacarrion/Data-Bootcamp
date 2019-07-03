![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Learn about relationships in data through correlation and regression

## Lesson Goals

In this lesson, you will learn the basics of correlation and regression including:

* Calculating correlation coefficients in Google Sheets.
* Creating a correlation matrix.
* Creating scatter plots to visualize relationships.
* Using linear regression to model relationships and make predictions.
* Calculating the coefficient of determination for linear regression.

## Introduction

In addition to calculating descriptive statistics for fields in your data, it is also important to examine how those fields are related to each other. Examining these field relationships is going to be the overarching theme of this lesson. We will look at a couple ways to analyze relationships between fields: correlation and regression.

Examining relationships between variables in data.

## Correlation

Correlation measures the strength of the linear relationship between two series of numeric variables. If the same directional variation is observed in both variables, they are said to have a positive correlation. If an opposite directional variation is observed among the variables, they are said to have a negative correlation. If they seem to be completely unrelated, then they are said to have no correlation. We can also observe other relationships between variables. In that case we say that there is association between variables. Correlation is a specific case of association where the relationship between variables is linear.

**Variable 1**|**Variable 2**|**Correlation**
:-----:|:-----:|:-----:
Increases|Increases|Positive
Decreases|Decreases|Positive
Increases|Decreases|Negative
Decreases|Increases|Negative
Increases or Decreases|Stays the Same|None
Stays the Same|Increase or Decrease|None

### Correlation Coefficient

Correlation is not so black and white, however. The strength of correlation between two variables can vary. The *correlation coefficient* tells us how strong of a correlation there is between variables and in what direction (positive or negative). The correlation coefficient for a set of variables can range from -1 (perfectly negatively correlated) to 1 (perfectly positively correlated). The closer to each of these values a correlation coefficient is (i.e. the further from zero), the stronger the correlation.

Let's revisit our cars data set in Google Sheets and calculate the correlation coefficient using the `CORREL` formula between some of the fields in *Sheet1*. We will start with the correlation between the MPG and Displacement fields.

```excel
=CORREL(B2:B33,D2:D33)

-0.8475513793
```

These two fields have a strong negative correlation, which tell us that the larger the engine, the less fuel efficient it is.

What about the correlation between Displacement and Horsepower?

```excel
=CORREL(D2:D33,E2:E33)

0.7909485864
```

:information_source: To learn more about the `CORREL` function, refer to the [Google Documentation](https://support.google.com/docs/answer/3093990?hl=en).

They have a strong positive correlation, indicating that the larger the engine, the more horsepower the car typically has.

### Correlation Matrix

Instead of looking at one correlation at a time, sometimes it is helpful to examine the correlations between all the numeric fields in your data to try to get an overall understanding of what correlations exist and how strong they are. The way to do this is to create a correlation matrix that calculates the correlation coefficient for every combination of numeric fields.

Below are step-by-step instructions for creating a correlation matrix in Google Sheets.

1. Copy and paste the field names for the numeric fields only (Column B to M) into a range of empty cells on your spreadsheet, leaving one empty column on the left.
1. Copy the numeric field names again and click the cursor in the second row of the left empty column (Cell A2).
1. From the menu, select *Edit*, then *Paste Special*, and then *Paste transposed*. That will paste the field names vertically across the rows instead of across the columns.
	![Paste Transposed](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/images/paste-transposed.png)

	You should now have an empty matrix, which we will fill in with correlation coefficients in the next steps. We will reference cells in the instructions below by their row/column name combinations in the matrix. For example, `MPG/Displacement` references the cell in Row "MPG" and Column "Displacement".

	![Empty Matrix](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/images/empty-matrix.png)

1. Select the cell located at `MPG/MPG`.
1. Type in formula `=CORREL($B$2:$B$33,B2:B33)` into that cell.

	:information_source: What's the difference between `B2` and `$B$2`? The former is called a *relative reference* while the latter is called an *absolute reference*. If you copy the formula containing relative references from a cell to another cell, Google Sheet will "intelligently" update the relative references in the formula based on the new cell's context. If you paste with the absolute reference, in contrast, Google Sheet will not update the reference.

1. Select Cell `MPG/MPG`, drag the cell rightward all the way to the end (Column "Carburators"). 
Check out cell `MPG/Cylinders`. You'll find the formula has been updated to `=CORREL($B$2:$B$33,C2:C33)`.
1. Select the cell located at `Cylinders/MPG`.
1. Type in formula `=CORREL($C$2:$C$33,B2:B33)`. Note that the first cell range of the formula is now referencing the Cylinders column in the original data.
1. Select Cell `Cylinders/MPG`, drag the cell rightward all the way to the end.
1. Repeat the same process for the rest of the rows in the matrix

When you are done, the resulting correlation matrix should look like the table below.

**Correl_Matrix**|**MPG**|**Cylinders**|**Displacement**|**Horsepower**|**Rear\_Axle\_Ratio**|**Weight (000)**|**Qtr\_Mile\_Time**|**Engine\_Shape**|**Transmission**|**Fwd\_Gears**|**Carburators**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
MPG|1|-0.8521619594|-0.8475513793|-0.7761683718|0.6811719078|-0.8676593765|0.4186840339|0.6640389191|0.5998324295|0.4802847573|-0.5509250739
Cylinders|-0.8521619594|1|0.9020328721|0.8324474527|-0.6999381138|0.7824957945|-0.5912420738|-0.8108117961|-0.5226070469|-0.4926865994|0.5269882937
Displacement|-0.8475513793|0.9020328721|1|0.7909485864|-0.7102139272|0.8879799221|-0.4336978808|-0.7104158908|-0.5912270401|-0.5555691986|0.3949768649
Horsepower|-0.7761683718|0.8324474527|0.7909485864|1|-0.4487591169|0.6587478873|-0.7082233889|-0.7230967374|-0.2432042572|-0.1257042582|0.7498124715
Rear\_Axle\_Ratio|0.6811719078|-0.6999381138|-0.7102139272|-0.4487591169|1|-0.7124406467|0.09120475965|0.440278465|0.7127111272|0.6996101319|-0.09078979887
Weight (000)|-0.8676593765|0.7824957945|0.8879799221|0.6587478873|-0.7124406467|1|-0.1747158787|-0.5549156777|-0.6924952588|-0.5832869965|0.4276059377
Qtr\_Mile\_Time|0.4186840339|-0.5912420738|-0.4336978808|-0.7082233889|0.09120475965|-0.1747158787|1|0.7445354435|-0.2298608622|-0.2126822297|-0.6562492283
Engine\_Shape|0.6640389191|-0.8108117961|-0.7104158908|-0.7230967374|0.440278465|-0.5549156777|0.7445354435|1|0.1683451246|0.2060233487|-0.569607141
Transmission|0.5998324295|-0.5226070469|-0.5912270401|-0.2432042572|0.7127111272|-0.6924952588|-0.2298608622|0.1683451246|1|0.7940587603|0.05753435107
Fwd\_Gears|0.4802847573|-0.4926865994|-0.5555691986|-0.1257042582|0.6996101319|-0.5832869965|-0.2126822297|0.2060233487|0.7940587603|1|0.2740728364
Carburators|-0.5509250739|0.5269882937|0.3949768649|0.7498124715|-0.09078979887|0.4276059377|-0.6562492283|-0.569607141|0.05753435107|0.2740728364|1

Note that there is a diagonal line of 1's going across the matrix where the correlation is being obtained between each field and itself, which understandably results in a perfect positive correlation. The data on both side of this diagonal like of 1's is a mirror image of the other side. For example, Cell `MPG/Horsepower` has exactly the same value as Cell `Horsepower/MPG`. Therefore, you really only need to pay attention to either the top half or bottom half of the matrix.

## Scatter Plots

In addition to calculating the correlation coefficient of two variables, you can also plot their data points using a scatter plot to see how they relate to each other and also to identify any anomalies. Below are the instructions for creating a scatter plot showing Displacement vs. MPG in Google Sheets.

1. Select columns B and D.
	
	:bulb: Tip: Hold down the *Command* key (Mac) or the *Ctrl* key (Windows) to select multiple columns in Google Sheets. Hold down the *Shift* key to select all columns between two columns.

1. From the menu, select *Insert* and then choose *Chart*.
1. A chart should display accompanied by the Chart Editor on the right-hand side of the screen.
1. In the Chart Editor, choose *Scatter* from the Chart Type drop-down menu.

Your results should look like the plot below.

![Displacement vs. MPG](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/images/displ_mpg_scatter.png)

We can see that as Displacement decreases, MPG generally increases, further confirming the strong negative correlation we concluded from their correlation coefficient in the previous section.

## Linear Regression

Regression is another way to examine the relationships between variables. While correlation measures the strength and direction relationships between variables, regression allows us to model the relationship and even generate predictions about what values of one variable we could expect given values of another variable. There are different methods for performing regression, but in this section, we are going to focus on one of the simplest: linear regression.

Linear regression is a technique for computing the best fit straight line through all the data points. Remember the formula `y = mx + b` from the algebra classes you took in school? Here is where that formula is going to help you in your data analysis career. The formula is made up of the following components.

* **Dependent Variable (y):** the target variable that you are trying to figure out how is affected.
* **Independent Variable (x):** the variable that you are trying to see how influences the dependent variable.
* **Slope (m):** the angle of the regression line that runs through
* **Intercept (b):** the value of the dependent variable when the independent variable is zero.


Let's see how this applies to our cars data set. In the previous sections, we saw that MPG and Displacement were negatively correlated and we created a scatter plot that showed us the data points and we visually witnessed how MPG increases as Displacement decreases. Now, suppose we wanted to model that relationship, look at specifically *how* MPG changes based on the Displacement of a car's engine, and be able to predict what the MPG of a car whose Displacement we already know. In other words, MPG is going to be the dependent variable and Displacement is going to be our independent variable. Here is what the linear equation is going to look like.

```excel
MPG = (m x Displacement) + b
```

How do we get the slope (m) and the intercept (b)? We fit a best-fit line to the data. Google Sheets lets us do that easily with the `LINEST` formula. We just need to specify the cell ranges containing the known values for our dependent and independent variables (the MPG and Displacement columns in our original data set).

```excel
=LINEST(B2:B33,D2:D33)

-0.04121511996	29.59985476
```

Google Sheets returns two values. The first value is the slope of the regression line and the second value is the intercept. We have now modeled the relationship between Displacement and MPG and are ready to generate predictions. First, we will do this manually and then we will look at how to do it in Google Sheets.

Let's say we know that the displacement of a particular vehicle is 160. Based on the data we have and what we know about it, how fuel efficient can we expect that vehicle to be? What MPG can we expect for it?

```excel
(-0.04121511996 x 160) + 29.59985476 = 23.00543556
```

We can expect a vehicle with a displacement of 160 to have an MPG of 23! If we didn't want to perform this calculation manually, we could do do it in Google Sheets using the `FORECAST` formula as follows.

```excel
=FORECAST(160,B2:B33,D2:D33)

23.00543556
```

Another thing that we can use to describe a variable's impact on another is the coefficient of variation, commonly referred to as R-squared. The coefficient of variation for linear regression is easy to calculate (it is just the correlation coefficient squared) and it tells us the amount of variability in a variable that is explained by the model.

The correlation coefficient for MPG and Displacement was -0.8475513793, so R-squared would be 0.7183433405 (-0.8475513793 squared), meaning that 71.8% of the variability of MPG can be explained by the vehicle's displacement. Later in the program, we will use R-squared as an evaluation metric for comparing the performance of different machine learning models, so make sure you understand this concept.

The final thing we will cover in this lesson is how to add a linear regression line to your scatter plots in Google Sheets. Below are the instructions for doing that.

1. Select your scatter plot chart (you may need to double-click on it) so that the Chart Editor appears on the right hand side of the screen.
1. In the Chart Editor click on the *Customize* tab and then expand the *Series* section.
1. Click the checkbox next to the *Trendline* option, and you should see a regression line appear in your scatter plot chart.
1. If you like, you can also click on the *Show R<sup>2</sup>* checkbox to show the R-squared value in the chart's legend.

Your scatter plot chart should now look like the example below.

![Scatter Plot Regression](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/images/scatter-regression.png)

## Summary

This lesson focused on examining and analyzing relationships between variables in our data. First, we introduced correlation coefficients and how to calculate them in Google Sheets. Then we covered how to look at correlation coefficients for all the numerical fields in our data by creating a correlation matrix. From there, we visualized relationships with scatter plots before moving on to regression, showing how to model variable relationships, make predictions, and calculate the coefficient of determination. Finally, we tied all these concepts together by learning how to add a regression line to our scatter plots.

As with the other topics you have learned about in this chapter, the concepts we have covered here in this Correlation and Regression lesson, will help form the foundation you will build upon as you tackle more advanced topics in data analytics. Make sure you understand them and, perhaps even more importantly, practice creating scatter plots and running regressions on other pairs of variables in the data set so that you get the hang of it.