from redis import Redis


def get_redis_connection():
    return Redis(host=settings.REDIS_HOST, port=6379, decode_responses=True)