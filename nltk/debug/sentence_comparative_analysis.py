
import nltk
import re

text = "Some of the consequences of that new standard of international English will be that some or all grammatical changes will be made."
# text = "A new internationl English will, without doubt, come with grammatical changes"

tokens = nltk.word_tokenize(text)
tagged_array = nltk.pos_tag(tokens)

for tag in tagged_array:
	# Stringify and replace junk at start and end
	result = str(tag).replace("(u", "").replace(")", "").replace("(", "")
	# Words and tags are surrounded by apostrophes, remove them
	result = result.replace("'", "")
	# Now we're left that with the word and the tag, separated by a comma. Split it into two
	split = result.split(", ")

	parsed_text = ""

	word = split[0]
	tag_short = split[1]

	# Only count results that contain a letter, remove pure numbers punctuation marks
	if re.search('[a-zA-Z]', result):
		result = word + " (" + tag_short + ")"
	else:
		result = word
	
	parsed_text += result + " "

	print(parsed_text)



# Some (DT) of (IN) the (DT) consequences (NNS) of (IN) that (DT) new (JJ) standard (NN) of (IN) international (JJ) English (NNP) will (MD) be (VB) that (IN) some (DT) or (CC) all (DT) grammatical (JJ) changes (NNS) will (MD) be (VB) made (VBN).

# A (DT) new (JJ) internationl (NN) English (NNP) will (MD), without (IN) doubt (NN) , come (VB) with (IN) grammatical (JJ) changes (NNS) 
