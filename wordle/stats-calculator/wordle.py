
import requests

from model import Wordles

resp = requests.get(url="https://pikma.ee/wordles/wordles.json")
data = resp.json()

parsed = Wordles.from_json(data)

player_averages = []

start = len(parsed) - 8
start = 0

for index in range(start, len(parsed) - 1):
	wordle = parsed[index]

	for player in wordle.players:

		player_average = next((x for x in player_averages if x["name"] == player.name), None)

		if player_average == None:
			entry = { "name": player.name, "total": 0, "count": 0 }
			if player.score != None:
				entry["total"] = player.score
				entry["count"] = 1

			player_averages.append(entry)
		else:
			if player.score != None:
				player_average["total"] = player_average["total"] + player.score
				player_average["count"] = player_average["count"] + 1


for player in player_averages:
	if player["count"] != 0:
		player["average"] = player["total"] / player["count"]
	else:
		player["average"] = 0

cleaned_list = filter(lambda x: x["average"] != 0, player_averages)
sorted_users = sorted(cleaned_list, key=lambda d: d["average"], reverse=False)

for i in range(0, len(sorted_users)):
	user = sorted_users[i]

	place = (str(i + 1) + ". ") if i > 8 else (" " + str(i + 1) + ". ")
	name = user["name"].ljust(len("good_luck_indrek"))
	average = str(round(user["average"], 2)).ljust(4)
	count = str(user["count"])

	print(place + name + " average score: " + average + " in " + count + " attempts")
