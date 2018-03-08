
# API Source:
# https://www.wordsapi.com/

import urllib2
import json

splitter = ") "
separator = "- "

base_url = "https://wordsapiv1.p.mashape.com/words/"

# Basic headers are required for any http request
basic_headers = {
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	'Accept-Encoding': 'none',
	'Accept-Language': 'en-US,en;q=0.8',
	'Connection': 'keep-alive'
}

# The mashable key is added as a special header
# so they could log the amount of words I have requested definitions of
mashable_key = open("mashable_key", 'r').read()

parsed_words = []

with open("raw-text.txt", 'r') as source_file:
	text = source_file.readlines()[0]
	split = text.split(splitter)

	for item in split:
		parsed_words.append(item + splitter)

total = str(len(parsed_words))
counter = 1

parsed_analyzed_words = []

for parsed_word in parsed_words:

	word_without_tag = parsed_word.split(" (")[0]

	# Clean the word, as it can contain some junk data (example: . But)
	clean_word = word_without_tag.replace(",", "").replace(".", "")
	clean_word = clean_word.replace(":", "")
	clean_word = clean_word.replace(";", "")
	clean_word = clean_word.replace("(", "").replace(")", "").strip()

	url = base_url + word_without_tag
	request = urllib2.Request(url)

	for key, value in basic_headers.items():
		request.add_header(key, value)
	
	request.add_header('X-Mashape-Key', mashable_key)

	print("Requesting analysis for word: " + clean_word + " (" + str(counter) + "/" + str(total) + ")")
	counter += 1

	response = urllib2.urlopen(request)
	
	result = response.read()
	result_json = json.loads(result)
	
	# Add add the un-analyzed word to the list and continue to the next item
	if "results" not in result_json:
		parsed_analyzed_words.append(parsed_word + separator)
		continue

	result_json = result_json["results"]

	possible_tags = []

	for child in result_json:
		tag = child["partOfSpeech"]
		if not tag in possible_tags:
			possible_tags.append(tag)

	possible_tags = "/".join(possible_tags)
	
	parsed_analyzed_word = parsed_word + separator + possible_tags

	parsed_analyzed_words.append(parsed_analyzed_word)

for parsed_analyzed_word in parsed_analyzed_words:
	with open("parsed-text.txt", 'w') as destination_file:
		destination_file.write(parsed_analyzed_word)







