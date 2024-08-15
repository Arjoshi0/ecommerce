# Django Notes

- Contribute to this open-source project

## Install django
- `pip install django`

## Create Virtual Environment
- `python -m venv .venv`

## Clone/Download the project
- In the directory where you have activated you virtual environment, clone the project there using `git clone git@github.com:Arjoshi0/ecommerce.git`

## Activate virtual environment
- Everytime you run a python project activate you virtual environment using 
  - In Windows use `.venv/Scripts/activate`
  - In Linux and MacOs use `source .venv/bin/activate`

## Install packages
- Go the the directory /ecommerce
- `pip install -r requirements.txt`

## Migrate your django data
- To make migrations ready use `python manage.py makemigrations`
- To migrate use `python manage.py migrate`

## Run the Project
- `python manage.py runserver`
- The default port of django application is 8000. If you want to change the running port type use `python manage.py runserver <port_name>`

# Git Notes

## Pull project
- After making necessary changes, first pull the project from remote using `git pull`
- If there is any conflicting changes, then stash the codes using `git add .` and `git stash`
- Now, pull the project and revert you stash using `git stash pop`

## Push
- Resolve the conflics and commit it using `git commit -m "<commit_message>"`
- Push it using `git push`

# Models
- String -> models.CharField()
- Integer -> models.IntegerField()