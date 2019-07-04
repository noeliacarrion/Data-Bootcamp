![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Web Scraping

## Lesson Goals

* Learn the basics of scraping content from web pages.
* Perform scraping of text from a web page.
* Perform extraction of an HTML table from a web page into a Pandas data frame.

## Introduction

Web scraping refers to the automatic extraction of information from a web page. This information is often a page's content, but it can also include information in the page's headers, links present on the page, or any other information embedded in the page's HTML. Because of this, scraping has become one of the most popular ways to extract data from the web. With basic knowledge of HTML and the help of a few Python libraries, you can obtain information from just about any page on the internet.

In this lesson, we will cover the basics of web scraping with Python and show examples of how to scrape text content from a simple web page as well the more complex task of extracting data from an HTML table embedded on a web page.

## Scraping a Simple Web Page

Scraping a simple website is relatively straightforward. The first thing we need to do is determine the web page we want to scrape and the information we would like to obtain from it. For our purposes, let's suppose we wanted to scrape a Reuters news article and we wanted to extract the main text content (article title, story, etc.).

We first need to specify the URL of the page we want to scrape and then use the requests library's `get` method to request the page and the `content` method to retrieve the HTML content.

```python
import requests

url = 'https://www.reuters.com/article/us-shazam-m-a-apple-eu/eu-clears-apples-purchase-of-shazam-idUSKCN1LM1TZ'
html = requests.get(url).content
html
```

```text
b'<!--[if !IE]> This has been served from cache <![endif]-->\n<!--[if !IE]> Request served from apache server: produs--i-0758d3a2a706a519d <![endif]-->\n<!--[if !IE]> Cached on Thu, 06 Sep 2018 14:41:34 GMT and will expire on Thu, 06 Sep 2018 14:56:33 GMT <![endif]-->\n<!--[if !IE]> token: acbf5604-af64-471f-8f8b-8d010b921037 <![endif]-->\n<!--[if !IE]> App Server /produs--i-00127219d2753366b/ <![endif]-->\n\n<!doctype html><html lang="en" data-edition="BETAUS">\n    <head>\n\n    <title>\n                EU clears Apple\'s purchase of Shazam | Reuters</title>
...
```

As you can see, there is a lot of extra information here that we don't really need if all we are interested in is the text content from the page. We will need to perform a few steps to clean this up, the first of which is to use the BeautifulSoup library to read the raw HTML and structure it in a way where we will be able to more easily parse the information we want out of it. In BeautifulSoup terms, this is called "making the soup."

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "lxml")
soup
```

```text
<!--[if !IE]> This has been served from cache <![endif]--><!--[if !IE]> Request served from apache server: produs--i-0758d3a2a706a519d <![endif]--><!--[if !IE]> Cached on Thu, 06 Sep 2018 14:41:34 GMT and will expire on Thu, 06 Sep 2018 14:56:33 GMT <![endif]--><!--[if !IE]> token: acbf5604-af64-471f-8f8b-8d010b921037 <![endif]--><!--[if !IE]> App Server /produs--i-00127219d2753366b/ <![endif]--><!DOCTYPE html>
<html data-edition="BETAUS" lang="en">
<head>
<title>
                EU clears Apple's purchase of Shazam | Reuters</title>
...
```

You can see that our soup is slightly more structured than our raw HTML, but the best part about BeautifulSoup comes next. It allows us to extract specific HTML elements from the soup we have created using the `find_all` method. In our case, we are going to use it to find and extract all the text contained within header tags and paragraph tags.

```python
tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'p']
text = [element.text for element in soup.find_all(tags)]
text
```

```text
["EU clears Apple's purchase of Shazam",
 '2 Min Read',
 'BRUSSELS (Reuters) - The European Union approved Apple’s planned acquisition of British music discovery app Shazam on Thursday, saying an EU antitrust investigation showed it would not harm competition in the bloc. ',
 'The deal, announced in December last year, would help the iPhone maker better compete with Spotify, the industry leader in music streaming services. Shazam identifies songs when a smartphone is pointed at an audio source. ',
 '“After thoroughly analyzing Shazam’s user and music data, we found that their acquisition by Apple would not reduce competition in the digital music streaming market,” EU competition commissioner Margrethe Vestager said in a statement. ',
 '“Data is key in the digital economy. We must therefore carefully review transactions which lead to the acquisition of important sets of data, including potentially commercially sensitive ones,” she added. ',
 'The European Commission opened a full-scale investigation into the deal in April, emblematic of its recent worries that companies may buy a data-rich rival to mine it for information or drive others out of the market. ',
 'Reuters last month reported sources saying that Apple was set to win unconditional EU antitrust approval for the deal following the probe requested by seven European countries including France, Italy, Spain and Sweden. ',
 'Reporting by Alissa de Carbonnel; Editing by Alastair Macdonald',
 'All quotes delayed a minimum of 15 minutes. See here for a complete list of exchanges and delays.',
 '© 2018 Reuters. All Rights Reserved.']
```

This gives us a neat list where the text of each HTML element BeautifulSoup found is an element in the list. If we want to view it in paragraph form, we can simply call the `join` method, use a new line (\n) to join the elements together, and we get the text neatly in paragraph form.

```python
print('\n'.join(text))
```

```text
EU clears Apple's purchase of Shazam
2 Min Read
BRUSSELS (Reuters) - The European Union approved Apple’s planned acquisition of British music discovery app Shazam on Thursday, saying an EU antitrust investigation showed it would not harm competition in the bloc. 
The deal, announced in December last year, would help the iPhone maker better compete with Spotify, the industry leader in music streaming services. Shazam identifies songs when a smartphone is pointed at an audio source. 
“After thoroughly analyzing Shazam’s user and music data, we found that their acquisition by Apple would not reduce competition in the digital music streaming market,” EU competition commissioner Margrethe Vestager said in a statement. 
“Data is key in the digital economy. We must therefore carefully review transactions which lead to the acquisition of important sets of data, including potentially commercially sensitive ones,” she added. 
The European Commission opened a full-scale investigation into the deal in April, emblematic of its recent worries that companies may buy a data-rich rival to mine it for information or drive others out of the market. 
Reuters last month reported sources saying that Apple was set to win unconditional EU antitrust approval for the deal following the probe requested by seven European countries including France, Italy, Spain and Sweden. 
Reporting by Alissa de Carbonnel; Editing by Alastair Macdonald
All quotes delayed a minimum of 15 minutes. See here for a complete list of exchanges and delays.
© 2018 Reuters. All Rights Reserved.
```

## More Complex Single-Page Scraping

The previous example was relatively straightforward because we were just extracting the text content from the page. Suppose however, we wanted to extract data that was contained within an HTML table and store it in a Pandas data frame. This objective makes our scraping task a bit more complex as we would need to identify the table within the HTML, identify the rows within the table, and then read and format the information within those rows so that they fit within a data frame. Let's look at an example of how we would extract a table containing life expectancies for each European country from Wikipedia.

This task would start out just like the previous one. We would specify the URL, use the requests library to request the page and retrieve the raw HTML content, and turn the HTML into soup using BeautifulSoup.

```python
url = 'https://en.wikipedia.org/wiki/List_of_European_countries_by_life_expectancy'
html = requests.get(url).content
soup = BeautifulSoup(html, "lxml")
```

Once we have our soup, we need to extract the table containing each country's life expectancy. You can look at the page source in a browser to determine whether you can specify a class for it. In the case of our table, it did have a class of "sortable wikitable" so we will use that as well as the index [0] to get just the single table we want.

```python
table = soup.find_all('table',{'class':'sortable wikitable'})[0]
table
```

```text
<table class="sortable wikitable">
<tbody><tr bgcolor="#efefef">
<th>Country</th>
<th><a href="/wiki/List_of_countries_by_life_expectancy" title="List of countries by life expectancy">Life expectancy</a>
</th></tr>
<tr>
<td><span class="flagicon"><img alt="" class="thumbborder" data-file-height="500" data-file-width="700" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/3/36/Flag_of_Albania.svg/21px-Flag_of_Albania.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/3/36/Flag_of_Albania.svg/32px-Flag_of_Albania.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/3/36/Flag_of_Albania.svg/42px-Flag_of_Albania.svg.png 2x" width="21"/> </span>Albania</td>
<td>72
</td></tr>
...
```

We now have the table we want, but to be able to load the data into Pandas, we need to extract each of the rows and their cell values into a list comprehension.

```python
rows = table.find_all('tr')
rows = [row.text.strip().split("\n") for row in rows]
rows
```

```text
[['Country', 'Life expectancy'],
 ['Albania', '72'],
 ['Austria', '82'],
 ['Belarus', '74'],
 ['Belgium', '81'],
 ['Bosnia and Herzegovina', '77'],
 ['Bulgaria', '75'],
 ['Croatia', '77'],
 ['Cyprus', '80'],
 ['Czech Republic', '79'],
 ...
```

From this list comprehension, we can specify what the column names are and then use the rest of the data to populate a data frame.

```python
colnames = rows[0]
data = rows[1:]

df = pd.DataFrame(data, columns=colnames)
df
```

![Life Expectancy Data Frame](../../../static/images/life-expectancy-dataframe.png)

## Web Scraping Challenges

The two scraping tasks we performed in this lesson were possible because the web pages were created with HTML. It is important to note that this is not always the case and that it will make your scraping efforts more difficult (if not impossible) when it is not.

Aside from this, there are several other factors that may present challenges when performing web scraping. Below is a list of challenges and considerations that should be helpful to keep in mind while performing web scraping.

* Need to determine what information you want to extract from each page.
* Consider creating a customized scraper for each site to account for different formatting from one site to the next.
* Consider that different pages within the same site may have different structure.
* Consider that a page's content and structure can change periodically.
* Terms of service for a website may not allow for scraping of their pages.

## Summary

In this lesson, we covered the basics of web scraping. We began by looking at an example of how we can scrape text from a web page using Python's requests and BeautifulSoup libraries. We then studied a more complex example where we had to extract a specific table from the HTML of a web page and then extract the rows of that table so that we could load them into a Pandas data frame. We finished up the chapter by noting some important challenges and considerations you should keep in mind while scraping. Now that you have completed this lesson, you should have the skills you need to obtain data from web pages and structure it in a way where it can be analyzed.
