
# IMPORTANT!
# Didn't want to duplicate comments,
# written_texts_analysis.py contains additional information about these imports,
# what you need to do before using nltk etc
import re
import time
import docx2txt
import nltk
# conf.py contains configuration etc. files used both by written_text_analysis.py and spoken_text_analysis.py
from conf import *

SOURCE_FILE_NAME = "interview02txt.txt"
PARSED_FILE_NAME = "parsed_spoken_texts.txt"

# Tags for speakers in the text
# These vary by text, are not universal
speakers = ["PM01", "EF02"]

parsed_raw_lines = []

with open(SOURCE_FILE_NAME, 'r') as result_file:
	for raw_line in result_file:
		
		# Remove the first three characters in the text, as they are just line numbers
		line = raw_line[3:]
		# Remove leading and trailing white-spaces
		line = line.strip()
		# Remove all instances of ":" as they denote emphasis, intonation, breaks in pronuncation
		line = line.replace(":", "")
		# Remove all tags (<tagname> </tagname>), usually overlapping speech
		# TODO: Somehow display that this is overlapping text?
		line = re.sub('<[^<]+?>', '', line)
		# Remove everything surrounded by parentheses and square brackets
		# These include unintelligible words, 
		line = re.sub("[\(\[].*?[\)\]]", "", line)
		# Remove = characters
		line = line.replace("=", "")
		# Remove @ characters
		line = line.replace("@", "")
		# Remove punctuation
		line = line.replace("?", "").replace(".", "")

		# Remove all speakers from lines
		for speaker in speakers:
			line = line.replace(speaker, "")

		parsed_raw_lines.append(line)

# Counter is used for logging purposes
# Just to get the line count
counter = 1

parsed_lines = []

for line in parsed_raw_lines:

	tokens = nltk.word_tokenize(line)
	tagged_array = nltk.pos_tag(tokens)
	
	parsed_text = ""

	for tag in tagged_array:
		# Stringify and replace junk at start and end
		result = str(tag).replace("(u", "").replace(")", "")
		# Words and tags are surrounded by apostrophes, remove them
		result = result.replace("'", "")
		# Now we're left that with the word and the tag, separated by a comma. Split it into two
		split = result.split(", ")

		word = split[0]
		tag_short = split[1]

		# Only count results that contain a letter, remove pure numbers punctuation marks
		if re.search('[a-zA-Z]', result):
			result = word + " (" + tag_short + ")"
		else:
			result = word
		
		result = result[1:]
		parsed_text += result + " "

	print parsed_text
	parsed_lines.append(parsed_text)

# Write texts from parsed text array to file
with open(PARSED_FILE_NAME, 'w') as result_file:
	for text in parsed_lines:
		result_file.write(text + "\n")





