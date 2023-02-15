from tinydb import Query, TinyDB

import utilities

db = TinyDB('db.json')
App = Query()

def insert(item):
    db.insert({'item': item, 'time': utilities.time()})

def all():
    result = db.all()
    return result

def reset():
    db.truncate()