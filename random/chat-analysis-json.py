
import json
import operator
import sys

sender_count = {}
content_count = {}

with open('message.json') as f:
	data = json.load(f)
	messages = data["messages"]
	for message in messages:
		sender = message["sender_name"]

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

    # print(str(data).encode('utf-8'))


sorted_sender_count = sorted(sender_count.items(), key=operator.itemgetter(1), reverse=True)

counter = 1
for key, value in sorted_sender_count:
    print(str(counter) + ". " + str(key.encode('utf-8'))[2:-1] + ": " + str(value))
    counter += 1

sorted_content_count = sorted(content_count.items(), key=operator.itemgetter(1), reverse=True)

counter = 1
for key, value in sorted_content_count:

	if counter > 40:
		break

	print(str(counter) + ". " + str(key.encode('utf-8'))[2:-1] + ": " + str(value))
	counter += 1