try:
    from functools import lru_cache
except ImportError:
    try:
        from fastcache import clru_cache as lru_cache
    except ImportError:
        def lru_cache(maxsize=None):
            return lambda x: x
