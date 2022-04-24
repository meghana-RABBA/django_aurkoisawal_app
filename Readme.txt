## AurKoiSawal

AurKoiSawal is a question and answer wabsite for engineering students, where engineering students can post their problems to this website and get the solutions for their problems.
It has all the features that a Question and Answer Website should have.


## Images

<img src="/images/img1.jpg">
<img src="/images/img2.jpg">
<img src="/images/img3.jpg">
<img src="/images/img4.jpg">

## Technology Stack

* [Python 3.7.x](https://www.python.org/)
* [Django Web Framework 3.2.x](https://www.djangoproject.com/)
* [BootStrap 4](https://getbootstrap.com/)
* [SQLite 3](https://www.sqlite.org/index.html)


## Functionalities


* Can upload questions
* Reply to any question
* Comment on replies
* Upvote an answer
* Downvote an answer
* User login feature
* User Register feature


## Setup Commands

Clone this repository

1. Clone this project using
````
$ git clone https://github.com/Yawan-1/StackOverFlow--Clone
````
2. Install the Django Framework

$ pip install django

Now run make <code>migrations</code> command, running make migrations command will perform Data Migrations to save the "Badges" in the database.
then migrate to load the operations of Data Migrations in database.
````
$ python manage.py makemigrations
$ python manage.py migrate
````

Then, simply run the server using this command.
````
$ python manage.py runserver
````

## Login and Password

* Admin
username: "admin"
password: "admin"

* User1
username: "pankaj123"
password: "aurkoisawal"

* User2 
username: "swathy2020@gmail.com"
password: "aurkoisawal"
