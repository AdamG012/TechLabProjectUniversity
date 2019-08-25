# README #

Welcome to The Trend Report, group P10's project for COMP3615.

Please see [the wiki index](https://bitbucket.org/p10-2017/the-trend-report/wiki/Home) for all relevant project info.

[The Trend Report Website (live version).](http://trends.techlab.works)


## How do I get set up? ##


### Get the code and version control ###

Download SourceTree:
https://www.sourcetreeapp.com/


Go to our BitBucket repo: https://bitbucket.org/p10-2017/the-trend-report/overview

Check out the code: Click the download icon underneath "Overview" and click "Clone in SourceTree"


### Edit the code ###

Download PyCharm IDE: https://www.jetbrains.com/pycharm/

Once you've installed it, open your repo folder from above (the-trend-report).


### Run the code ###

**Download and install Django**

Details: https://docs.djangoproject.com/en/1.11/topics/install/#installing-official-release

Summary:

- Install pip (assumes you already have Python **3**)
- Install Django


**Install MySQL server and SequelPro**

MySQL: https://dev.mysql.com/downloads/mysql/

SequelPro: https://www.sequelpro.com/

- Create a database user called trend_report with password p102017
- Create an empty database called trend_report


**Install Python MySQL wrapper**

Details: https://docs.djangoproject.com/en/1.11/ref/databases/#mysql-notes

Summary:
- Install MySQL client https://pypi.python.org/pypi/mysqlclient



**Run Django!**

`$ cd University/2017/COMP3615/the-trend-report/p10`  (or wherever it is on your system)

`$ python manage.py runserver`


### Test setup instructions

A test database has been named in the settings.py file: 'test_trend_report'

If the 'trend_report' user cannot create/ access the test database, grant the user all privileges in mysql with:
`GRANT ALL PRIVILEGES ON *.* TO 'trend_report'@'localhost';`
`FLUSH PRIVILEGES;`

Unit tests use mock models, views etc... to install mock:

`$ pip install mock`
`$ pip install mock_django`

### Run tests

#### Unit Tests

To run all automated tests:
`$ python manage.py test trendreport`

To run all tests with a list of all tests (with speed up):
`$ python manage.py test trendreport --parallel -v 2`

To run tests with a specific tag(s):
`$ python manage.py test trendreport --tag=tag_name_goes_here`

##### Optional extra: 

install coverage.py

`$ coverage run --source='.' manage.py test trendreport`

`$ coverage report`

## Database Instructions ##
*For the below, replace `pip` with `pip3` depending on your environment.*

*Also replace `python` with `python3` or `py` depending on your environment*
### Install django-tables2 API ###
This is required to display the automatically formatted tables. These are used mostly for testing but will be required for your code to run:

`$ pip install django-tables2`

This is required to install Pillow which is deals with images that the client might upload:

`pip install pillow`

This is required to install CKEditor which is the API that we are using for rich text integration:

`pip install django-ckeditor`

This is requred to install [taggit](https://django-taggit.readthedocs.io/en/latest/forms.html)

`pip install django-taggit`

### Setup database to default values ###
To create and populate the database with default values, run:

`$ python setup-database.py [python/python3/py]`

The last argument depends on what command you use to run the script.

Follow the prompts to create a user account for the admin page.
### Get database structures to update ###
In terminal, navigate to the p10 folder where manage.py is.

#### Automatic Mode ####
To do all of the following automatically, run:

`$ python update_database.py [python/python3/py]`

The last argument depends on what command you use to run the script.

#### Manual Mode ####
To do this manually, the following commands are used:

To display a list of the database structures currently in your database use

`$ python manage.py showmigrations trendreport`

You will see a [] for the structures that exist in the code but are not in your database, and a [x] for those that are installed in the database.


To gather the information from your code about which the structures that need to be updated use

`$ python manage.py makemigrations trendreport`


To update your local database with the information gathered use

`$ python manage.py migrate`

### Access admin site ###
To create a user 

`$ python manage.py createsuperuser`

then follow the instructions.

Sign in to the [admin site](http://127.0.0.1:8000/admin)


## Get Apache Server running ##

First make sure you have apache-httpd installed:

`$ brew install homebrew/apache/httpd24`

TIP: replace `brew` with `apt-get` on a linux system or a Windows friendly alternative of your choice on a Windows OS.
### Install mod_wsgi interface for Apache web server ###
*For the below, replace `pip` with `pip3` depending on your environment.*


Next, install mod_wsgi:

`$ pip install mod_wsgi`

## BEFORE DEPLOYING ##
Before deploying by merging to the master branch, ensure that debug is set to False in the settings.py file. 

`debug = False` 

### To deploy: ###

1. Merge into master branch
2. Remotely access ec2 server through terminal

`ssh -i "trendreport.pem" ec2-user@ec2-54-252-156-137.ap-southeast-2.compute.amazonaws.com`
3. Pull changes with
`git pull`
4. Restart apache server (Further instructions to be added)


## Useful Resources ##

* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)
* [Learn Django Queries](https://docs.djangoproject.com/en/1.11/topics/db/queries/)
* [More command line commands for Django admin](https://docs.djangoproject.com/en/1.11/ref/django-admin/)
* [Reference for many-to-many relationships in Django](https://docs.djangoproject.com/en/1.11/topics/db/models/#intermediary-manytomany)
