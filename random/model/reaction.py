
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