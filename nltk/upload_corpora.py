
# nltk and docx2txt need to be installed before you run it
import nltk
import re
import time
import docx2txt
import json
import requests

HEADER_ID = "0114"

SOURCE_FILE_NAME = "raw_texts/written_texts.docx"

docx2txt.process(SOURCE_FILE_NAME)

source_texts = docx2txt.process(SOURCE_FILE_NAME)

essay_blocks = source_texts.split(HEADER_ID)
lines = source_texts.split("\n")

essay_ids = []
raw_texts = []

# Read raw texts from source and add it to the raw text array
for essay in essay_blocks:

	if (len(essay.strip()) == 0):
		continue

	paragraph = essay[4:].strip()#.encode('utf-8').strip()
	raw_texts.append(paragraph)

for line in lines:
	if line.strip().encode('utf-8').startswith(HEADER_ID):
		essay_ids.append(line.strip())

result = []

index = 0

for text in raw_texts:
	
	tokens = nltk.word_tokenize(text)
	tagged_array = nltk.pos_tag(tokens)

	word = tagged_array[0][0]
	tag = tagged_array[0][1]

	result.append({
		"essay_id": essay_ids[index],
		"word": word,
		"tag": tag
		})

	index += 1

print(result)
json_result = json.dumps(result)

print(json_result)

r = requests.post("http://bugs.python.org", data=json_result)


