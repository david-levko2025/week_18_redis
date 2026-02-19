import os
import redis
import json

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
REDIS_DB = int(os.getenv("REDIS_DB", "0"))


class Redis:
    def get_redis_config(self):
        return redis.Redis(host='localhost', port=6379, decode_responses=True,db=0)
    def get_data(self, route_num: str):
        route_data = self.get_redis_config().get(f"route:{route_num}")
        if route_data:
            return json.loads(route_data)  # type: ignore
        else:
            return None

    def insert_route_data(self, route_data, route_num):
        client = self.get_redis_config()
        client.setex(f"route:{route_num}", 3600, json.dumps(route_data))