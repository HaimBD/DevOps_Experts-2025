import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0,username='default', password='Pa55w.rd')

print(r.get('foo'))