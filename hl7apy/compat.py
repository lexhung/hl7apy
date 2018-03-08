try:
    from functools import lru_cache
except ImportError:
    from fastcache import clru_cache as lru_cache
