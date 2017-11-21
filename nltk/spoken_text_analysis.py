
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

parsed_lines = []

with open(SOURCE_FILE_NAME, 'r') as result_file:
	for raw_line in result_file:
		
		# Remove the first three characters in the text, as they are just line numbers
		line = raw_line[3:]
		# Remove leading and trailing white-spaces
		line = line.strip()
		# Remove all instances of ":" as they denote emphasis, intonation, breaks in pronuncation
		line = line.replace(":", "")
		# Remove all tags (<tagname> </tagname>)
		line = re.sub('<[^<]+?>', '', line)

		# Remove all speakers from lines
		for speaker in speakers:
			line = line.replace(speaker, "")

		parsed_lines.append(line)

# Counter is used for logging purposes
# Just to get the line count
counter = 1

for line in parsed_lines:
	print str(counter) + ": " + line
	counter += 1
