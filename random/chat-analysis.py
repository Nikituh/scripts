
# Basic script that analyzes the message counts of a single chat from a downloaded facebook archive
# The script must be in the same folder as your unpacked archive folder

# To download your archive, click on Settings (dropdown in your top-right corner),
# then 'Download a copy of your Facebook data.'
# Your entire facebook history is parsed together into a full offline web page,
# containing .html files of everything you've ever said and done
# This operation might take some time, my archive's eventual size was 2.8gb

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree
import time
import operator

start_time = time.time()

# Chats are located under facebook<username>/messages/<index(int)>.html
# The number seems to be completely random, not based on any statistic about the chat
username = "aareundo"
index = "99"
path = 'facebook-' + username + '/messages/' + index + '.html'

# The file itself is a self-sufficient html file, meaning it contains extra information
# Messages themselves are under body and thread (the div)
raw = xml.etree.ElementTree.parse(path).getroot()
raw = raw.find('body').find('div')

messages_by_user = {}
total = 0

for item in raw:
    item_type = item.get("class")
    
    # Raw chat items contain <p> separators. Only parse those of the type 'message'
    if item_type == "message":

    	# The actual message content is, still, even more hidden under another container and inside a span
    	message = item.find('div').find('span')
    	by_user = message.text
    	total += 1
	
    	if not by_user in messages_by_user:
    		messages_by_user[by_user] = 1
    	else:
    		messages_by_user[by_user] += 1


        # If you wish to get the character count instead:
        # split = by_user.split()
        # for character in split:
        #     if not by_user in messages_by_user:
        #         messages_by_user[by_user] = 1
        #     else:
        #         messages_by_user[by_user] += 1


# Sort by descending
sorted_messages_by_user = sorted(messages_by_user.items(), key=operator.itemgetter(1), reverse=True)

counter = 1
for key, value in sorted_messages_by_user:
	print(str(counter) + ". " + key.encode('utf-8').strip() + ": " + str(value))
	counter += 1

print("Total: " + str(total))

elapsed_time = time.time() - start_time
print("Calculation took: " + str(elapsed_time))








