
from .reaction import *

class Message:

	def __init__(self):
		pass

	def from_json(json):
		message = Message()
		message.sender_name = json["sender_name"]
		message.timestamp_ms = json["timestamp_ms"]
		message.type = json["type"]
		message.has_content = False

		if "content" in json:
			message.has_content = True
			message.content = json["content"]
		elif "photos" in json:
			message.content = "<photos>"
		elif "sticker" in json:
			message.content = "<sticker>"
		elif "gif" in json:
			message.content = "<gif>"
		else:
			message.content = None

		if "reactions" in json:
			message.reactions = Reaction.list_from_json(json["reactions"])
		else:
			message.reactions = []
		return message