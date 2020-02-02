
import json
import operator
import sys

class Message:

	def __init__(self):
		pass

	def from_json(json):
		message = Message()
		message.sender_name = json["sender_name"]
		message.timestamp_ms = json["timestamp_ms"]
		message.type = json["type"]
    	
		if "content" in json:
			message.content = json["content"]
    	
		if "reactions" in json:
			message.reactions = Reaction.list_from_json(json["reactions"])
		return message

class Reaction:
	def __init__(self):
		pass

	def from_json(json):
		reaction = Reaction()
		print(json);
		reaction.reaction = json["reaction"];
		reaction.actor = json["actor"]
		return reaction

	def list_from_json(json):
		reactions = []
		for child in json:
			reactions.append(Reaction.from_json(child))
		return reactions

messages = []

for i in range(1, 18):
	with open("messages/message_" + str(i) + ".json") as f:
		data = json.load(f)
		messages_json = data["messages"]

	for message_json in messages_json:
		message = Message.from_json(message_json)


