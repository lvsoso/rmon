#coding=utf-8
from rmon.models.server import Server

def inc(x):
    return x + 1

def test_inc(app, db, server):
    print(Server.query.count())
    print(app)
    print(dir(db))
    print(server.query.count())
    assert inc(3) == 4
