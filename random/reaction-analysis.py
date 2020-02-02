# -*- coding: UTF-8 -*-

import json
import operator
import sys

# Message Model
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
		else:
			message.reactions = []
		return message

# Reaction Model
class Reaction:
	def __init__(self):
		pass

	def from_json(json):
		reaction = Reaction()
		reaction.reaction = json["reaction"].encode("unicode-escape")
		reaction.actor = json["actor"]
		return reaction

	def list_from_json(json):
		reactions = []
		for child in json:
			reactions.append(Reaction.from_json(child))
		return reactions

# Read and parse messages from files
messages = []

for i in range(1, 18):
	with open("messages/message_" + str(i) + ".json") as f:
		data = json.load(f)
		messages_json = data["messages"]

	for message_json in messages_json:
		message = Message.from_json(message_json)
		messages.append(message)

# Group messages by sender, print top
messages_by_sender = {}

for message in messages:
	if message.sender_name in messages_by_sender:
		messages_by_sender[message.sender_name] += 1
	else:
		messages_by_sender[message.sender_name] = 1

sorted_sender_count = sorted(messages_by_sender.items(), key=operator.itemgetter(1), reverse=True)

# counter = 1
# for key, value in sorted_sender_count:
#     print(str(counter) + ". " + str(key) + ": " + str(value))
#     counter += 1

# Group reactions, print top
reaction_map = {
	b'\\xf0\\x9f\\x98\\x86': "😆",
	b'\\xf0\\x9f\\x98\\x8d': "😍",
	b'\\xf0\\x9f\\x91\\x8d': "👍",
	b'\\xf0\\x9f\\x98\\xae': "😮",
	b'\\xf0\\x9f\\x98\\xa2': "😢",
	b'\\xf0\\x9f\\x98\\xa0': "😠",
	b'\\xe2\\x9d\\xa4':       "❤",
	b'\\xf0\\x9f\\x91\\x8e': "👎"
}

reactions = {}

for message in messages:
	for reaction in message.reactions:
		if reaction.reaction in reactions:
			reactions[reaction.reaction] += 1
		else:
			reactions[reaction.reaction] = 1

sorted_reaction_count = sorted(reactions.items(), key=operator.itemgetter(1), reverse=True)

counter = 1
for key, value in sorted_reaction_count:
	print(str(counter) + ". " + reaction_map[key] + ": " + str(value))
	counter += 1










