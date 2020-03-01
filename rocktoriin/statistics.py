
import xlrd 
import operator

loc = ("lood.xlsx") 
  
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0) 

class Question:
	def __init__(self, artist, song):
		self.artist = artist
		self.song = song

questions = []

artists = {}
songs = {}

for i in range(sheet.nrows): 
	artist = sheet.cell_value(i, 1)
	song = sheet.cell_value(i, 2)
	questions.append(Question(artist, song))

for question in questions:

	if question.artist in artists:
		artists[question.artist] += 1
	else:
		artists[question.artist] = 1

	if question.song in songs:
		songs[question.song] += 1
	else:
		songs[question.song] = 1

sorted_artist_count = sorted(artists.items(), key=operator.itemgetter(1), reverse=True)

counter = 1
for key, value in sorted_artist_count:
    print(str(counter) + ". " + str(key) + " (" + str(value) + ")")
    counter += 1
    if counter == 11:
    	break


sorted_song_count = sorted(songs.items(), key=operator.itemgetter(1), reverse=True)

counter = 1
for key, value in sorted_song_count:
    print(str(counter) + ". " + str(key) + " (" + str(value) + ")")
    counter += 1
    if counter == 11:
    	break





