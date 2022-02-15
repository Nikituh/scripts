
from openpyxl import load_workbook

FILENAME = "ruutude-arvutus-piiale-veebr2022"

workbook = load_workbook(filename = FILENAME + ".xlsx")
worksheet = workbook.active

START_ROW = 2
MAX_ROW = worksheet.max_row

for row in range(START_ROW, MAX_ROW):
	# This is executed 3059 times
	column_a = 0
	column_b = 1
	a_value = worksheet[row][column_a].value
	if a_value is not None and a_value.startswith("2019"):
		worksheet[row][column_b].value = a_value
		worksheet[row][column_a].value = None


workbook.save(FILENAME + "-output.xlsx")

print("Done!")
