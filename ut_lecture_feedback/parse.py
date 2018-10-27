
# -*- coding: utf-8 -*-

import json
import os

FILENAME = "loengu-tagasiside-25.10-1"

STUDENT_NAME_KEY = "Ees- ja perekonnanimi"
PRESENTATION_SCORE_KEY = "Kuidas hindad esineja üldist esinemisoskust?"
DIFFICULTY_KEY = "Mis oli teemakäsitluse raskusaste?"

with open(FILENAME + ".json") as f:
    data = json.load(f)

for key, values in data.items():
	index = 0
	for value in values:
		if key == PRESENTATION_SCORE_KEY and value == 5:
			print(data[STUDENT_NAME_KEY][index])
			index += 1
