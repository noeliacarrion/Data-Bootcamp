![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Working with APIs

## Lesson Goals

* Learn how to make simple calls to an API and retrieve JSON data.
* Learn how to handle nested JSON API results.
* Learn about API authentication.
* Learn how to use Python wrappers for popular APIs.

## Introduction

Thus far in the program, we have learned how to obtain data from files and from relational databases. However, sometimes the data we need is not readily available via one of these two data sources. In some cases, the data we need may be contained within an application. Application owners will often create APIs (or Application Programming Interface) so that their applications can talk to other applications. The API is a set of programmatic instructions for accessing the software application, and the data that comes from an API typically contains some sort of structure (such as JSON). This structure makes working with API data preferable to crawling websites and scraping content off of web pages.

In this lesson, we are going to learn how to make API calls to an application, retrieve data in JSON format, learn about API authentication, and use Python libraries to obtain data from APIs.

## Simple API Example with Requests

There are a few libraries that can be used for working with APIs in Python, but the *requests* library is one of the most intuitive. It has a `get` method that allows you to send an HTTP request to an application and receive a response. Let's take a look at a basic API call using the requests library.

```python
import json
import requests

response = requests.get('https://jsonplaceholder.typicode.com/todos')
results = response.json()
results
```

```text
[{'completed': False, 'id': 1, 'title': 'delectus aut autem', 'userId': 1},
 {'completed': False,
  'id': 2,
  'title': 'quis ut nam facilis et officia qui',
  'userId': 1},
 {'completed': False, 'id': 3, 'title': 'fugiat veniam minus', 'userId': 1},
 {'completed': True, 'id': 4, 'title': 'et porro tempora', 'userId': 1},
 {'completed': False,
  'id': 5,
  'title': 'laboriosam mollitia et enim quasi adipisci quia provident illum',
  'userId': 1},
...
```

In this example, we used the `get` method to send a request to the JSONPlaceholder API, and we received back a response in the form of JSON structured data. If we wanted to analyze this data, we could easily use Pandas to convert the response data into a data frame to which we can then apply various analytical methods.

```python
import pandas as pd

data = pd.DataFrame(results)
data.head(10)
```

![Simple API Results](../../../static/images/simple-api-results.png)

## More Complex Requests API Example

In the previous section, the data we received from the API was not very complex. It was all at a single level and fit neatly into a data frame. However, sometimes API responses contain data that is nested and we have to find a way to flatten the JSON data so that it fits nicely into a data frame. Let's make an API call to the the Github public API, create a Pandas data frame from the results, and examine the structure of the data.

```python
response = requests.get('https://api.github.com/events')

data = pd.DataFrame(response.json())
data.head(10)
```

![Nested API Results](../../../static/images/nested-api-results.png)

When we look at the data frame, we can see that there are dictionaries nested in several fields. We need to extract the information that is in these fields and add them to the data frame as columns. To do this, we are going to create our own `flatten` function that accepts a data frame and a list of columns that contain nested dictionaries in them. Our function is going to iterate through the columns and, for each column, it is going to:

* Turn the nested dictionaries into a data frame with a column for each key
* Assign column names to each column in this new data frame
* Add these new columns to the original data frame
* Drop the column with the nested dictionaries

```python
def flatten(data, col_list):
    for column in col_list:
        flattened = pd.DataFrame(dict(data[column])).transpose()
        columns = [str(col) for col in flattened.columns]
        flattened.columns = [column + '_' + colname for colname in columns]
        data = pd.concat([data, flattened], axis=1)
        data = data.drop(column, axis=1)
    return data
```

Now that we have our function, let's apply it to the columns that have nested dictionaries and get back a revised data frame.

```python
nested_columns = ['actor', 'org', 'payload', 'repo']

flat = flatten(data, nested_columns)
flat.head(10)
```

![Flattened API Results](../../../static/images/flattened-api-results.png)

This data looks much cleaner, and now we have access to the information that was enclosed within those dictionaries. Sometimes multiple rounds of flattening will be required if the JSON data returned from the API you are working with has hierarchically nested data.

## Authentication and Python API Wrappers

The examples we have used so far in this lesson requested information from public APIs. For these APIs, authorization was not required. However, most application that you will want to request data from (social networks, search engines, etc.) will want to know who is accessing their application, how they plan on doing so, and what they plan to do with the data.

For these popular applications, there are also Python wrappers that have been written for their APIs that make interacting with them much easier than it would be otherwise. One example is the *tweepy* library that makes obtaining data from the Twitter API relatively simple.

Before we can use it, we need to create a developer account (if we don't already have one, create an application, and obtain credentials from Twitter. To create a developer account, follow the steps below.

* Go to https://developer.twitter.com/en/apply-for-access.html.
* Click *Apply for a developer account*.
* Follow the instructions and provide the information necessary to create a developer account for personal use.
* Twitter will review your application and approve your account (assuming you didn't say you would do anything that violates their terms of service).

After receiving confirmation that your developer account has been approved, you must create an application by logging into your account and following the steps to create a new app. Once the app has been created, the next step is to obtain your credentials. These credentials will give you permission to access the Twitter API. The credentials consist of an API key, API secret key, access token, and access token secret. They can be found by viewing the details of your app and clicking on the *Keys and Tokens* tab.

**Warning:** You should store your credentials in a safe place, never share them, and never upload them to Github.

Now that we have obtained our credentials, we can use tweepy to access the Twitter API as follows. You will need to replace the credentials below with your actual credentials for this code to function.

```python
import tweepy

API_KEY = "YourAPIKey"
API_SECRET = "YourAPISecret"
ACCESS_TOKEN = "YourAccessToken"
ACCESS_TOKEN_SECRET = "YourAccessTokenSecret"

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
```

We can now create a function that will send some sort of request to the Twitter API. For example, suppose we wanted to create a data frame that contained 100 users that follow Ironhack on Twitter. We could construct a `get_followers` function that leverages tweepy's `followers` method, create a list comprehension of the results, and then turn that into a data frame.

```python
def get_followers(user, count=100):
    results = api.followers(user, count=count)
    followers = [pd.Series(follower._json) for follower in ironhack]
    df = pd.DataFrame(followers)
    return df

ironhack = get_followers('ironhack')
ironhack.head(10)
```

![Ironhack Twitter Followers](../../../static/images/api-ironhack-followers.png)

**Challenge:** The tweepy library has many more [methods](https://tweepy.readthedocs.io/en/v3.6.0/index.html) for interacting with the Twitter API. Practice writing functions for getting a user's profile information or getting tweets from a user's timeline.

## Summary

In this lesson, we covered the basics of working with APIs. We began by introducing the *requests* library and showing how to make a simple API call using it. We then obtained some more complex JSON data from an API, where the information was nested, and learned how to flatten it. We also discussed the need for authentication and the steps needed to register a developer account and create an app with Twitter. Finally, we saw how useful Python wrappers for APIs, such as the tweepy library, can be for interacting with web applications.
