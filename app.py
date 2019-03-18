import redis
from flask import Flask, jsonify

app = Flask("rest-repo")

global redis_pool
redis_url = os.environ.get('REDIS_URL', 'redis://localhost:6379/0')
redis_pool = redis.ConnectionPool.from_url(redis_url)
r = redis.Redis(connection_pool=redis_pool)
r.set('foo', 'bar')
print 'connected to redis, kespace info: %s' % r.info('keyspace')

@app.route("/")
def home():
    return 'it works'

@app.route("/db-info")
def info():
    return jsonify(r.info('keyspace'))