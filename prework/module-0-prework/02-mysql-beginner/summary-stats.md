![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Learn how to calculate summary statistics in MySQL

## Lesson Goals

In this lesson, you will learn how to summarize data with SQL including:

* Grouping data and removing duplicates.
* Counting records and distinct categories.
* Totaling up values by summing.
* Including averages in your summaries.
* Adding conditions and filtering to your summaries.

## Introduction

Grouping and summarizing are foundational components of data analysis. As humans, we are not very good at finding insights in granular details, so grouping and summarizing data helps us look at things from further away so that we can observe patterns. When it comes making decisions about something we are examining, it is helpful to know how alike or different its behavior is to other things that have similar attributes, and grouping and summarizing helps us with this as well.

In this lesson, we are going to continue using the Ratings table in the Apps database from the previous lesson and illustrate how grouping and summarizing can help you manipulate data and extract insights.

## Grouping in SQL

Suppose we want to see a list of the unique genres in our Ratings table. If we just ran a regular `SELECT` query and selected that field from the Ratings table, we would have a lot of duplicates. Fortunately, we can use the `GROUP BY` command to group the data by Genre so that each genre gets listed only once.

```sql
SELECT Genre
FROM Ratings
GROUP BY Genre;
```

```text
Genre
Games
Productivity
Weather
Shopping
Reference
...
```

We can apply this same logic to group by any field in our table. For example, if we wanted to see the price range for apps, we could obtain that as follows.

```sql
SELECT Price
FROM Ratings
GROUP BY Price
ORDER BY Price ASC;
```

```text
Price
0
0.99
1.99
2.99
3.99
...
59.99
74.99
99.99
249.99
299.99
```

From the results, we can see that prices for apps range from free ($0) to $299.

We can even group by multiple fields to see prices by genre.

```sql
SELECT Genre, Price
FROM Ratings
GROUP BY Genre, Price
ORDER BY Genre ASC, Price ASC;
```

From our results, we can see that the highest priced apps ($249 and $299) are in the Education genre.

## Summary Statistics: Counting

In addition to grouping our data, we can also calculate summary statistics. The simplest example is just counting the number of records in a table. We can do that using the `COUNT` command.

```sql
SELECT COUNT(*)
FROM Ratings;
```

```text
Count(*)
7197
```

In one of the examples in the previous section, we grouped by Genre, but what if we wanted to know the total number of unique genres in our data? We could apply the `DISTINCT` command to the Genre field inside our `COUNT` command to get that. In other words, we are counting the distinct number of genres.

```sql
SELECT COUNT(DISTINCT(Genre))
FROM Ratings;
```

```text
COUNT(DISTINCT(Genre))
23
```

Now we know that there are 23 distinct genres in our data. Next, let's group by Genre and count the number of records in each genre.

```sql
SELECT Genre, COUNT(*) AS Records
FROM Ratings
GROUP BY Genre;
```

**Genre**|**Records**
-----|-----
Games|3862
Productivity|178
Weather|72
Shopping|122
Reference|64
Finance|104

Note that we also used an `AS` statement to change the name of the column that held the record counts. You can use the same approach to change the name of any column your queries return.

Next, let's add sorting and limiting to our query to get the top 3 genres with the most apps.

```sql
SELECT Genre, COUNT(*) AS Records
FROM Ratings
GROUP BY Genre
ORDER BY COUNT(*) DESC
LIMIT 3;
```

**Genre**|**Records**
-----|-----
Games|3862
Entertainment|535
Education|453

From our results, we can see that there are 3,862 apps in the Games genre, 535 apps in the Entertainment genre, and 453 apps in the Education genre.

## Summary Statistics: Summing

Suppose we also wanted to do some analysis on app ratings and see what genre has had the most number of ratings. We can apply the `SUM` command to the TotalRatings field while maintaining our grouping by Genre.

```sql
SELECT Genre, SUM(TotalRatings) AS TotalRatings
FROM Ratings
GROUP BY Genre
ORDER BY SUM(TotalRatings) DESC;
```

**Genre**|**TotalRatings**
-----|-----
Games|52878491
Social Networking|7598316
Photo & Video|5008946
Entertainment|4030518
Music|3980199

Judging from the results, it looks like the most rated genres are Games, Social Networking, and Photo & Video.

## Summary Statistics: Averaging

Next, let's get the average overall rating for each genre and add it to our query results. We can do this by applying the `AVG` command to the OverallRating field as follows.

```sql
SELECT Genre, SUM(TotalRatings) AS TotalRatings, AVG(OverallRating) AS AvgRating
FROM Ratings
GROUP BY Genre
ORDER BY SUM(TotalRatings) DESC;
```

**Genre**|**TotalRatings**|**AvgRating**
-----|-----|-----
Games|52878491|3.685007768
Social Networking|7598316|2.98502994
Photo & Video|5008946|3.800859599
Entertainment|4030518|3.246728972
Music|3980199|3.97826087

## Summary Statistics: Adding Conditions

Finally, let's filter our results for just free apps by adding a `WHERE` clause and limit our results to the top 5 apps with the most total ratings.

```sql
SELECT Genre, SUM(TotalRatings) AS TotalRatings, AVG(OverallRating) AS AvgRating
FROM Ratings
WHERE Price = 0
GROUP BY Genre
ORDER BY SUM(TotalRatings) DESC
LIMIT 5;
```

**Genre**|**TotalRatings**|**AvgRating**
-----|-----|-----
Games|42713023|3.528577758
Social Networking|7590182|2.996503497
Photo & Video|4550732|3.793413174
Music|3784296|3.940298507
Entertainment|3614869|3.148203593

From our results, we can see that Music apps are rated the most highly out of the top 5 whereas Social Networking apps are rated the lowest.

## Summary

In this lesson, we have built on the previous lesson's examples, incorporating grouping and summarization to view our data from a few different perspectives. We have taken an approach where we first present a simple example and then add sophistication layer by layer to illustrate the process of building more complex queries, which we will see later in the program. Hopefully this approach is intuitive, and you can take the concepts you have learned here and use them to answer additional questions you may have about our Ratings data set.