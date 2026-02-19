from datetime import datetime
from redis_connection import Redis
from mongo_connection import MongoConnection
import json


def main():
    redis_class = Redis()
    mongo_class = MongoConnection()
    print("waiting for alerts...")
    while True:
        alert = redis_class.pop_alert('urgent_queue')
        if alert is None:
            alert = redis_class.pop_alert('normal_queue')
        if alert is None:
            continue
        alert_json_format = json.loads(alert)  # type: ignore
        print(f"we have {alert_json_format['priority']} alert!")
        alert_json_format["insertion_time"] = datetime.now()
        print(f"the insertion_time: {alert_json_format['insertion_time']}")
        mongo_class.insert_alert(alert_json_format)


if __name__ == "__main__":
    main()