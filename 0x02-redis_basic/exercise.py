#!/usr/bin/env python3
"""First task of using Redis"""
import uuid
import redis
from functools import wraps
from typing import Union, Callable, Any


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper

class Cache:
    '''A class for implementing random caching'''

    def __init__(self) -> None:
        '''Contructor of class Cache'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''Store data in redis with a uuid key'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self,
            key: str,
            fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        '''Retrieves a value from a redis database'''
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> Union[str, bytes, int, float]:
        '''Retrieves a string value from a Redis data storage.'''
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Union[str, bytes, int, float]:
        '''Retrieves a int value from a Redis data storage'''
        return self.get(key, lambda x: int(x))
