
import operator

folder = "manually-analyzed/"
base_file_name = "parsed-text-manually-analyzed-"
extension = ".txt"

filenames = [
	folder + base_file_name + "1" + extension,
	folder + base_file_name + "2" + extension,
	folder + base_file_name + "3" + extension,
	folder + base_file_name + "4" + extension,
	folder + base_file_name + "5" + extension,
	# folder + base_file_name + "6" + extension,
]

counter = 1

overall_tag_count = 0

total_tag_counts = {}


for name in filenames:
	with open(name, 'r') as file:
		lines = file.readlines()

		essay_tag_counts = {}

		for line in lines:
			if "(" in line and ")" in line: 
				entities = line.replace(".", "").replace(",", "").replace(":", "").replace("?", "")
				entities = entities.strip().split(" ")

				word = entities[0]
				tag = entities[1]

				if tag in essay_tag_counts:
					essay_tag_counts[tag] += 1
				else:
					essay_tag_counts[tag] = 1

				if tag in total_tag_counts:
					total_tag_counts[tag] += 1
				else:
					total_tag_counts[tag] = 1

				overall_tag_count += 1;

		sorted_counts = sorted(essay_tag_counts.items(), key=operator.itemgetter(1), reverse=True)

		print("Tag count in essay " + str(counter) + ":")
		print(sorted_counts)
		print("\n")

		counter += 1

sorted_counts = sorted(total_tag_counts.items(), key=operator.itemgetter(1), reverse=True)

print("Total tag count:")
print(sorted_counts)
print("\n")

print(overall_tag_count)