# https://www.statbunker.com/competitions/LeagueTable?comp_id=556

import csv
import requests
from time import sleep
from bs4 import BeautifulSoup

wfile  = open('./data/comp_extra.csv', "wb")
writer = csv.writer(wfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_NONE)

competitions = [374, 369, 375, 377, 373, 378, 416, 419, 412, 414, 415, 413, 447, 455, 454, 462, 449, 461, 483, 491, 486, 492, 481, 484, 485, 516, 521, 517, 520, 515, 514, 518]

writer.writerow(["comp_id", "team_name", "goals_for", "goals_against", "points"])

for competition in competitions:
    r = requests.get("https://www.statbunker.com/competitions/LeagueTable?comp_id="+str(competition))
    soup = BeautifulSoup(r.text, 'html.parser')
    rows = soup.find('tbody').find_all('tr')

    for row in rows:
        elements = row.find_all('td')
        writer.writerow([str(competition), elements[1].text, elements[6].text, elements[7].text, elements[9].text])

    sleep(5)

wfile.close()
rfile.close()