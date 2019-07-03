![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Challenge: Install Jupyter Notebook

![Jupyter](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/images/jupyter.svg)

## Introduction

[Project Jupyter](http://jupyter.org/about) is a non-profit, open-source project dedicated to supporting interactive data science and scientific computing. It has been widely used by data scientists and analysts in working with data. In this course we will use Jupyter Notebook as the main workspace for the hands-on work because it is very convenient to compile and test your Python code in Jupyter Notebook.

## Install Jupyter Notebook

There are three ways to install Jupyter Notebook. The first way works for Mac users in which they can install with Homebrew:

```
$ brew install jupyter
```

The second way (also for Mac users) is to use pip to install Jupyter Notebook. [Pip](https://pypi.org/project/pip/) is a package management tool for Python, just like Homebrew which is a package management tool for Mac. Pip is installed by default with Python so you don't have to install it separately. But you'll want to upgrade pip before using it to install Jupyter Notebook:

```
$ python3 -m pip install --upgrade pip
$ python3 -m pip install jupyter
```

The third way is to install Jupyter Notebook with the [Anaconda Distribution](https://www.anaconda.com/download/). This option is recommended for Windows users but it will also work for Mac users. Anaconda will install Python, Jupyter Notebook, and other commonly used packages useful in scientific computing and data science. Just make sure to download the Python 3.6 version instead of 2.7.

:bulb: Tip: Anaconda is a little behind the latest development of Python. But it should work for this course without any problem because there is almost no syntax difference between Python 3.6 and 3.7.

### Is it working?

After installing Jupyter Notebook, run the following command in the terminal to launch it. Jupyter Notebook will be served from the directory where you run the command.

```
$ jupyter notebook
[I 22:49:03.262 NotebookApp] Serving notebooks from local directory: /Users/CurrentUser/Desktop
[I 22:49:03.262 NotebookApp] 0 active kernels
[I 22:49:03.262 NotebookApp] The Jupyter Notebook is running at:
[I 22:49:03.262 NotebookApp] http://localhost:8888/?token=8fcea448502a9a9f26533e446744bd71e64890f9f35e219c
[I 22:49:03.262 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 22:49:03.267 NotebookApp]

    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://localhost:8888/?token=8fcea448502a9a9f26533e446744bd71e64890f9f35e219c&token=8fcea448502a9a9f26533e446744bd71e64890f9f35e219c
[I 22:49:03.440 NotebookApp] Accepting one-time-token-authenticated connection from ::1
```

A new browser tab should be automatically opened which looks like the following (depending on where you launched Jupyter Notebook):

![Jupyter Notebook](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/images/jupyter-notebook.png)

If you encounter any problem in installing or using Jupyter Notebook, refer to the official [installation instructions](http://jupyter.org/install) and [documentation](http://jupyter.org/documentation).

## Summary

In this challenge we installed Jupyter Notebook, which will be the main workspace of your hands-on work with Python and data analysis in this course. There is a multi-user version of Jupyter called the [JupyterHub](http://jupyter.org/hub). A lot of companies host JupyterHub for their data analysts, data scientists, and software engineers to collaborate on data projects. 
