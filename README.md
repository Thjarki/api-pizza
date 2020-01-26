# api-pizza

API for pizzas in iceland.

# Requirements

- python 3.7
- pip
- pipenv

# How to run

```console
foo@bar:~$ pipenv shell
```

if model for database has been change, you must run these commands inside the shell

```console
If no database has been initialized, otherwise skip

foo@bar:~$ python migrate.py db init
```

```console
foo@bar:~$ python migrate.py db migrate
foo@bar:~$ python migrate.py db upgrade
```
