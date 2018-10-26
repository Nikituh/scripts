
import json
import operator
import sys

class LongestMessage:
    def __init__(self):
    	self.content = ""
    	self.length = 0
    	self.sender = ""

class Sender:
	def __init__(self):
		self.sender = ""
		self.message_lengths = []
		self.emoticon_message_count = 0

	def get_average(self):
		lengths = self.message_lengths
		return 0 if len(lengths) == 0 else round((float(sum(lengths)) / len(lengths)), 2)

sender_count = {}
content_count = {}

longest_message = LongestMessage()

senders = []

def find_sender(name):
	for sender in senders:
		
		if sender.sender == name:
			return sender
	return None;

with open('message.json') as f:
	data = json.load(f)
	messages = data["messages"]
	for message in messages:
		sender = message["sender_name"].encode('utf-8').strip()

		if not sender in sender_count:
			sender_count[sender] = 1
		else:
			sender_count[sender] += 1

		if "content" in message:
			content = message["content"]

			if not content in content_count:
				content_count[content] = 1
			else:
				content_count[content] += 1

			message_length = len(content)

			if (message_length > longest_message.length):
				longest_message.content = content.encode('utf-8').strip()
				longest_message.length = len(content)
				longest_message.sender = sender


			existing = find_sender(sender)

			if existing == None:
				new = Sender()
				new.sender = sender
				new.message_lengths.append(message_length)
				senders.append(new)

				if (len(content)) <= 2:
					new.emoticon_message_count += 1
			else:
				existing.message_lengths.append(message_length)

				if (len(content)) <= 2:
					existing.emoticon_message_count += 1


### SENDER:

sorted_sender_count = sorted(sender_count.items(), key=operator.itemgetter(1), reverse=True)

counter = 1
for key, value in sorted_sender_count:
    print(str(counter) + ". " + str(key) + ": " + str(value))
    counter += 1

### CONTENT:

# sorted_content_count = sorted(content_count.items(), key=operator.itemgetter(1), reverse=True)

# counter = 1
# for key, value in sorted_content_count:

# 	if counter > 40:
# 		break

# 	print(str(counter) + ". " + str(key.encode('utf-8'))[2:-1] + ": " + str(value))
# 	counter += 1

### LONGEST MESSAGE

# print("Longest message" + str(longest_message.length) + ": " + str(longest_message.content))
# print("Sender: " + str(longest_message.sender))

# ### AVERAGE MESSAGE LENGTH

# counter = 1
# sorted_senders = sorted(senders, key=lambda x: x.emoticon_message_count, reverse=True)
# for sender in sorted_senders:
# 	# print(str(counter) + ": " + str(sender.sender).replace("b", "").replace("'", "") + ": " + str(sender.get_average()))
# 	print(str(counter) + ": " + str(sender.sender).replace("b", "").replace("'", "") + ": " + str(sender.emoticon_message_count))
# 	counter += 1





