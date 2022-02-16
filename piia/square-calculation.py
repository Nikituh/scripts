
from openpyxl import load_workbook
import types
import sys

FILENAME = "ruutude-arvutus-piiale-veebr2022"

workbook = load_workbook(filename = FILENAME + ".xlsx")
worksheet = workbook.active

# First gather all types into an object. This is a simple sheet, no need to define constants
type_sheet = workbook["elupaigatüüp_19"]
type_dict = {}
type_rows_total = type_sheet.max_row
for row in range(1, type_rows_total + 1):
	id = type_sheet[row][0].value
	type = type_sheet[row][1].value
	type_dict[id] = type

REPLACE_ID_START_ROW = 588
MAX_ROW = worksheet.max_row

PLANT_LISTING_COL_LEGACY = 0
PLANT_LISTING_COL = 1

for row in range(REPLACE_ID_START_ROW, MAX_ROW + 1):
	sys.stdout.write("\r")
	sys.stdout.write("Replacing legacy field name: " + str(row) + "/" + str(MAX_ROW))
	sys.stdout.flush()
	
	a_value = worksheet[row][PLANT_LISTING_COL_LEGACY].value
	if a_value is not None and a_value.startswith("2019"):
		worksheet[row][PLANT_LISTING_COL].value = a_value
		worksheet[row][PLANT_LISTING_COL_LEGACY].value = None

sys.stdout.write("\n")

BOX_CALCULATION_START_ROW = 43

# Collect all data from left columns and store in 'data' object
data = []
# Store row data in simple object
item = types.SimpleNamespace()
item.plants = []

for row in range(BOX_CALCULATION_START_ROW, MAX_ROW + 1):

	sys.stdout.write("\r")
	sys.stdout.write("Processing row data: " + str(row) + "/" + str(MAX_ROW))
	sys.stdout.flush()

	heading_text = worksheet[row][PLANT_LISTING_COL].value

	if heading_text is not None and heading_text.startswith("20"):
		# If it starts with '20', it's a new object start row.
		# Add current iteration object to result and clear previous item data collected
		data.append(item)

		item = types.SimpleNamespace()
		item.plants = []
		item.id = worksheet[row][1].value
		item.row_nr = row
		if item.id.startswith("2019"):
			# Only 2019 environments exist in type sheet, and the only ones necessary as well
			item.environment = type_dict[item.id]
		
	elif heading_text is not None:
		plant = types.SimpleNamespace()
		plant.habitat             = worksheet[row][2].value
		plant.human_tolerance     = worksheet[row][3].value
		plant.frequency           = worksheet[row][4].value
		plant.border_propoertion  = worksheet[row][5].value
		plant.conservation_status = worksheet[row][6].value
		plant.red_book            = worksheet[row][7].value
		plant.average_height      = worksheet[row][8].value
		plant.max_height          = worksheet[row][9].value
		plant.est_end             = worksheet[row][10].value
		plant.est_begin           = worksheet[row][11].value
		plant.est_persistence     = worksheet[row][12].value
		item.plants.append(plant)


ENVIRONMENT_COL     = 14
IDENTIFIER_COL      = 15
GRASSLAND_COL       = 16
FOREST_COL          = 17
WETLAND_COL         = 18
HUMAN_TOLERANCE_COL = 19
FREQUENCE_COL       = 20
PROPORTION_COL      = 21
CONSERV_STATUS_COL  = 22
RED_BOOK_COL        = 23
AVERAGE_HEIGHT_COL  = 24
MAX_HEIGHT_COL      = 25
EST_END             = 26
EST_BEGIN_COL       = 27
EST_PERSISTENCE_COL = 28

print(len(data))
for item in data:
	print(str(item))

workbook.save(FILENAME + "-output.xlsx")

print("Done! Processed " + str(MAX_ROW) + " rows")




