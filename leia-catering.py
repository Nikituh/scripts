
import requests
from bs4 import BeautifulSoup
import json

class Caterer:

	def __init__(self):
		pass

	def from_row(row): 
		caterer = Caterer()

		caterer.name =  row.find("div", {"class": "caterer-title"}).find("a").text.strip()
		caterer.phone = row.find("div", {"class": "service-details--phone"}).text.strip()
		caterer.email = row.find("div", {"class": "service-details--email"}).text.strip()
		caterer.site =  row.find("div", {"class": "service-details--homepage"}).find("a")["href"].strip()

		return caterer


PAGE_COUNT = 13

caterers = []

for index in range(PAGE_COUNT):
	page_number = index + 1
	html = requests.get("https://leiacatering.ee/?page=" + str(page_number)).text
	soup = BeautifulSoup(html, 'html.parser')

	for row in soup.find_all("div", {"class": "caterer-box"}):
		caterer = Caterer.from_row(row)
		caterers.append(caterer)

with open("leia-catering.json", "w", encoding='utf-8') as file:
        json.dump([caterer.__dict__ for caterer in caterers], file, indent=4, ensure_ascii=False)