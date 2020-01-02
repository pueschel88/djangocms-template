# djangocms-template


## Admin Panel

The login/password from the [the stage]() and local setups (created by default):
- test@what.digital
- test@what.digital


## Development Setup

Built on Python 3.7, Django 2.1, DjangoCMS 3.7, Webpack 4, TypeScript 3.

### Docker Intro

Make sure you have an up-to-date version of docker and docker-compose and node / yarn installed on your system

To execute a command you can use `docker-compose run --rm web <command>` directly or you can `docker-compose run --rm web bash` and then have a persistent terminal into the docker container

If a docker container is already running, you can connect to it using `docker-compose exec web <command>`

## Setup

- `docker-compose build web`
- `docker-compose up db`
- `docker-compose up web`
- `docker-compose exec web ./manage.py migrate`
- install yarn and node 10 outside of docker (better performance)
    - `yarn install --pure-lockfile`
    - `yarn start`

Installing additional requirements:
- `docker-compose exec web pip install -r requirements.txt` or just simply `docker-compose build web`

Testing:
- `docker-compose exec web ./manage.py collectstatic`
- `docker-compose exec web ./manage.py test --keepdb`


### local postgres db

docker-compose.yml now supports a postgresql database out of the box. Here are the steps to set it up:
- cd into this project
- make sure the following vars are in your `.env` file:
    ```.env
    DB_PORT=54320
    ```
- docker-compose up db
- cd into your deploy-django project (make sure your credentials folder has the correct server SSH key)
- create credentials/secrets-{project-name}-local.yml file and add the following content, adapt paths to your local dev env setup:
    ```
    user_name: {your-local-systems-user-name}
    project_root: /Users/etc/etc/{project-name}
    ```
    
- run ./deploy {project-name}-stage 6-pulldata.yml
- run ./deploy {project-name}-local 8-pushdata-dev.yml
- run the `web` container from within pycharm or docker-compose up web and see 🌟 


## Development Guidelines

This project is a fork of [djangocms-template](https://gitlab.com/what-digital/djangocms-template/), if you would like to edit the basic structure - create an MR there.

- [backend guidelines](/docs/readme/backend.md)
- [frontend guidelines](/docs/readme/frontend.md)
