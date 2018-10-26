
import operator
import conf

counter = 1
total_word_count = 0

tag_counts = { }
word_counts = { }

with open("output/parsed_written_texts_no_legend.txt", 'r') as file:
	lines = file.readlines()
	for line in lines:
		line = line.strip()

		if (line != ""):
			entities = line.replace(".", "").replace(",", "").replace(":", "").replace("?", "")
			entities = entities.strip().split(" ")

			tag_counter = 0

			tagged_word = ""

			for entity in entities:

				if (entity == ""):
					continue

				if "(" in entity and ")" in entity:
					tag = entity
					if tag in tag_counts:
						tag_counts[tag] += 1
					else:
						tag_counts[tag] = 1
				else:
					word = entity.lower()
					total_word_count += 1

					if word in word_counts:
						word_counts[word] += 1
					else:
						word_counts[word] = 1

sorted_tag_counts = sorted(tag_counts.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_tag_counts)

sorted_word_counts = sorted(word_counts.items(), key=operator.itemgetter(1), reverse=True)

counter = 0
print(str(len(sorted_word_counts)))
print(str(total_word_count))
# for word in sorted_word_counts:
	# if counter < 20:
	# 	print(word[0] + ": " + str(word[1]))
	# 	counter += 1

	# if word[1] > 100:
		# print(word[0] + ": " + str(word[1]))

tags = []
for tag in conf.penn_treebank_tags:
	tags.append(tag)

for tag in sorted_tag_counts:
	tag = tag[0].replace("(", "").replace(")", "")
	if tag in tags:
		tags.remove(tag)


for tag in tags:
	print(tag + " (" + conf.penn_treebank_tags[tag] + ")")



