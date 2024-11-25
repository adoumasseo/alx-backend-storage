#!/usr/bin/env python3
"""script that provides some stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient


nginx_collection = MongoClient().logs.nginx
logs_count = nginx_collection.count_documents({})
GET_count = nginx_collection.count_documents({'method': 'GET'})
POST_count = nginx_collection.count_documents({'method': 'POST'})
PUT_count = nginx_collection.count_documents({'method': 'PUT'})
PATCH_count = nginx_collection.count_documents({'method': 'PATCH'})
DELETE_count = nginx_collection.count_documents({'method': 'DELETE'})
GET_STATUS = nginx_collection.count_documents(
        {'method': 'GET', 'path': "/status"})
print(
        "{} logs\nMethods:\n\tmethod GET: {}\n\tmethod POST: {}\n\tmethod"
        " PUT: {}\n\tmethod PATCH: {}\n\tmethod DELETE: {}\n{} "
        "status check".format(logs_count, GET_count, POST_count,
                              PUT_count, PATCH_count, DELETE_count,
                              GET_STATUS
                              )
    )
