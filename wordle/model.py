
class Wordles:
	def __init__(self):
		pass

	def from_json(data):

		player_names = data[0]

		wordles = []

		for index in range(1, len(data)):
			wordle = Wordle.from_json(data[index], player_names)
			wordles.append(wordle)

		return wordles


class Wordle:
	def __init__(self):
		pass

	def from_json(data, player_names):

		players = []

		for index in range(2, len(player_names)):
			name = player_names[index]
			player = Player(index, name)
			players.append(player)

		wordle = Wordle()
		wordle.id = data[0]

		for index in range(2, len(players)):
			player = players[index]
			player.score = data[index]
		
		wordle.players = players

		return wordle


class Player:
	def __init__(self, index, name):
		self.index = index
		self.name = name
		self.score = -1

	def __repr__(self):
		return "{ index: " + str(self.index) + " name: " + self.name + " score: " + str(self.score) + " }"