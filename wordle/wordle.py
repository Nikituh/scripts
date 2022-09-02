
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

for i in range(1, len(data)):
  entry = data[i]
  for j in range(2, len(entry)):
  	score = entry[j]
  	users[j]["score"] = score

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