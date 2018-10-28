
# -*- coding: utf-8 -*-

import json
import os

FILENAME = "loengu-tagasiside-25.10-1"
TYPE = "_by_row"

def get_percentage(part, whole):
  return 100 * float(part)/float(whole)

with open(FILENAME + TYPE + ".json") as f:
    data = json.load(f)

lowest_performance = 5
lowest_difficulty = 5

total = len(data)
top_notch_performance = 0
total_performance_score = 0.0

for review in data:
	performance = review["performance_score"]
	difficulty = review["difficulty_score"]

	if lowest_performance > performance:
		lowest_performance = performance

	if lowest_difficulty > difficulty:
		lowest_difficulty = difficulty


	if performance == 5:
		top_notch_performance += 1

	total_performance_score += performance

print("Performance mean: " + str(total_performance_score / total))
print("Top notch performance: " + str(get_percentage(top_notch_performance, total)) + "%")
# print(lowest_performance)
# print(lowest_difficulty)


