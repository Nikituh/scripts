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

SOURCE_FILE_NAME = "Kirjalikkorpus_kõik.docx"
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

with open(PARSED_FILE_NAME, 'w') as result_file:
	result_file.write("LEGEND: \n")
	for key in penn_treebank_tags:
		text = key + ": " + penn_treebank_tags[key]
		result_file.write(text + "\n")

	result_file.write("\n\n")

text = docx2txt.process(SOURCE_FILE_NAME)

raw_pages = []
parsed_pages = []

# docx2txt doesn't really offer a convenient way to read a document per page,
# so I put together this hack that separates the whole text into pages by the headers each text contains.
# Each text contains a number that starts with 0114 and then four other characters
for item in text.split("0114"):
	paragraph = item[4:].strip()
	raw_pages.append(paragraph)

counter = 0

for page in raw_pages:
	counter += 1
	print "Paragraph " + str(counter) + ": \n"
	print page

start = time.time()

tokens = nltk.word_tokenize(text)
tagged_array = nltk.pos_tag(tokens)

with open(PARSED_FILE_NAME, 'a') as result_file:
	for tag in tagged_array:

		# Stringify and replace junk at start and end
		result = str(tag).replace("(u", "").replace(")", "")
		# Words and tags are surrounded by apostrophes, remove them
		result = result.replace("'", "")
		
		# Only count results that contain a letter, remove pure numbers punctuation marks
		if (re.search('[a-zA-Z]', result) and "\u" not in result):
			split = result.split(", ")

			word = split[0]
			tag_short = split[1]
			tag_long = penn_treebank_tags[tag_short]

			# result = word + " - " + tag_short + " (" + tag_long + ")"
			result = word + " (" + tag_short + ")"
			result_file.write(result + " ")
		else:
			split = result.split(", ")
			punctuation_mark = split[0]

			if punctuation_mark == ".":
				result_file.write(punctuation_mark + "\n\n")
			else:
				result_file.write(punctuation_mark + " ")

end = time.time()

print("Tagging took	: " + str(end - start))






