# django-backend-architecture
Django backend architecture - learn to build backend server for websites for portfolio management like portfoliobox.net


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




