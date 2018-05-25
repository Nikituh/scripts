
import docx2txt
import operator

SOURCE_FILE_NAME = "raw_texts/MA Thesis.docx"

source_texts = docx2txt.process(SOURCE_FILE_NAME)

# print(source_texts)
print(str(len(source_texts.split(" "))))

split = source_texts.split(" ")

unique_words = {}

for word in split:
	word = word.lower()
	if word not in unique_words:
		unique_words[word] = 1
	else:
		unique_words[word] += 1


print(str(len(unique_words)))

sorted_unique_words = sorted(unique_words.items(), key=operator.itemgetter(1), reverse=True)

counter = 0

for word in sorted_unique_words:
	if counter < 20:
		print(word[0] + ": " + str(word[1]))
		counter += 1