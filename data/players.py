import csv
import requests
from time import sleep
import datetime
from datetime import date
from bs4 import BeautifulSoup

wfile  = open('./data/players_age.csv', "wb")
rfile  = open('./data/players.csv', "rb")

reader = csv.reader(rfile, delimiter=';')
writer = csv.writer(wfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_NONE)

rownum = 0

for row in reader:
    if rownum == 0:
        writer.writerow(["id", "name", "team_name", "team_id", "position", "goals", "season", "comp_id", "age"])
    else:
        player_id = row[0][35:]
        r = requests.get("https://www.statbunker.com/players/getPlayerDetails?player_id="  +str(player_id))
        soup = BeautifulSoup(r.text, 'html.parser')

        elements = soup.find('tbody').find_all('td')
        born = datetime.datetime.strptime(elements[3].text, "%d %b %Y").date()
        today = date.today()
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        row.append(str(age))
        writer.writerow(row)
    rownum += 1
    if rownum % 5 == 0:
        print rownum
        sleep(1)

wfile.close()
rfile.close()