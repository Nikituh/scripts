
from model.message import Message
from model.reaction import Reaction

import os
import json
import operator

BASE = "messages/facebook-aareundo (4)/messages/inbox/"
ENTITY = "<name-of-person-or-group>"

path = BASE + ENTITY
files = os.listdir(path)

messages = []

for name in files:
	if "message_" in name:
		with open(path + name) as f:
			data = json.load(f)
			messages_json = data["messages"]

		for message_json in messages_json:
			message = Message.from_json(message_json)
			# if (message.content == "<photos>"):
			messages.append(message)

messages_by_sender = {}
for message in messages:
	if message.sender_name in messages_by_sender:
		messages_by_sender[message.sender_name] += 1
	else:
		messages_by_sender[message.sender_name] = 1

sorted_sender_count = sorted(messages_by_sender.items(), key=operator.itemgetter(1), reverse=True)

print("Total messages sent:")
counter = 1
for key, value in sorted_sender_count:
    print(str(counter) + ". " + str(key) + ": " + str(value))
    counter += 1

reactions_by_sender = {}
for message in messages:
	for reaction in message.reactions:
		if reaction.actor in reactions_by_sender:
			reactions_by_sender[reaction.actor] += 1
		else:
			reactions_by_sender[reaction.actor] = 1

sorted_sender_count = sorted(reactions_by_sender.items(), key=operator.itemgetter(1), reverse=True)

print("Total reactions:")
counter = 1
for key, value in sorted_sender_count:
    print(str(counter) + ". " + str(key) + ": " + str(value))
    counter += 1



