import json

api = '{"bill_id": "hr100", "title": "Infrastructure Act", "status": "passed", "votes": {"yea": 245, "nay": 190}}'
bill_data = json.loads(api)

print(bill_data['title'])
print(bill_data['votes']['yea'])