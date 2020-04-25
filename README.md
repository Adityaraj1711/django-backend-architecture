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
Development server - 

    - vagrant - tell what type of server we need
    - virtualbox

Application code -

    - layer 1: python
    - layer 2: Django - provides feature for creating a standard web app
    - layer 3: Django rest framework

tools - 

    - atom
    - git: version control
    - modheader: modify http header while testing API
    

## How to Build and run the project
* Install using vagrant [**Recommended Method**] 
    * Clone this repo.
    * Install Vagrant [Find instruction here](https://www.sitepoint.com/getting-started-vagrant-windows/)
    * Execute `vagrant init` in a terminal from the repo directory.
    * Execute `vagrant up` to start vagrant box
    * Execute `vagrant ssh` to connect to Vagrant Box and then enter following commands
```bash
    cd /vagrant/
        
```    

# Project Directory Structure

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




