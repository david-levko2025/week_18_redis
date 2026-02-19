import redis
import json


class Redis():
    def get_redis_config(self):
        return redis.Redis(host='localhost', port=6379, decode_responses=True,db=0)

    def push_alarm(self,alert_data, queue):
        try:
            client = self.get_redis_config()
            client.lpush(queue, json.dumps(alert_data))
            print(f"alert pushed to queue{queue}")
            print(f"alert data\n{alert_data}")
        except Exception as e:
            print(f"faild to push alert to redis: {e}")