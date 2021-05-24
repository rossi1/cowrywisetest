**SAMPLE API**


## Technologies Used
Below is a list of technologies used to build this project

-   Django
-   Docker Compose 1.17+
-   Docker
-   Postgres

## Installation
Follow these steps to set up the app.

Clone the repo:

[Github repo](https://rossi1/cowrywisetest)

Navigate to the project directory:

`cd cowrywise`

Create a virtual environment
`python -m venv kye_venv`

Note, you don't have to create the virtual environement in the project to prevent adding it to git or kindly add 
it to the .gitignore file

This will generate the virtual environment but will not activate it To activate the virtual environment, run:

`$ source src/kye_venv/bin/activate`

Environment variables like  `SECRET_KEY`  and  `DATABASE_URL`  should be added. Kindy refer to the .env_example to populate the .env

Create a  `.env`  file in your src folder. 

Then  `source .env`  at the terminal.

## Running and Development

Make sure your database is configured and your virtual environment is activated.
Install all dependencies using: 
`pip install -r requirements.txt`

Migration
Run the below command to run migrations
 
`$ python manage.py makemigrations`
`$ python manage.py migrate`


Start the application with `python manage.py runserver`

You are good to go.

## Understanding the Docker Compose Setup

Before you begin, check out the production.yml file in the root of this project. Keep note of how it provides configuration for the following services:

- django: your application running behind Gunicorn;
- postgres: PostgreSQL database with the application’s relational data;
- redis: Redis instance for caching;
- traefik: Traefik reverse proxy with HTTPS on by default.:

Build the stack first:

`$ docker-compose -f production.yml build`

run the stack:

`$ docker-compose -f production.yml up`

To run the stack and detach the containers, run:

`$ docker-compose -f production.yml up -d`

To run a migration, open up a second terminal and run:

`$ docker-compose -f production.yml run --rm django python manage.py migrate`


To check the logs out, run:

`$ docker-compose -f production.yml logs`


If you need a shell, run:

`$ docker-compose -f production.yml run --rm django python manage.py shell`

If you want to scale your application, run:

`$ docker-compose -f production.yml up --scale django=4`

To see how your containers are doing run:

` $ docker-compose -f production.yml ps`
