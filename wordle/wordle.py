
import requests

resp = requests.get(url="https://pikma.ee/wordles/wordles.json")
data = resp.json()

userEntry = data[0]

users = []

for user in userEntry:
	users.append({
		"count": 0,
		"total": 0,
		"average": -1,
		"name": user
	})


fullParticipation = []
for i in range(1, len(data)):
	entry = data[i]
	if None in entry:
		continue
	fullParticipation.append(entry)

topParticipation = []
for i in range(1, len(data)):
	entry = data[i]
	print(entry)
	ffy = 2
	ints = 4
	Niki = 8
	S6jalammas = 9
	tiit = 11
	if entry[ffy] is not None and entry[ints] is not None and entry[Niki] is not None and entry[S6jalammas] is not None and entry[tiit] is not None:
		topParticipation.append(entry)


#for i in range(0, len(fullParticipation)):
#	entry = fullParticipation[i]
for i in range(0, len(topParticipation)):
	entry = topParticipation[i]
#for i in range(1, len(data)):
#	entry = data[i]
	for j in range(2, len(entry)):
		score = entry[j]
		if score is not None:
			users[j]["count"] += 1
			users[j]["total"] += score

longest_name_len = 0

for user in users:
	if user["count"] == 0:
		continue
	user["average"] = round(user["total"] / user["count"], 2)

	if len(user["name"]) > longest_name_len:
		longest_name_len = len(user["name"])

sorted_users = sorted(users, key=lambda d: d["average"], reverse=False)
sorted_users = [x for x in sorted_users if x["average"] != -1]

for i in range(0, len(sorted_users)):
	user = sorted_users[i]

	place = (str(i + 1) + ". ") if i > 8 else (" " + str(i + 1) + ". ")
	name = user["name"].ljust(longest_name_len)
	average = str(user["average"]).ljust(4)
	count = str(user["count"]).ljust(3)
	
	print(place + name + " average score: " + average + " in " + count + " attempts")


users = data[0]
latest = data[len(data) - 1]

print(users)
for i in range(2, len(users)):
	print(users[i] + ": " + str(latest[i]))