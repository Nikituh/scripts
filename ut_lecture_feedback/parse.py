
# -*- coding: utf-8 -*-

import json
import os

MAX = 5
MIN = 1

FILENAME = "loengu-tagasiside-25.10-1"
TYPE = "_by_row"

def get_percentage(part, whole):
  return 100 * float(part)/float(whole)

with open(FILENAME + TYPE + ".json") as f:
    data = json.load(f)

lowest_performance = 5
lowest_difficulty = 5

top_score_count = 0
lowest_score_count = 0

total = len(data)
total_performance_score = 0.0

for review in data:
	performance = review["performance_score"]
	difficulty = review["difficulty_score"]

	if lowest_performance > performance:
		lowest_performance = performance

	if lowest_difficulty > difficulty:
		lowest_difficulty = difficulty


	if performance == 5:
		top_score_count += 1

	if performance == 2:
		lowest_score_count += 1;

	total_performance_score += performance

print("Lowest difficulty: " + str(lowest_difficulty))
print("Lowest performance : " + str(lowest_performance))

print("Performance mean: " + str(total_performance_score / total))

print("Highest performance percentage: " + str(round(get_percentage(top_score_count, total))) + "%")
print("Lowest performance percentage: " + str(round(get_percentage(lowest_score_count, total))) + "%")






