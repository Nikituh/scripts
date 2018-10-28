
# -*- coding: utf-8 -*-

import json
import os

FILENAME = "loengu-tagasiside-25.10-1"
TYPE = "_by_row"

with open(FILENAME + TYPE + ".json") as f:
    data = json.load(f)

for review in data:
	if review["difficulty_score"] == 5:
		print review["student_name"]
