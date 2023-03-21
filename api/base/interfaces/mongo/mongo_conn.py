#!/usr/bin/env python
""" Initialise mongodb connection """
import os

from pymongo import MongoClient


class MongoSettings():
    host: str = os.getenv("MONGOHOST")
    port: str = os.getenv("MONGOPORT")
    username: str = os.getenv('MONGOUSER')
    password: str = os.getenv('MONGOPASS')
    uri: str = "mongodb://{}:{}@{}:{}".format(username, password, host, port) \
        if username else "mongodb://{}:{}".format(host, port)
    database: str = "demo_api"
    demo_collection: str = "demo"


class Database(MongoClient):
    """Singleton wrapper for MongoClient."""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(MongoClient, cls).__new__(
                cls, *args, **kwargs)
        return cls._instance

    def __init__(self, *args, **kwargs):
        super().__init__(MongoSettings.uri, *args, **kwargs)
        self.demo_collection = self[MongoSettings.database][MongoSettings.demo_collection]