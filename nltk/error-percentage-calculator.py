
# Simple script that calculates the error percentage of NTLK automatic tagger,
# after tags have been manually double-checked

# Manual tagging symbols:
# ---------------------------------------------------------------
# | + | correct
# | - | incorrect
# | # | no results or non-existant symbol
# | ! | incorrect, but due to the developer's parser's fault
# ---------------------------------------------------------------

# Expects the format to be: 
# <word> (<tag>) - word/api/suggestions <manual-tagging-symbol>, 
# e.g: glad (JJ) - adjective/noun +

lines = []

total_count = 0;
correct_tag_count = 0

def get_percentage(part, whole):
  return 100 * float(part)/float(whole)

with open("parsed-text-manually-analyzed.txt", 'r') as file:

	lines = file.readlines()
	total_count = len(lines)

	for line in lines:
		split = line.split(" ")
		manual_tag = split[len(split) - 1].strip()
		
		if manual_tag == "+":
			correct_tag_count += 1
		elif manual_tag == "-":
			print("Incorrect tag: " + line)
		elif manual_tag == "#":
			print("Nonexistant symbol: " + line)
		elif manual_tag == "!":
			print("The developer should write a better parser: " + line)

percent = get_percentage(correct_tag_count, total_count)
print("NLTK correct tag percentage: " + str(percent))
