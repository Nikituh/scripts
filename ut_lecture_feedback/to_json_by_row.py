
# pip install openpyxl
import openpyxl
import json
import datetime
import io

FILENAME = "loengu-tagasiside-25.10-1"
SOURCE_EXTENSION = ".xlsx"
DESTINATION_EXTENSION = ".json"

EPOCH = datetime.datetime.utcfromtimestamp(0)
# https://stackoverflow.com/questions/6999726/how-can-i-convert-a-datetime-object-to-milliseconds-since-epoch-unix-time-in-p
def unix_time_millis(dt):
    return (dt - EPOCH).total_seconds() * 1000.0

book = openpyxl.load_workbook(FILENAME + SOURCE_EXTENSION)
rows = book.active.rows

destination_content = []

for row in rows:
	
	# Timestamp
	timestamp = row[0].value

	if timestamp is None:
		# The sheet contains empty rows. This ensures we're not parsing an empty row
		continue

	if timestamp == "Timestamp":
		# This ensures we're not parsing the first row, containing headers
		continue
	
	# Timestamp is not serializable, translate it to milliseconds
	timestamp = unix_time_millis(timestamp)

	# Ees- ja perekonnanimi
	student_name = row[1].value
	# Esineja nimi
	lecturer_name = row[2].value
	# Kuidas hindad esineja üldist esinemisoskust?
	performance_score = row[3].value
	# Mis oli teemakäsitluse raskusaste?
	difficulty_score = row[4].value
	# Too välja üks mõte või teadmine, mille Sina sellest loengust kaasa võtad.
	new_information = row[5].value
	# Kas oli teemasid, millest oleksid tahtnud selles loengus (rohkem) kuulda?
	wanted_to_hear_more = row[6].value
	# Mis teemasid oleks võinud lisaks/rohkem käsitleda?
	topic_wanted_to_hear_more = row[7].value
	# Kas oskaksid sellest loengust nimetada midagi, millega olid varasemalt juba kursis.
	student_already_aware_of = row[8].value

	review = {
		"student_name": student_name,
		"lecturer_name": lecturer_name,
		"performance_score": performance_score,
		"difficulty_score": difficulty_score,
		"new_information": new_information,
		"wanted_to_hear_more": wanted_to_hear_more,
		"topic_wanted_to_hear_more": topic_wanted_to_hear_more,
		"student_already_aware_of": student_already_aware_of
	}

	destination_content.append(review)

# encoding="utf-8" requires python3:
# brew install python3
# pip3 install openpyxl
with open(FILENAME + "_by_row" + DESTINATION_EXTENSION, "w", encoding="utf-8") as file:
	json.dump(destination_content, file, indent=4, ensure_ascii=False)

print("Done!")





