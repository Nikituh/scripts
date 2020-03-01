
import xlrd 
import operator

loc = ("lood.xlsx") 
  
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0) 

artists = {}
songs = {}

for i in range(sheet.nrows): 
	artist = sheet.cell_value(i, 1)
	song = sheet.cell_value(i, 2)

	if artist in artists:
		artists[artist] += 1
	else:
		artists[artist] = 1

	if song in songs:
		songs[song] += 1
	else:
		songs[song] = 1

# sorted_artist_count = sorted(artists.items(), key=operator.itemgetter(1), reverse=True)

# counter = 1
# for key, value in sorted_artist_count:
#     print(str(counter) + ". " + str(key) + " (" + str(value) + ")")
#     counter += 1
#     if counter == 11:
#     	break


sorted_song_count = sorted(songs.items(), key=operator.itemgetter(1), reverse=True)

counter = 1
for key, value in sorted_song_count:
    print(str(counter) + ". " + str(key) + " (" + str(value) + ")")
    counter += 1
    if counter == 11:
    	break