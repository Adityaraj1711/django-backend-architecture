# Under Construction

# Django Backend Architecture
Learn to create your own portfolio platform like portfoliobox.net - Open-Source Project By Aditya Raj

## About this open source project
The open-source project is for the developers who are trying to learn and create an application by following the best practices and paradigms. The project requires familiarity with Python programming language.

---
## Learn to build a portfolio website backend
- **This Backend is written using Django Framework** - Django provides simplicity, flexibility, reliability, and scalability. Django has its own naming system for all functions and components
 - **Feature encapsulation** - Django follows a file naming convention to manage the apps and so different feature are group together.
 - **Easy to Customize** - Pluggable and easy to customize emitters, parsers, validators, and authenticators.
 - **Response Handling** - HTTP response handling, content type negotiation using HTTP Accept headers.
 - **Views for request/response** - Clean, simple, views for Resources, using Django's class-based views.
 - **Converting data into valid HTTP request** - Powerful serialization engine using Django's rest framework.


Ready to use a Vagrant file for getting started with Django projects
Simpler API mapping for 




















## MVC Architecture: Model, View, Controller
---




# Project outline
    create profile -> draft details -> publish portfolio <- peers access

# Response request handling schematic diagram

# Concepts used in the project
 - [Difference between Vagrant and Docker](https://www.vagrantup.com/intro/vs/docker.html)
    
    https://djangocentral.com/creating-sitemaps-in-django/
    https://github.com/AliYmn/djeasy
    https://stackoverflow.com/questions/53404738/how-to-send-email-with-django-rest-framwork
    https://github.com/wsvincent/drfx
## API documentation












## Required setup
For development server - 

    - vagrant - tell what type of server we need
    - virtualbox

For application code -

    - layer 1: python
    - layer 2: Django - provides feature for creating a standard web app
    - layer 3: Django rest framework

Utility tools - 

    - atom editor
    - git: version control
    - modheader: modify http header while testing API
    






















## How to Build and run the project
* Install using vagrant [**Recommended Method**] 
    * Clone this repo.
    * Install Vagrant [Find instruction here](https://www.sitepoint.com/getting-started-vagrant-windows/)
    * Execute `vagrant up` to start vagrant box
    * Execute `vagrant ssh` to connect to Vagrant Box
    * Install postgresql in vagrant
    * Create user and database for postgresql
    ```git bash
    vagrant@ubuntu-xenial:/vagrant$ cd /vagrant/
    vagrant@ubuntu-xenial:/vagrant$ sudo su - postgres
    postgres@ubuntu-xenial:~$ psql
    postgres=# CREATE USER myprojectuser WITH PASSWORD 'password';
    postgres=# CREATE DATABASE myproject;
    postgres=# GRANT ALL PRIVILEGES ON DATABASE myproject to myprojectuser;
    postgres=# ALTER ROLE myprojectuser SET timezone TO 'UTC';
    postgres=# ALTER USER myprojectuser CREATEDB;
    postgres-# \q
    postgres@ubuntu-xenial:~$ exit
    ```
    * Quit postgres and run the following commands from the same bash
    ```git
     vagrant@ubuntu-xenial:/vagrant$ cd /vagrant/src/django_backend_api/
     vagrant@ubuntu-xenial:/vagrant/src/django_backend_api$ python3 manage.py makemigrations
     vagrant@ubuntu-xenial:/vagrant/src/django_backend_api$ python3 manage.py migrate
     vagrant@ubuntu-xenial:/vagrant/src/django_backend_api$ python3 manage.py runserver 0.0.0.0:8080
     ```
    * The server could now be accessible from your browser at [127.0.0.1:8080](http://127.0.0.1:8080)

# Project Directory Structure
```
├── e
├── get-pip.py
├── LICENSE
├── README.md
├── requirements.txt
├── src
│   └── django_backend_api
│       ├── api
│       │   ├── admin.py
│       │   ├── apps.py
│       │   ├── __init__.py
│       │   ├── migrations
│       │   │   ├── 0001_initial.py
│       │   │   ├── 0002_auto_20200418_2235.py
│       │   │   ├── __init__.py
│       │   │   └── __pycache__
│       │   │       └── __init__.cpython-35.pyc
│       │   ├── models.py
│       │   ├── permission.py
│       │   ├── __pycache__
│       │   │   ├── __init__.cpython-35.pyc
│       │   │   └── views.cpython-35.pyc
│       │   ├── serializers.py
│       │   ├── tests
│       │   │   ├── __init__.py
│       │   │   ├── test_certificate_api.py
│       │   │   ├── test_college_api.py
│       │   │   ├── test_portfolio_image_api.py
│       │   │   ├── test_project_api.py
│       │   │   └── tests.py
│       │   ├── urls.py
│       │   └── views.py
│       ├── db.sqlite3
│       ├── django_backend_api
│       │   ├── __init__.py
│       │   ├── settings.py
│       │   ├── urls.py
│       │   └── wsgi.py
│       ├── manage.py
│       └── media
│           └── uploads
│               └── avatar
│                   ├── 362af174-310f-4d00-9a30-26fe8d533fdb.jpg
│                   └── a2c74d16-06dd-4090-aab9-c7f776d1d411.jpg
├── ubuntu-xenial-16.04-cloudimg-console.log
└── Vagrantfile

```


--_Directory traversal for API calls_

# API examples

# How to customize according to your use

# Find the project useful


services -

api/<user_name>/
    methods - GET
api/cv/
    methods - GET, POST
api/cv/1
    methods - PUT, DELETE
api/about/
    methods - GET, POST
api/about/1
    methods - PUT, DELETE
api/projects/
    methods - GET, POST
api/projects/1
    methods - PUT, DELETE


models
---------------
Education
    college
    address
    grade
    degree
    from_date
    to_date

Skill
    skill
    rate

About
    about

Company
    company
    address
    url

WorkExperience
    Company
    from_date
    to_date
    currently_working_here

Projects
    project
    about
    feature
    tech_stack
    project_url

ImportantLinks
    about
    url

Interest
    interest
SpokenLanguage
    language

Achievement
    achievement
    when
    where

Certification
    name
    url

Portfolio
    name
    email
    Project
    About
    WorkExperience
    Achievement
    Certification
    Interest
    ImportantLinks
    SpokenLanguage




api/user/<user_name>/
    Only one portfolio
    user_name is unique
    GET request
api/college/
    GET, POST for logged in user
api/skill/
    GET, POST for logged in user
api/skill/<skill_id>
    PUT, DELETE
api/education/
    GET, POST for logged in user
api/education/<id>
api/experience/



