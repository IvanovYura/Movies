import os


class BaseConfig:
    ENABLE_CACHE = True
    CACHE_TYPE = 'simple'
    CACHE_TIMEOUT = 60

    BASE_GHIBLI_URL = os.environ.get('BASE_GHIBLI_URL', 'https://ghibliapi.herokuapp.com')


class TestConfig(BaseConfig):
    BASE_GHIBLI_URL = ''
    ENABLE_CACHE = False
