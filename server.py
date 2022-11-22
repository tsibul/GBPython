import random
import redis

with redis.Redis() as redis_server:
    redis_server.lpush('queue', random.randint(0, 10))
