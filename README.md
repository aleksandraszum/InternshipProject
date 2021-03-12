# Notes webapp for Full-Stack Developer Assignment

## Table of contents
* [Author](#author)
* [General info](#general-info)
* [Requirement](#Requirement)
* [Setup and running](#setup-and-running)
* [Example usages](#usages)



## Author
Aleksandra Szum

## General info
Notes is a web application for recruitment to PolSource.

Project was created and tested in Windows Environment.

## Technologies
- Python 3.7
- asgiref==3.3.1
- Django==3.1.7
- djangorestframework==3.12.2
- pytz==2021.1
- sqlparse==0.4.1


## Setup and running
To run this project you need Python3. First, run Windows PowerShell and:
- clone this repository:

```powershell
git clone https://github.com/aleksandraszum/InternshipProject.git
```

- instal virtualenv:

```powershell
pip install virtualenv
```

- install requirements:

```powershell
pip install -r requirements.txt
```

- migrate data:

```powershell
python manage.py migrate
```

- run project:

```powershell
python manage.py runserver
```

### Example usage
- Add a new note
- Edit a note to add some new information
- Delete a note if it isn't necessary 
- Display all newest version of notes or all version of the specific note


