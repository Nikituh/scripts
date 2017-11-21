# -*- coding: utf-8 -*-

# Tagging tool of learner language corpora
# In its current state it's not by any means a universal tool,
# created to process a specific text file:
# Kirjalikkorpus_kõik.docx

# nltk and docx2txt need to be installed before you run it
import nltk
import re
import time
import docx2txt
import re

SOURCE_FILE_NAME = "written_texts.docx"
PARSED_FILE_NAME = "parsed_written_texts.txt"

# NOTE:
# Initially, if you haven't, you need to download the necessary files:
# It's mostly just a bunch of libraries and corpora you won't use (3.5GB), so 'all' isn't necessary, 
# but I don't know which ones i'd need, so screw it. Got 'em all

# nltk.download('all')

# The default tagger of nltk.pos_tag() uses the Penn Treebank Tag Set
# http://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
penn_treebank_tags = {
	"CC": "Coordinating conjunction",
	"CD": "Cardinal number",
	"DT": "Determiner",
	"EX": "Existential there",
	"FW": "Foreign word",
	"IN": "Preposition or subordinating conjunction",
	"JJ": "Adjective",
	"JJR": "Adjective, comparative",
	"JJS": "Adjective, superlative",
	"LS": "List item marker",
	"MD": "Modal",
	"NN": "Noun, singular or mass",
	"NNS": "Noun, plural",
	"NNP": "Proper noun, singular",
	"NNPS":	"Proper noun, plural",
	"PDT": "Predeterminer",
	"POS": "Possessive ending",
	"PRP": "Personal pronoun",
	"PRP$": "Possessive pronoun",
	"RB": "Adverb",
	"RBR": "Adverb, comparative",
	"RBS": "Adverb, superlative",
	"RP": "Particle",
	"SYM": "Symbol",
	"TO": "to",
	"UH": "Interjection",
	"VB": "Verb, base form",
	"VBD": "Verb, past tense",
	"VBG": "Verb, gerund or present participle",
	"VBN": "Verb, past participle",
	"VBP": "Verb, non-3rd person singular present",
	"VBZ": "Verb, 3rd person singular present",
	"WDT": "Wh-determiner",
	"WP": "Wh-pronoun",
	"WP$": "Possessive wh-pronoun",
	"WRB": "Wh-adverb"
}

# Time is used simply for logging purposes. I want to know how long tagging takes
start = time.time()

# As the initial step, write the legend to the file
with open(PARSED_FILE_NAME, 'w') as result_file:
	result_file.write("LEGEND: \n")
	for key in penn_treebank_tags:
		text = key + ": " + penn_treebank_tags[key]
		result_file.write(text + "\n")

# Process word document
source_texts = docx2txt.process(SOURCE_FILE_NAME)

raw_texts = []
parsed_texts = []

# docx2txt doesn't really offer a convenient way to read a document per page,
# so I put together this hack that separates the whole text into pages by the headers each text contains.
# Each text contains a number that starts with 0114 and then four other characters

# Read raw texts from source and add it to the raw text array
for source_text in source_texts.split("0114"):
	paragraph = source_text[4:].strip()
	raw_texts.append(paragraph)


# TODO 
# Word's with apostrophies (let's) parsed wrong, split into three words: let + u2019 + s
# UTF-8 encoding?
# Save as .csv
# Questions:
# Does it look for sentences (and verbs in then?)

# Parse raw texts and add them to the parsed text array
for text in raw_texts:
	
	# text = nltk.wordpunct_tokenize(text.decode('utf8'))
	tokens = nltk.word_tokenize(text)
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
		
		parsed_text += result + " "

	parsed_texts.append(parsed_text)

# Write texts from parsed text array to file
with open(PARSED_FILE_NAME, 'a') as result_file:
	for text in parsed_texts:
		result_file.write(text + "\n\n")

end = time.time()

print("Tagging took	: " + str(end - start))




