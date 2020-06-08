## Description

This is a simple service which returns information about films and people appeared in it provided by 3rd-party API GHIBLI: https://ghibliapi.herokuapp.com/

### Requirements 

1. Python 3.7
2. pipenv

### How To

1. run ```python -m pipenv install``` to create a virtual environment and install dependencies 
2. run ```python service/app.py``` to run an application
3. use Browser ```http://127.0.0.1:8000``` to see the Swagger UI or use CURL to test the endpoint

### Testing

To run unit tests use:
```shell
python -m unittest discover -s tests/ -v
```

## Comments

1. My intention was not to spend more than 4 hours for a task
2. I tried to use PEP8 to format my code, but I could miss something
3. I definitely could write more unit tests
4. Usually I cover as much code as I can, for this I use `coverage` module
5. I tried to keep the service as simple as possible. For this reason I used Flask-Cache
6. I did not write much doc strings, because the code looks self-explanatory
