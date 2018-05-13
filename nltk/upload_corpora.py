
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

	words = []

	word_index = 0
	for item in tagged_array:
		word = item[0]
		tag = item[1]
		words.append({ "text": word.encode('ascii','ignore'), "tag": tag, "index": word_index })
		word_index += 1

	result.append({
		"essay_id": essay_ids[index],
		"words": words
		})

	index += 1

# request = requests.post("https://corpus.nikitech.eu/corpus_upload.php", data = { 'data': result })
url = "https://corpus.nikitech.eu/corpus_upload.php"
headers = { 'Content-Type': 'application/json', 'Accept':'application/json' }
request = requests.post(url, data=json.dumps(result), headers=headers)

print(request.text)


