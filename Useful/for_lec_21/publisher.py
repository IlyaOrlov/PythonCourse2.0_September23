import redis

r = redis.Redis(host='localhost', port=6379, db=0)
r.publish('my-chat', 'user: Hello!')
