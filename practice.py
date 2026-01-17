bills = [
    {"id": "hr1", "title": "The Petroleum is Good for America Act", "cosponsors": 13},
    {"id": "hr2", "title": "The Clean Energy Act of 2026", "cosponsors": 27},
    {"id": "hr3", "title": "The Education Reform Act of 2026", "cosponsors": 22}
]

for i in bills:
    print(f"{i['id'].upper()}: {i['title']} has {i['cosponsors']} cosponsors.")

popular_bills = []

for bill in bills:
    if bill['cosponsors'] > 20:
        popular_bills.append(bill)

print("\nHow many bills are considered popular in terms of cosponsorship?")
print(len(popular_bills))

print("\nWhat are their titles?")
for bill in popular_bills:
    print(bill['title'])