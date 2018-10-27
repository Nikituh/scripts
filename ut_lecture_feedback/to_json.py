
# -*- coding: utf-8 -*-

### Script to simply read .xlsx and write it to .json,
### data parsing is done in separate files
### because fuck everything about that format

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

columns = [ 
	"A", # Timestamp
	"B", # Ees- ja perekonnanimi
	"C", # Esineja nimi
	"D", # Kuidas hindad esineja üldist esinemisoskust?
	"E", # Mis oli teemakäsitluse raskusaste?
	"F", # Too välja üks mõte või teadmine, mille Sina sellest loengust kaasa võtad.
	"G", # Kas oli teemasid, millest oleksid tahtnud selles loengus (rohkem) kuulda?
	"H", # Mis teemasid oleks võinud lisaks/rohkem käsitleda?
	"I"  # Kas oskaksid sellest loengust nimetada midagi, millega olid varasemalt juba kursis.
]

book = openpyxl.load_workbook(FILENAME + SOURCE_EXTENSION)
sheet = book.active

destination_content = {}

for column in columns:

	index = 0
	header = ""

	for item in sheet[column]:

		if index == 0:
			header = item.value
			destination_content[header] = []
		else:
			value = item.value

			if value == None:
				# The file contains blank rows, ignore them
				continue

			if header == "Timestamp":
				# Timestamp is not serializable, translate it to milliseconds
				value = unix_time_millis(value)

			destination_content[header].append(value)
		
		index += 1

# encoding="utf-8" requires python3:
# brew install python3
# pip3 install openpyxl
with open(FILENAME + DESTINATION_EXTENSION, "w", encoding="utf-8") as file:
	json.dump(destination_content, file, indent=4, ensure_ascii=False)

print("Done!")






