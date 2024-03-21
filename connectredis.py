import redis
import json
r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='qwer1234')
def getvalue(key):
    if(r.get(key)==None):
        return None
    return json.loads(r.get(key))
def setvalue(key, value):
    r.set(key,value)
def dellkey(key):
    r.delete(key)
