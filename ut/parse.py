# coding=utf-8

# pip install textract
import textract

extension = ".pdf"
folder_ma = "texts-ma/"
folder_ba = "texts-ba/"

files_ma = [
	"BLEHNER_SVEN_MA_THESIS",
	"Iila_Marit_MA_Thesis",
	"Kubre_Liisa_MA_Thesis",
	"Kümnik_Maret_MA_Thesis",
	"Laanepere_Lilian_MA_Thesis.pdf1",
	"Maatee, Sylvia. MA thesis",
	"Mugra_Siiri_MA_Thesis",
	"Parker_Helen_MA_Thesis",
	"Rahusaar_Anne_MA_Thesis",
	"Sagar_Sandra_MA_Thesis",
	"Thealane_Kairit_MA_Thesis",
	"Tihkan_Kristi_MA_Thesis",
	"Tiido_Terje_MA_Thesis",
	"Wu_GaoHeng_MA_Thesis"
]

files_ba = [
	"Eesalu_Mona_BA_Thesis",
	"Meriste_Liisa_BA_Thesis",
	"Roomäe_Annotated Transcript of Grammar Day",
	"Gaibli_Aibike_BA_Thesis",
	"Nook_Petra_BA_Thesis",
	"Roomäe_Kärt_BA_Thesis",
	"Gortalova_Jekaterina_BA_Thesis",
	"Näär_Kaisa-Liina_BA_Thesis",
	"Sai_Elizaveta_BA_Thesis",
	"Joemaa_Evelin_BA_Thesis",
	"Org_MariaRoberta_BA_Thesis",
	"Sünd_Siiri_BA_Thesis",
	"Kahur_Helen_BA",
	"Parksepp_Lotte_BA_Thesis",
	"Talviste_Eliseta_BA_Thesis",
	"Karilaid_Liis_BA_Thesis",
	"Peedumäe_Ander_BA_Thesis",
	"Teele_Männik_BA_24May2019",
	"Konno_Henry_BA_Thesis",
	"Peterson_Karl_BA_Thesis",
	"Tsebakov_Fjodor_BA_Thesis",
	"Mander_Monika_BA_Thesis",
	"Poopuu_Amanda_BA_Thesis",
	"Visnapuu_Karmen_BA_Thesis",
	"Melnik_Darja_BA_Thesis",
	"Rips_Elisabeth_BA_Thesis",
]

def calculate(folder, files):

	for file in files:
		path = folder + file + extension
		text = textract.process(path)

		split = text.split(" ")

		unique_words = {}

		for word in split:
			word = word.lower()
			if word not in unique_words:
				unique_words[word] = 1
			else:
				unique_words[word] += 1

		ratio = int((float(len(unique_words)) / float(len(split)) * 100)) / 100.0
		print("" + file + ": words: " + str(len(split)) + "; unique: " + str(len(unique_words)) + "; ratio: " + str(ratio))

calculate(folder_ma, files_ma)
calculate(folder_ba, files_ba)





