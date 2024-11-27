#!/usr/bin/env python3
"""First task of using Redis"""
import uuid
import redis
from typing import Union


class Cache:
    '''A class for implementing random caching'''

    def __init__(self) -> None:
        '''Contructor of class Cache'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''Store data in redis with a uuid key'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
