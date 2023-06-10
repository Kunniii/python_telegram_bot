import json
from requests import get, post

url = "http://localhost:8000"


message = "*New Alert Created*\n```\nAlert: {The id of alert}\nRule:  {Some Rules Here}\nDate:  {Date created}\n```"

data = {"message": message}


res = post(url + "/send_alert", json=data)

print(json.dumps(res.json(), indent=2))
