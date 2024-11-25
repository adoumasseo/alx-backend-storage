#!/usr/bin/env python3
'''a Python function that inserts a new document
in a collection based on kwarg'''


def insert_school(mongo_collection, **kwargs):
    '''a fct to insert data in a mongodb collections'''
    cresult = mongo_collection.insert_one(kwargs)
    return cresult.inserted_id
