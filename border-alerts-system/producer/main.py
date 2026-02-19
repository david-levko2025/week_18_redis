from priority_logic import Redis,open_file,process_alert

def main():
    redis_cnx = Redis()
    alerts_list = open_file()
    for alert in alerts_list:
        process_alert(alert, redis_cnx)


if __name__ == "__main__":
    main()