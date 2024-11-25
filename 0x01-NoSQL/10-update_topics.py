#!/usr/bin/env python3
'''a fct that changes all topics of a school document based on the name'''


def update_topics(mongo_collection, name, topics):
    '''Update some rows'''
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
