<!--
repo name: mirumee-interview-task
description: Mirumee interview task
github name:  karolchmiel94
link: https://github.com/karolchmiel94/mirumee-interview-task
logo path:
screenshot:
email: karolch94@gmail.com
-->

<!-- PROJECT LOGO -->
<br/>
<p align="center">
    <!-- <a href="https://github.com/karolchmiel94/mirumee-interview-task">
        <img src="" alt="Logo" width="80" height="80">
    </a> -->
    <h3 align="center"><a href="https://github.com/karolchmiel94/mirumee-interview-task">mirumee-interview-task</a></h3>
    <p align="center">
         Are you a fan of first stage rocket's cores? Check this project and see which one was used the most and add it to as your favourite!
        <br />
        <br />
    </p>
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

- [Table of Contents](#table-of-contents)
- [Requirements](#requiremens)
- [Setup](#setup)
- [Functionalities description](#functionalities-description)

<!-- Requirements -->
## Requirements

- Python
- PIP


<!-- Setup -->
## Setup

Project isn't dockerized yet. To run it run:

> mkdir interview-task

> cd interview-task

- Clone project

> git clone https://github.com/karolchmiel94/mirumee-interview-task.git

- Create and activate virtual environment

> python3 -m venv venv

> source venv/bin/activate

- Install dependencies

> pip install -r requirements.txt

- Migrate database

> django-admin manage.py migrate

- Run application

> python manage.py runserver

<!-- Functionalities description -->
## Functionalities description

- First task

List of  most used first stages can be fetched from:
GET /fetch-cores/
query parameters:
- cores_number: integer
    description: Number of the most popularly used cores
    paramType: query
- successful: boolean
    description: Include or exclude successful missions
    values: True / False
    paramType: query
- planned: boolean
    description: Include or exclude planned missions
    values: True / False
    paramType: query

available commands:

- fetch_most_used_cores

Command fetches most used first stages sorted descending by number of uses.
Command arguments:
cores_number: int | Optional
-successful: str | Optional
-planned: str | Optional

Example uses:

Fetch all cores:
> python manage.py fetch_most_used_cores

Fetch 3 cores:
> python manage.py fetch_most_used_cores 3

Fetch 11 cores from successful launches without planned future missions:
> python manage.py fetch_most_used_cores 11 -successful True -planned False

- Second task

List of cores. If there is no cores saved in database, they are fetched from SpaceX api:
GET /cores/

Add core to favourites:
POST /favourite-cores/
{

  "core" : "CORE_ID",
  "user" : "USER_ID",

}

List favourite cores:
GET /favourites-cores/