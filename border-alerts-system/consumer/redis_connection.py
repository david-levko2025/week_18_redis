import os
import redis

class Redis():
    def get_redis_config(self):
        return redis.Redis(host='localhost', port=6379, decode_responses=True,db=0)
    
    def pop_alert(self, queue: str):
        client = self.get_redis_config()
        alert_data = client.rpop(queue)
        return alert_data