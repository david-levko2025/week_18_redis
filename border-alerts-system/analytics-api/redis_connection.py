from redis import Redis

from mongo_connection import settings

def get_redis_connection():
    return Redis(host='localhost', port=6379, decode_responses=True)