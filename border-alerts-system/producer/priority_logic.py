import json
from schema import BorderAlerts

def open_file():
    with open("data/border_alerts.json",'r') as file:
        border_alerts = json.load(file)
    return border_alerts

def priority_classification():
    border_alerts_file = open_file()

    for alert in border_alerts_file:
        if alert['weapon_count'] > 0:
            border_alerts_file['priority'] = 'URGENT'

        elif alert['distance_from_fence_m'] <=50:
            border_alerts_file['priority'] = 'URGENT'

        elif alert['people_count'] >= 8:
            border_alerts_file['priority'] = 'URGENT'

        elif alert['vehicle_type'] == "truck":
            border_alerts_file['priority'] = 'URGENT'

        elif alert['distance_from_fence_m'] <= 150 and alert['people_count'] >= 4:
            border_alerts_file['priority'] = 'URGENT'

        elif alert['vehicle_type'] == "jeep" and alert['people_count'] >= 3:
            border_alerts_file['priority'] = 'URGENT'
            
        else:
            border_alerts_file['priority'] = 'NORMAL'