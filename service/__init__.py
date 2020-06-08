from flask_caching import Cache

from service.config import BaseConfig

# simple Flask cache
if BaseConfig.ENABLE_CACHE:
    cache = Cache()
